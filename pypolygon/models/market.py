from typing import Optional, List
from pydantic import BaseModel, Field

class TickerResult(BaseModel):
    c: float = Field(..., description="Close price")
    h: float = Field(..., description="Highest price")
    l: float = Field(..., description="Lowest price")  # noqa: E741
    n: int = Field(..., description="Number of transactions")
    o: float = Field(..., description="Open price")
    t: int = Field(..., description="Unix Msec Timestamp")
    v: int = Field(..., description="Trading volume")
    vw: float = Field(..., description="Volume weighted average price")
    otc: Optional[bool] = Field(None, description="Over the counter")
    ticker: Optional[str] = Field(None, description="Ticker name")
    
    
    @classmethod
    def aggregate(cls, data: List["TickerResult"]) -> "TickerResult":
        # Sort by timestamp
        data = sorted(data, key=lambda x: x.t)
        
        otc_0 = data[0].otc
        ticker_0 = data[0].ticker
        
        if not all([x.otc == otc_0 for x in data]):
            raise ValueError("OTC mismatch")

        if not all([x.ticker == ticker_0 for x in data]):
            raise ValueError("Ticker mismatch")
        
        o_tot = data[0].o
        c_tot = data[-1].c
        n_tot = sum([x.n for x in data])
        v_tot = sum([x.v for x in data])
        h_tot = max([x.h for x in data])
        l_tot = min([x.l for x in data])
        t_tot = data[0].t
        vw_tot = sum([x.vw*x.v for x in data]) / v_tot
        
        return cls(
            o=o_tot,
            c=c_tot,
            h=h_tot,
            l=l_tot,
            n=n_tot,
            t=t_tot,
            v=v_tot,
            vw=vw_tot,
            otc=otc_0,
            ticker=ticker_0
        )
        
class AggregatesResponse(BaseModel):
    adjusted: bool
    queryCount: int
    request_id: str
    results: List[TickerResult]
    resultsCount: int
    status: str
    ticker: str
