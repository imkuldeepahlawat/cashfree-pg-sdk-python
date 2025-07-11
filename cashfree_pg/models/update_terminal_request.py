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
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from cashfree_pg.models.update_terminal_request_terminal_meta import UpdateTerminalRequestTerminalMeta
from typing_extensions import Annotated

class UpdateTerminalRequest(BaseModel):
    """
    Request body to update terminal details.
    """
    terminal_email: Optional[StrictStr] = Field(None, description="Mention the updated email ID of the terminal.")
    terminal_phone_no: Optional[Annotated[str, StringConstraints(strict=True, max_length=10, min_length=10)]] = Field(None, description="Terminal phone number to be updated.")
    terminal_meta: Optional[UpdateTerminalRequestTerminalMeta] = None
    terminal_type: StrictStr = Field(..., description="Mention the terminal type to be updated. Possible values - AGENT, STOREFRONT.")
    __properties = ["terminal_email", "terminal_phone_no", "terminal_meta", "terminal_type"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateTerminalRequest:
        """Create an instance of UpdateTerminalRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UpdateTerminalRequest:
        """Create an instance of UpdateTerminalRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "terminal_email, terminal_phone_no, terminal_meta, terminal_type" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of terminal_meta
        if self.terminal_meta:
            _dict['terminal_meta'] = self.terminal_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateTerminalRequest:
        """Create an instance of UpdateTerminalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateTerminalRequest.parse_obj(obj)

        _obj = UpdateTerminalRequest.parse_obj({
            "terminal_email": obj.get("terminal_email"),
            "terminal_phone_no": obj.get("terminal_phone_no"),
            "terminal_meta": UpdateTerminalRequestTerminalMeta.from_dict(obj.get("terminal_meta")) if obj.get("terminal_meta") is not None else None,
            "terminal_type": obj.get("terminal_type")
        })
        return _obj


