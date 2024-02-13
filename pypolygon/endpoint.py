import requests
from abc import ABC, abstractmethod
from typing import Any, Type, Generic, TypeVar, Set, Iterable
from pydantic import BaseModel
from pypolygon.key import APIKey
from pypolygon.url import APIUrl

ResponseType = TypeVar("ResponseType", bound=BaseModel)

_BASE_URL = "https://api.polygon.io"


class PolygonEndpoint(ABC, Generic[ResponseType]):

    _url: APIUrl
    _query_params: Set[str]
    _response_model: Type[ResponseType]

    def __init__(
        self,
        url: APIUrl,
        query_params: Iterable[str],
        resposnse_model: Type[ResponseType],
    ) -> None:

        self._url = url
        self._query_params = set(query_params)
        self._response_model = resposnse_model
        
    def _execute(self, **kwargs: Any) -> ResponseType:

        # Select the query parameters
        query_params = {k: str(v) for k, v in kwargs.items() if k in self._query_params}

        # If the API key is not provided, use the default key
        if "apiKey" not in query_params:
            query_params["apiKey"] = APIKey().get_key()

        url_params = {k: v for k, v in kwargs.items() if k not in self._query_params}

        # Construct the URL
        url = _BASE_URL + self._url(**url_params)

        # Make the request
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        response = requests.get(url, params=query_params, headers=headers)
        rjson = response.json()
        
        return self._response_model.model_validate(rjson)
    
    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> ResponseType:
        return self._execute(*args, **kwds)