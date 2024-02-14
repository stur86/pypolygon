from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field


class Locale(Enum):
    US = "us"
    GLOBAL = "global"


class MarketType(Enum):
    STOCKS = "stocks"
    CRYPTO = "crypto"
    FX = "fx"
    OTC = "otc"
    INDICES = "indices"


class TickerInfo(BaseModel):
    active: Optional[bool] = Field(
        None,
        description="Whether or not the asset is actively traded. False means the asset has been delisted.",
    )
    cik: Optional[str] = Field(None, description="The CIK number for this ticker.")
    composite_figi: Optional[str] = Field(
        None, description="The composite OpenFIGI number for this ticker."
    )
    currency_name: Optional[str] = Field(
        None, description="The name of the currency that this asset is traded with."
    )
    delisted_utc: Optional[str] = Field(
        None, description="The last date that the asset was traded."
    )
    last_updated_utc: Optional[str] = Field(
        None, description="The information is accurate up to this time."
    )
    locale: Locale = Field(..., description="The locale of the asset.")
    market: MarketType = Field(..., description="The market type of the asset.")
    name: str = Field(
        ...,
        description="The name of the asset. For stocks/equities this will be the companies registered name. "
        "For crypto/fx this will be the name of the currency or coin pair.",
    )
    primary_exchange: Optional[str] = Field(
        None, description="The ISO code of the primary listing exchange for this asset."
    )
    share_class_figi: Optional[str] = Field(
        None, description="The share Class OpenFIGI number for this ticker."
    )
    ticker: str = Field(
        ..., description="The exchange symbol that this item is traded under."
    )
    type: Optional[str] = Field(None, description="The type of the asset.")


class TickersResponse(BaseModel):
    next_url: Optional[str] = Field(
        None, description="The URL to the next page of results."
    )
    status: str = Field(..., description="The status of the response.")
    count: int = Field(default=0, description="The number of results returned.")
    request_id: str = Field(..., description="The unique identifier for this request.")
    results: List[TickerInfo] = Field(..., description="The results of the request.")


"""
active*boolean

Whether or not the asset is actively traded. False means the asset has been delisted.
addressobject
address1string

The first line of the company's headquarters address.
citystring

The city of the company's headquarters address.
postal_codestring

The postal code of the company's headquarters address.
statestring

The state of the company's headquarters address.
brandingobject
icon_urlstring

A link to this ticker's company's icon. Icon's are generally smaller, square images that represent the company at a glance. Note that you must provide an API key when accessing this URL. See the "Authentication" section at the top of this page for more details.
logo_urlstring

A link to this ticker's company's logo. Note that you must provide an API key when accessing this URL. See the "Authentication" section at the top of this page for more details.
cikstring

The CIK number for this ticker. Find more information here.
composite_figistring

The composite OpenFIGI number for this ticker. Find more information here
currency_name*string

The name of the currency that this asset is traded with.
delisted_utcstring

The last date that the asset was traded.
descriptionstring

A description of the company and what they do/offer.
homepage_urlstring

The URL of the company's website homepage.
list_datestring

The date that the symbol was first publicly listed in the format YYYY-MM-DD.
locale*enum [us, global]

The locale of the asset.
market*enum [stocks, crypto, fx, otc, indices]

The market type of the asset.
market_capnumber

The most recent close price of the ticker multiplied by weighted outstanding shares.
name*string

The name of the asset. For stocks/equities this will be the companies registered name. For crypto/fx this will be the name of the currency or coin pair.
phone_numberstring

The phone number for the company behind this ticker.
primary_exchangestring

The ISO code of the primary listing exchange for this asset.
round_lotnumber

Round lot size of this security.
share_class_figistring

The share Class OpenFIGI number for this ticker. Find more information here
share_class_shares_outstandingnumber

The recorded number of outstanding shares for this particular share class.
sic_codestring

The standard industrial classification code for this ticker. For a list of SIC Codes, see the SEC's SIC Code List.
sic_descriptionstring

A description of this ticker's SIC code.
ticker*string

The exchange symbol that this item is traded under.
ticker_rootstring

The root of a specified ticker. For example, the root of BRK.A is BRK.
ticker_suffixstring

The suffix of a specified ticker. For example, the suffix of BRK.A is A.
total_employeesnumber

The approximate number of employees for the company.
typestring

The type of the asset. Find the types that we support via our Ticker Types API.
weighted_shares_outstandingnumber

The shares outstanding calculated assuming all shares of other share classes are converted to this share class.

"""
