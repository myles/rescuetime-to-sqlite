import pytest
import responses
from responses import matchers

from rescuetime_to_sqlite import client


@responses.activate
@pytest.mark.parametrize(
    "params, expected_params",
    (
        (None, None),
        (
            {"i-am-a-query-param": "i-am-a-query-param-value"},
            "i-am-a-query-param=i-am-a-query-param-value",
        ),
    ),
)
def test_rescuetime_client__request(params, expected_params):
    key = "IAmARescueTimeAPIKey"
    url = "https://www.rescuetime.com/anapi/example"

    if params is None:
        params = {}

    params["key"] = key

    responses.add(
        responses.Response(
            method="GET",
            url=url,
            match=[
                matchers.query_string_matcher(
                    f"format=json&{expected_params}&key={key}"
                ),
            ],
        ),
    )

    rt_client = client.RescueTimeClient(key=key)
    rt_client.request(url=url, params=params)

    assert len(responses.calls) == 1
