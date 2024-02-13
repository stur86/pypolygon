from typing import Optional, List
from pydantic import BaseModel

class TickerResult(BaseModel):
    c: float
    h: float
    l: float  # noqa: E741
    n: int
    o: float
    t: int
    v: int
    vw: float
    ticker: Optional[str] = None

class AggregatesResponse(BaseModel):
    adjusted: bool
    queryCount: int
    request_id: str
    results: List[TickerResult]
    resultsCount: int
    status: str
    ticker: str
