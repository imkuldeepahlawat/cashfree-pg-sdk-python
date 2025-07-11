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
from pydantic import ConfigDict, BaseModel, StrictInt, StrictStr

class UploadTerminalDocsEntity(BaseModel):
    """
    Upload the terminal documents.
    """
    cf_terminal_id: Optional[StrictInt] = None
    doc_type: Optional[StrictStr] = None
    doc_value: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties = ["cf_terminal_id", "doc_type", "doc_value", "status"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UploadTerminalDocsEntity:
        """Create an instance of UploadTerminalDocsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UploadTerminalDocsEntity:
        """Create an instance of UploadTerminalDocsEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cf_terminal_id, doc_type, doc_value, status" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> UploadTerminalDocsEntity:
        """Create an instance of UploadTerminalDocsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UploadTerminalDocsEntity.parse_obj(obj)

        _obj = UploadTerminalDocsEntity.parse_obj({
            "cf_terminal_id": obj.get("cf_terminal_id"),
            "doc_type": obj.get("doc_type"),
            "doc_value": obj.get("doc_value"),
            "status": obj.get("status")
        })
        return _obj


