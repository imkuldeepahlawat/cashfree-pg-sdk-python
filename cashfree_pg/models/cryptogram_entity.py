# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictStr

class CryptogramEntity(BaseModel):
    """
    Crytogram Card object
    """
    instrument_id: Optional[StrictStr] = Field(None, description="instrument_id of saved instrument")
    token_requestor_id: Optional[StrictStr] = Field(None, description="TRID issued by card networks")
    card_number: Optional[StrictStr] = Field(None, description="token pan number")
    card_expiry_mm: Optional[StrictStr] = Field(None, description="token pan expiry month")
    card_expiry_yy: Optional[StrictStr] = Field(None, description="token pan expiry year")
    cryptogram: Optional[StrictStr] = Field(None, description="cryptogram")
    card_display: Optional[StrictStr] = Field(None, description="last 4 digits of original card number")
    __properties = ["instrument_id", "token_requestor_id", "card_number", "card_expiry_mm", "card_expiry_yy", "cryptogram", "card_display"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CryptogramEntity:
        """Create an instance of CryptogramEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CryptogramEntity:
        """Create an instance of CryptogramEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "instrument_id, token_requestor_id, card_number, card_expiry_mm, card_expiry_yy, cryptogram, card_display" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CryptogramEntity:
        """Create an instance of CryptogramEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CryptogramEntity.parse_obj(obj)

        _obj = CryptogramEntity.parse_obj({
            "instrument_id": obj.get("instrument_id"),
            "token_requestor_id": obj.get("token_requestor_id"),
            "card_number": obj.get("card_number"),
            "card_expiry_mm": obj.get("card_expiry_mm"),
            "card_expiry_yy": obj.get("card_expiry_yy"),
            "cryptogram": obj.get("cryptogram"),
            "card_display": obj.get("card_display")
        })
        return _obj


