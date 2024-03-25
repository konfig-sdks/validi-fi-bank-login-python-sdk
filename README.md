<div align="left">

[![Visit Validifi](./header.png)](https://validifi.com&#x2F;)

# Validifi<a id="validifi"></a>

ValidiFI, an analytics and technology company, connects bank account and payment insights to help companies in a variety of industries provide more confident, trustworthy and transparent transactions. Our differentiated data, sourced directly from banks, payment processors, and financial platforms helps companies to ensure compliance, mitigate risk, combat fraud, and confidently validate bank account and ownership. For more information, visit ValidiFI.com.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`validifibanklogin.connect.bank_lookup`](#validifibankloginconnectbank_lookup)
  * [`validifibanklogin.connect.create_session`](#validifibankloginconnectcreate_session)
  * [`validifibanklogin.connect.get_full_account_info`](#validifibankloginconnectget_full_account_info)
  * [`validifibanklogin.insights.get_insight_by_id`](#validifibanklogininsightsget_insight_by_id)
  * [`validifibanklogin.insights.submit_loan_application`](#validifibanklogininsightssubmit_loan_application)
  * [`validifibanklogin.reports.submit_afford_ai`](#validifibankloginreportssubmit_afford_ai)
  * [`validifibanklogin.token.check_health`](#validifibanklogintokencheck_health)
  * [`validifibanklogin.token.create`](#validifibanklogintokencreate)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ValidiFI&serviceName=BankLogin&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from validi_fi_bank_login_python_sdk import ValidiFiBankLogin, ApiException

validifibanklogin = ValidiFiBankLogin()

try:
    # Bank Lookup
    validifibanklogin.connect.bank_lookup(
        search="{{routingNumber}}",
    )
except ApiException as e:
    print("Exception when calling CONNECTApi.bank_lookup: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from validi_fi_bank_login_python_sdk import ValidiFiBankLogin, ApiException

validifibanklogin = ValidiFiBankLogin()


async def main():
    try:
        # Bank Lookup
        await validifibanklogin.connect.abank_lookup(
            search="{{routingNumber}}",
        )
    except ApiException as e:
        print("Exception when calling CONNECTApi.bank_lookup: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from validi_fi_bank_login_python_sdk import ValidiFiBankLogin, ApiException

validifibanklogin = ValidiFiBankLogin()

try:
    # Bank Lookup
    bank_lookup_response = validifibanklogin.connect.raw.bank_lookup(
        search="{{routingNumber}}",
    )
    pprint(bank_lookup_response.headers)
    pprint(bank_lookup_response.status)
    pprint(bank_lookup_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CONNECTApi.bank_lookup: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `validifibanklogin.connect.bank_lookup`<a id="validifibankloginconnectbank_lookup"></a>

Bank Lookup

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.connect.bank_lookup(
    search="{{routingNumber}}",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/CONNECT/Banks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.connect.create_session`<a id="validifibankloginconnectcreate_session"></a>

CONNECT Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.connect.create_session(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/CONNECT/Session` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.connect.get_full_account_info`<a id="validifibankloginconnectget_full_account_info"></a>

Get Full Account Info from CONNECT Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.connect.get_full_account_info(
    account_token="accountToken_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_token: `str`<a id="account_token-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/accounts/{accountToken}/export` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.insights.get_insight_by_id`<a id="validifibanklogininsightsget_insight_by_id"></a>

Get Insights

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.insights.get_insight_by_id(
    body=None,
    inquiry_id="inquiryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inquiry_id: `str`<a id="inquiry_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/Insights/2/{inquiryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.insights.submit_loan_application`<a id="validifibanklogininsightssubmit_loan_application"></a>

BankQUALIFY

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.insights.submit_loan_application(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/Insights` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.reports.submit_afford_ai`<a id="validifibankloginreportssubmit_afford_ai"></a>

AffordAi

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.reports.submit_afford_ai(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/affordai` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.token.check_health`<a id="validifibanklogintokencheck_health"></a>

Health Check

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.token.check_health(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/HealthCheck` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `validifibanklogin.token.create`<a id="validifibanklogintokencreate"></a>

OAuth 2.0 Token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validifibanklogin.token.create(
    client_id="{{clientId}}",
    client_secret="{{clientSecret}}",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenCreateRequest`](./validi_fi_bank_login_python_sdk/type/token_create_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v4/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
