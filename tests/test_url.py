import pytest
from pypolygon.url import APIUrl


def test_url():
    
    url = APIUrl("/v2/test/{firstParam}/{secondParam}")
    
    assert url.fmt == "/v2/test/{firstParam}/{secondParam}"
    assert url.params == ["first_param", "second_param"]
    
    assert url(first_param="test1", second_param="test2") == "/v2/test/test1/test2"
    assert url("test1", "test2") == "/v2/test/test1/test2"
    assert url("test1", second_param="test2") == "/v2/test/test1/test2"
    
    # Should raise ValueError
    with pytest.raises(ValueError):
        url("test1")