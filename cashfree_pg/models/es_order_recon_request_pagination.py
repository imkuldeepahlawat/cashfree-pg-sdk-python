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
from pydantic import ConfigDict, BaseModel, Field, StrictInt, StrictStr

class ESOrderReconRequestPagination(BaseModel):
    """
    Set limit based on your requirement. Pagination limit will fetch a set of orders, next set of orders can be generated using the cursor shared in previous response of the same API.
    """
    cursor: Optional[StrictStr] = None
    limit: Optional[StrictInt] = Field(None, description="Set the minimum/maximum limit for number of filtered data. Min value - 10, Max value - 100.")
    __properties = ["cursor", "limit"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ESOrderReconRequestPagination:
        """Create an instance of ESOrderReconRequestPagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> ESOrderReconRequestPagination:
        """Create an instance of ESOrderReconRequestPagination from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cursor, limit" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> ESOrderReconRequestPagination:
        """Create an instance of ESOrderReconRequestPagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ESOrderReconRequestPagination.parse_obj(obj)

        _obj = ESOrderReconRequestPagination.parse_obj({
            "cursor": obj.get("cursor"),
            "limit": obj.get("limit")
        })
        return _obj


