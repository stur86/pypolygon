from typing import Any
from pypolygon.endpoint import PolygonEndpoint, _BASE_URL
from pypolygon.url import APIUrl
from pydantic import BaseModel

def test_endpoint(requests_mock, monkeypatch):
        
        class TestModel(BaseModel):
            msg: str
            
        class TestEndpoint(PolygonEndpoint[TestModel]):
            
            def __init__(self) -> None:
                url = APIUrl("/v2/test/{firstParam}/{secondParam}")
                query_params = ["name"]
                super().__init__(url, query_params, TestModel)
            
            def __call__(self, *args: Any, **kwds: Any) -> TestModel:
                 return super()._execute(*args, **kwds)
        
        endpoint = TestEndpoint()        
        monkeypatch.setenv("POLYGON_API_KEY", "TESTKEY")
        
        requests_mock.get(f"{_BASE_URL}/v2/test/test1/test2?name=test3&apiKey=TESTKEY", json={"msg": "test", "status": "OK"})
            
        ans = endpoint(first_param="test1", second_param="test2", name="test3")
                        
        assert ans.msg == "test"