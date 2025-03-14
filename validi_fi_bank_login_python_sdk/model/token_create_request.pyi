# coding: utf-8

"""
    RIBBIT API v4

    ValidiFI, an analytics and technology company, connects bank account and payment insights to help companies in a variety of industries provide more confident, trustworthy and transparent transactions. Our differentiated data, sourced directly from banks, payment processors, and financial platforms helps companies to ensure compliance, mitigate risk, combat fraud, and confidently validate bank account and ownership. For more information, visit ValidiFI.com.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from validi_fi_bank_login_python_sdk import schemas  # noqa: F401


class TokenCreateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            clientId = schemas.StrSchema
            clientSecret = schemas.StrSchema
            __annotations__ = {
                "clientId": clientId,
                "clientSecret": clientSecret,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clientId", "clientSecret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientSecret"]) -> typing.Union[MetaOapg.properties.clientSecret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clientId", "clientSecret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
        clientSecret: typing.Union[MetaOapg.properties.clientSecret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TokenCreateRequest':
        return super().__new__(
            cls,
            *args,
            clientId=clientId,
            clientSecret=clientSecret,
            _configuration=_configuration,
            **kwargs,
        )
