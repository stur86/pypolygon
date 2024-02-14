from pypolygon.endpoint import PolygonEndpoint
from pypolygon.url import APIUrl
from pypolygon.models.market import GroupedDailyResponse

class GroupedDailyEndpoint(PolygonEndpoint[GroupedDailyResponse]):

    def __init__(self) -> None:
        url = APIUrl(
            "/v2/aggs/grouped/locale/us/market/stocks/{date}"
        )
        query_params = ["adjusted", "include_otc"]
        super().__init__(url, query_params, GroupedDailyResponse)

    def __call__(
        self,
        date: str,
        adjusted: bool = True,
        include_otc: bool = False,
    ) -> GroupedDailyResponse:
        return super()._execute(
            date=date,
            adjusted=adjusted,
            include_otc=include_otc,
        )


if __name__ == "__main__":

    endpoint = GroupedDailyEndpoint()

    ans = endpoint(
        date="2024-02-13",
    )
    
    print(ans)