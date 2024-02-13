import requests
from abc import ABC, abstractmethod
from typing import Type, Generic, TypeVar, Set
from pydantic import BaseModel
from pypolygon.key import APIKey

ResponseType = TypeVar('ResponseType', bound=BaseModel)

def snake_to_camel(s: str) -> str:
    tokens = s.split('_')
    return tokens[0] + ''.join(token.title() for token in tokens[1:])

def convert_url_param(s: str) -> str:
    # Special exception for keywords "from" and "to" since
    # "from" is a reserved keyword in Python
    if s == "range_from":
        return "from"
    if s == "range_to":
        return "to"
    return snake_to_camel(s)

_BASE_URL = "https://api.polygon.io"

class PolygonEndpoint(ABC, Generic[ResponseType]):
    
    url_format: str
    url_params: Set[str]
    query_params: Set[str]
    response_model: Type[ResponseType]
    
    _response: ResponseType
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    def _execute(self, **kwargs) -> ResponseType:
        
        # Select the url parameters
        try:
            url_params = {convert_url_param(param): kwargs[param] for param in self.url_params}
        except KeyError as e:
            raise ValueError(f"Missing url parameter: {e}")

        # Select the query parameters
        query_params = {snake_to_camel(param): str(kwargs[param]) 
                        for param in self.query_params if param in kwargs}
        
        # If the API key is not provided, use the default key
        if 'apiKey' not in query_params:
            query_params['apiKey'] = APIKey().get_key()
        
        # Construct the URL
        url = _BASE_URL + self.url_format.format(**url_params)
        
        # Make the request
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.get(url, params=query_params, headers=headers)
        rjson = response.json()
        
        print(rjson)
        
        self._response = self.response_model.model_validate(rjson) 
    
    @property
    def response(self) -> ResponseType:
        return self._response
    
if __name__ == "__main__":
    
    class AggregatesResponse(BaseModel):
        ticker: str
        queryCount: int
    
    class AggregatesEndpoint(PolygonEndpoint):
        
        url_format = r"/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/2024-01-01/{to}"
        url_params = {"stocks_ticker", "multiplier", "timespan", "range_from", "range_to"}
        query_params = {"adjusted", "sort", "limit", "api_key"}
        response_model = AggregatesResponse
        
        
        def __init__(self) -> None:
            self._execute(stocks_ticker="AAPL", 
                          multiplier=1, 
                          timespan="day", 
                          range_from="2024-01-01",
                          range_to="2024-01-10")
            
    agg = AggregatesEndpoint()
    print(agg.response)
    
    