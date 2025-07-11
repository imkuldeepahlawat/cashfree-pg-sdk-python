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
from pydantic import ConfigDict, BaseModel, StrictStr

class ErrorDetailsInPaymentsEntity(BaseModel):
    """
    The error details are present only for failed payments
    """
    error_code: Optional[StrictStr] = None
    error_description: Optional[StrictStr] = None
    error_reason: Optional[StrictStr] = None
    error_source: Optional[StrictStr] = None
    error_code_raw: Optional[StrictStr] = None
    error_description_raw: Optional[StrictStr] = None
    error_subcode_raw: Optional[StrictStr] = None
    __properties = ["error_code", "error_description", "error_reason", "error_source", "error_code_raw", "error_description_raw", "error_subcode_raw"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ErrorDetailsInPaymentsEntity:
        """Create an instance of ErrorDetailsInPaymentsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> ErrorDetailsInPaymentsEntity:
        """Create an instance of ErrorDetailsInPaymentsEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "error_code, error_description, error_reason, error_source, error_code_raw, error_description_raw, error_subcode_raw" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> ErrorDetailsInPaymentsEntity:
        """Create an instance of ErrorDetailsInPaymentsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorDetailsInPaymentsEntity.parse_obj(obj)

        _obj = ErrorDetailsInPaymentsEntity.parse_obj({
            "error_code": obj.get("error_code"),
            "error_description": obj.get("error_description"),
            "error_reason": obj.get("error_reason"),
            "error_source": obj.get("error_source"),
            "error_code_raw": obj.get("error_code_raw"),
            "error_description_raw": obj.get("error_description_raw"),
            "error_subcode_raw": obj.get("error_subcode_raw")
        })
        return _obj


