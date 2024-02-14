from pypolygon.endpoint import PolygonEndpoint
from pypolygon.url import APIUrl
from pypolygon.models.reference import TickersResponse


class TickersEndpoint(PolygonEndpoint[TickersResponse]):
    def __init__(self) -> None:
        url = APIUrl("/v3/reference/tickers")
        query_params = [
            "ticker",
            "type",
            "market",
            "exchange",
            "cusip",
            "cik",
            "date",
            "search",
            "active",
            "order",
            "limit",
            "sort",
        ]
        super().__init__(url, query_params, TickersResponse)

    def __call__(
        self,
        ticker: str = "",
        type: str = "",
        market: str = "",
        exchange: str = "",
        cusip: str = "",
        cik: str = "",
        date: str = "",
        search: str = "",
        active: bool = True,
        order: str = "asc",
        limit: int = 100,
        sort: str = "ticker",
    ) -> TickersResponse:
        return super()._execute(
            ticker=ticker,
            type=type,
            market=market,
            exchange=exchange,
            cusip=cusip,
            cik=cik,
            date=date,
            search=search,
            active=active,
            order=order,
            limit=limit,
            sort=sort,
        )


if __name__ == "__main__":

    endpoint = TickersEndpoint()

    ans = endpoint(ticker="C*")

    for r in ans.results:
        print(r.ticker, "\t", r.name)
