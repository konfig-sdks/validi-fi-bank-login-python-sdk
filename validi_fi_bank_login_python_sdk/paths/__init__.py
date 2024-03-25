# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from validi_fi_bank_login_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V4_TOKEN = "/v4/token"
    V4_HEALTH_CHECK = "/v4/HealthCheck"
    V4_INSIGHTS = "/v4/Insights"
    V4_INSIGHTS_2_INQUIRY_ID = "/v4/Insights/2/{inquiryId}"
    V4_CONNECT_SESSION = "/v4/CONNECT/Session"
    V4_CONNECT_BANKS = "/v4/CONNECT/Banks"
    V4_ACCOUNTS_ACCOUNT_TOKEN_EXPORT = "/v4/accounts/{accountToken}/export"
    V4_AFFORDAI = "/v4/affordai"
