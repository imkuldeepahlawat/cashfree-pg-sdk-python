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
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr

class OrderAuthenticateEntity(BaseModel):
    """
    This is the response shared when merchant inovkes the OTP submit or resend API
    """
    cf_payment_id: Optional[StrictStr] = Field(None, description="The payment id for which this request was sent")
    action: Optional[StrictStr] = Field(None, description="The action that was invoked for this request.")
    authenticate_status: Optional[StrictStr] = Field(None, description="Status of the is action. Will be either failed or successful. If the action is successful, you should still call the authorization status to verify the final payment status.")
    payment_message: Optional[StrictStr] = Field(None, description="Human readable message which describes the status in more detail")
    __properties = ["cf_payment_id", "action", "authenticate_status", "payment_message"]

    @field_validator('action')
    @classmethod
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUBMIT_OTP', 'RESEND_OTP'):
            raise ValueError("must be one of enum values ('SUBMIT_OTP', 'RESEND_OTP')")
        return value

    @field_validator('authenticate_status')
    @classmethod
    def authenticate_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('FAILED', 'SUCCESS'):
            raise ValueError("must be one of enum values ('FAILED', 'SUCCESS')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OrderAuthenticateEntity:
        """Create an instance of OrderAuthenticateEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OrderAuthenticateEntity:
        """Create an instance of OrderAuthenticateEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cf_payment_id, action, authenticate_status, payment_message" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> OrderAuthenticateEntity:
        """Create an instance of OrderAuthenticateEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderAuthenticateEntity.parse_obj(obj)

        _obj = OrderAuthenticateEntity.parse_obj({
            "cf_payment_id": obj.get("cf_payment_id"),
            "action": obj.get("action"),
            "authenticate_status": obj.get("authenticate_status"),
            "payment_message": obj.get("payment_message")
        })
        return _obj


