from typing import Optional, List
from pydantic import BaseModel, Field

class TickerResult(BaseModel):
    c: float = Field(..., description="Close price")
    h: float = Field(..., description="Highest price")
    l: float = Field(..., description="Lowest price")  # noqa: E741
    o: float = Field(..., description="Open price")
    t: int = Field(..., description="Unix Msec Timestamp")
    v: float = Field(..., description="Trading volume")
    n: Optional[int] = Field(None, description="Number of transactions")
    vw: Optional[float] = Field(None, description="Volume weighted average price")
    otc: Optional[bool] = Field(None, description="Over the counter")
    T: Optional[str] = Field(None, description="Ticker name")
    
    
    @classmethod
    def aggregate(cls, data: List["TickerResult"]) -> "TickerResult":
        # Sort by timestamp
        data = sorted(data, key=lambda x: x.t)
        
        otc_0 = data[0].otc
        ticker_0 = data[0].T
        
        if not all([x.otc == otc_0 for x in data]):
            raise ValueError("OTC mismatch")

        if not all([x.T == ticker_0 for x in data]):
            raise ValueError("Ticker mismatch")
        
        o_tot = data[0].o
        c_tot = data[-1].c
        v_tot = sum([x.v for x in data])
        h_tot = max([x.h for x in data])
        l_tot = min([x.l for x in data])
        t_tot = data[0].t
        
        # n and vw are optional
        if any([x.n is None for x in data]):
            n_tot = None
        else:  
            n_tot = sum([x.n for x in data])

        if any([x.vw is None for x in data]):
            vw_tot = None
        else:
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
            T=ticker_0
        )

class BaseAggregatesResponse(BaseModel):
    adjusted: bool
    queryCount: int
    request_id: str
    resultsCount: int
    status: str        

        
class AggregatesResponse(BaseAggregatesResponse):
    ticker: str
    results: List[TickerResult]

class GroupedDailyResponse(BaseAggregatesResponse):
    results: List[TickerResult]