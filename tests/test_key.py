import pytest
from pypolygon.key import APIKey

def test_key(monkeypatch):
    
    monkeypatch.delenv('POLYGON_API_KEY')
    
    # Should raise ValueError
    with pytest.raises(ValueError):
        APIKey.get_key()    
    
    monkeypatch.setenv('POLYGON_API_KEY', 'test_key')
    
    assert APIKey.get_key() == 'test_key'
    
    # Clean up
    monkeypatch.delenv('POLYGON_API_KEY')