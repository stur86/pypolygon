import pytest
from pypolygon.url import APIUrl


def test_url():
    
    url = APIUrl("/v2/test/{param1}/{param2}")
    
    assert url.fmt == "/v2/test/{param1}/{param2}"
    assert url.params == ["param1", "param2"]
    
    
    assert url(param1="test1", param2="test2") == "/v2/test/test1/test2"
    assert url("test1", "test2") == "/v2/test/test1/test2"
    assert url("test1", param2="test2") == "/v2/test/test1/test2"
    
    # Should raise ValueError
    with pytest.raises(ValueError):
        url("test1")