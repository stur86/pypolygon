from typing import Any, List
from string import Formatter

class APIUrl:
    
    _fmt: str
    _params: List[str]
    
    def __init__(self, url_fmt: str) -> None:
        
        self._fmt = url_fmt
        
        # Find the url parameters
        self._params = []
        for _, param, _, _ in Formatter().parse(url_fmt):
            if param is not None:
                self._params.append(param)
    
    @property
    def fmt(self) -> str:
        return self._fmt
    
    @property
    def params(self) -> List[str]:
        return self._params
    
    def __call__(self, *args: Any, **kwds: Any) -> str:
        
        # Check that the keyword arguments are a subset of the parameters
        if not set(kwds.keys()).issubset(set(self._params)):
            raise ValueError("Invalid keyword argument")
        
        if len(args) + len(kwds) != len(self._params):
            raise ValueError("Invalid number of arguments")
        
        for i, a in enumerate(args):
            kwds[self._params[i]] = a
            
        return self._fmt.format(**kwds)