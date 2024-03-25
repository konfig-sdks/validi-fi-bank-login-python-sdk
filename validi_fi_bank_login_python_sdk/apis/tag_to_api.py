import typing_extensions

from validi_fi_bank_login_python_sdk.apis.tags import TagValues
from validi_fi_bank_login_python_sdk.apis.tags.connect_api import CONNECTApi
from validi_fi_bank_login_python_sdk.apis.tags.token_api import TokenApi
from validi_fi_bank_login_python_sdk.apis.tags.insights_api import InsightsApi
from validi_fi_bank_login_python_sdk.apis.tags.reports_api import ReportsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONNECT: CONNECTApi,
        TagValues.TOKEN: TokenApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.REPORTS: ReportsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONNECT: CONNECTApi,
        TagValues.TOKEN: TokenApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.REPORTS: ReportsApi,
    }
)
