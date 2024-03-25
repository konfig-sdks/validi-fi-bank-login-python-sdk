import typing_extensions

from validi_fi_bank_login_python_sdk.paths import PathValues
from validi_fi_bank_login_python_sdk.apis.paths.v4_token import V4Token
from validi_fi_bank_login_python_sdk.apis.paths.v4_health_check import V4HealthCheck
from validi_fi_bank_login_python_sdk.apis.paths.v4_insights import V4Insights
from validi_fi_bank_login_python_sdk.apis.paths.v4_insights_2_inquiry_id import V4Insights2InquiryId
from validi_fi_bank_login_python_sdk.apis.paths.v4_connect_session import V4CONNECTSession
from validi_fi_bank_login_python_sdk.apis.paths.v4_connect_banks import V4CONNECTBanks
from validi_fi_bank_login_python_sdk.apis.paths.v4_accounts_account_token_export import V4AccountsAccountTokenExport
from validi_fi_bank_login_python_sdk.apis.paths.v4_affordai import V4Affordai

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V4_TOKEN: V4Token,
        PathValues.V4_HEALTH_CHECK: V4HealthCheck,
        PathValues.V4_INSIGHTS: V4Insights,
        PathValues.V4_INSIGHTS_2_INQUIRY_ID: V4Insights2InquiryId,
        PathValues.V4_CONNECT_SESSION: V4CONNECTSession,
        PathValues.V4_CONNECT_BANKS: V4CONNECTBanks,
        PathValues.V4_ACCOUNTS_ACCOUNT_TOKEN_EXPORT: V4AccountsAccountTokenExport,
        PathValues.V4_AFFORDAI: V4Affordai,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V4_TOKEN: V4Token,
        PathValues.V4_HEALTH_CHECK: V4HealthCheck,
        PathValues.V4_INSIGHTS: V4Insights,
        PathValues.V4_INSIGHTS_2_INQUIRY_ID: V4Insights2InquiryId,
        PathValues.V4_CONNECT_SESSION: V4CONNECTSession,
        PathValues.V4_CONNECT_BANKS: V4CONNECTBanks,
        PathValues.V4_ACCOUNTS_ACCOUNT_TOKEN_EXPORT: V4AccountsAccountTokenExport,
        PathValues.V4_AFFORDAI: V4Affordai,
    }
)
