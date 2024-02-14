import pytest
from pypolygon.models.market import TickerResult


def test_tickers():
    
    t1 = TickerResult(
        c=1,
        h=2,
        l=0,
        n=100,
        o=0.5,
        t=1000,
        v=1000,
        vw=1,
        otc=True,
        T="AAPL"
    )
    
    t2 = TickerResult(
        c=2,
        h=3,
        l=1,
        n=100,
        o=1,
        t=2000,
        v=1000,
        vw=2,
        otc=True,
        T="AAPL"
    )
    
    tsum = TickerResult.aggregate([t1, t2])
    
    assert tsum.c == 2
    assert tsum.h == 3
    assert tsum.l == 0
    assert tsum.n == 200
    assert tsum.o == 0.5
    assert tsum.t == 1000
    assert tsum.v == 2000
    assert tsum.vw == 1.5
    assert tsum.otc
    assert tsum.T == "AAPL"
    
    # Try with different tickers
    t2.T = "TSLA"
    
    with pytest.raises(ValueError):
        TickerResult.aggregate([t1, t2])
        