# coding: utf-8

"""
    RIBBIT API v4

    ValidiFI, an analytics and technology company, connects bank account and payment insights to help companies in a variety of industries provide more confident, trustworthy and transparent transactions. Our differentiated data, sourced directly from banks, payment processors, and financial platforms helps companies to ensure compliance, mitigate risk, combat fraud, and confidently validate bank account and ownership. For more information, visit ValidiFI.com.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from validi_fi_bank_login_python_sdk.paths.v4_health_check.get import CheckHealth
from validi_fi_bank_login_python_sdk.paths.v4_token.post import Create
from validi_fi_bank_login_python_sdk.apis.tags.token_api_raw import TokenApiRaw


class TokenApi(
    CheckHealth,
    Create,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TokenApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TokenApiRaw(api_client)
