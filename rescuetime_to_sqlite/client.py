import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple, TypedDict, Union

from requests import PreparedRequest, Request, Response, Session


class Perspective(str, Enum):
    RANK = "rank"
    INTERVAL = "interval"


class ResolutionTime(str, Enum):
    MONTH = "month"
    WEEK = "week"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"


class RestrictKind(str, Enum):
    CATEGORY = "category"
    ACTIVITY = "activity"
    PRODUCTIVITY = "productivity"
    DOCUMENT = "document"
    EFFICIENCY = "efficiency"


class RestrictSourceType(str, Enum):
    COMPUTERS = "computers"
    MOBILE = "mobile"
    OFFLINE = "offline"


class RescueTimeClient:
    def __init__(self, key: str):
        self.key = key

        self.analytic_data_api_url = "https://www.rescuetime.com/anapi/data"
        self.daily_summary_feed_api_url = (
            "https://www.rescuetime.com/anapi/daily_summary_feed"
        )
        self.highlights_feed_api_url = (
            "https://www.rescuetime.com/anapi/highlights_feed"
        )

        self.session = Session()

        user_agent = "rescuetime-to-sqlite (+https://github.com/myles/rescuetime-to-sqlite)"
        self.session.headers["User-Agent"] = user_agent

    def request(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[Tuple[int, int]] = None,
        **kwargs,
    ) -> Tuple[PreparedRequest, Response]:
        """
        Makes a basic request to RescueTime.
        """
        if params is None:
            params = {}

        if "key" not in params:
            params["key"] = self.key

        # We want to use JSON as the format by default.
        if "format" not in params:
            params["format"] = "json"

        request = Request(method="GET", url=url, params=params, **kwargs)

        prepped = self.session.prepare_request(request)
        response = self.session.send(prepped, timeout=timeout)

        return prepped, response

    def get_analytic_data(
        self,
        perspective: Perspective = Perspective.RANK,
        resolution_time: ResolutionTime = ResolutionTime.HOUR,
        restrict_begin: Optional[datetime.date] = None,
        restrict_end: Optional[datetime.date] = None,
        restrict_kind: Optional[RestrictKind] = None,
        restrict_thing: Optional[str] = None,
        restrict_thingy: Optional[str] = None,
        restrict_source_type: Optional[RestrictSourceType] = None,
        restrict_schedule_id: Optional[int] = None,
    ) -> Tuple[PreparedRequest, Response]:
        """
        Returns Analytic Data API.

        RescueTime data is detailed and complicated. The Analytic Data API is
        targeted at bringing developers the prepared and pre-organized data
        structures already familiar through the reporting views of
        www.rescuetime.com. The data is read-only through the webservice, but
        you can perform any manipulations on the consumer side you want. Keep
        in mind this is a draft interface, and may change in the future. We do
        intend to version the interfaces though, so it is likely forward
        compatible.
        """
        params = {
            "perspective": perspective,
            "resolution_time": resolution_time,
        }

        if restrict_begin is not None:
            params["restrict_begin"] = restrict_begin.isoformat()

        if restrict_end is not None:
            params["restrict_end"] = restrict_end.isoformat()

        if restrict_kind is not None:
            if (
                restrict_kind == RestrictKind.EFFICIENCY
                and perspective != Perspective.INTERVAL
            ):
                raise ValueError(
                    f"You can only use {restrict_kind!r} with perspective={Perspective.INTERVAL}"
                )

            params["restrict_kind"] = restrict_kind

        if restrict_thing is not None:
            params["restrict_thing"] = restrict_thing

        if restrict_thingy is not None:
            params["restrict_thingy"] = restrict_thingy

        if restrict_source_type is not None:
            params["restrict_source_type"] = restrict_source_type

        if restrict_schedule_id is not None:
            params["restrict_schedule_id"] = str(restrict_schedule_id)

        return self.request(self.analytic_data_api_url, params=params)

    def get_daily_summary_feed(self) -> Tuple[PreparedRequest, Response]:
        """
        Returns Daily Summary Feed API.

        The Daily Summary Feed API provides a high level rollup of the time a
        user has logged for a full 24-hour period (defined by the user's
        selected time zone). This is useful for generating notifications that
        don't need to be real-time and don't require much granularity (for
        greater precision or more timely alerts, see the Alerts Feed API). This
        can be used to construct a customized daily progress report delivered
        via email. The summary can also be used to alert people to specific
        conditions.
        """
        return self.request(self.daily_summary_feed_api_url)

    def get_highlights_feed(self) -> Tuple[PreparedRequest, Response]:
        """
        Returns Highlights Feed API.

        The Highlights Feed API is a list of recently entered Daily Highlight
        events. These are user-entered strings that are meant to provide
        qualitative context for the automatically logged time about the user's
        activities. It is often used to keep a log of "what got done today".
        Highlights are a premium feature and as such the API will always return
        zero results for users on the RescueTime Lite plan.
        """
        return self.request(self.highlights_feed_api_url)


class AnalyticData(TypedDict):

    notes: str
    row_headers: List[str]
    rows: List[List[Union[str, int]]]
