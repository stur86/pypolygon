from pypolygon.endpoint import PolygonEndpoint
from pypolygon.url import APIUrl
from pypolygon.models.market import AggregatesResponse


class AggregatesEndpoint(PolygonEndpoint[AggregatesResponse]):

    def __init__(self) -> None:
        url = APIUrl(
            "/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from}/{to}"
        )
        query_params = ["adjusted", "sort", "limit"]
        super().__init__(url, query_params, AggregatesResponse)

    def __call__(
        self,
        stocks_ticker: str,
        timespan: str,
        range_from: str,
        range_to: str,
        multiplier: int = 1,
        adjusted: bool = True,
        sort: str = "asc",
        limit: int = 10000,
    ) -> AggregatesResponse:
        return super()._execute(
            stocks_ticker=stocks_ticker,
            timespan=timespan,
            range_from=range_from,
            range_to=range_to,
            multiplier=multiplier,
            adjusted=adjusted,
            sort=sort,
            limit=limit,
        )


if __name__ == "__main__":

    endpoint = AggregatesEndpoint()

    ans = endpoint(
        stocks_ticker="AAPL",
        timespan="day",
        range_from="2024-01-01",
        range_to="2024-01-05",
    )

    print(ans)
