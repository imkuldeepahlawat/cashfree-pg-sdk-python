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

class AddressDetails(BaseModel):
    """
    Address associated with the customer.
    """
    name: Optional[StrictStr] = Field(None, description="Full Name of the customer associated with the address.")
    address_line_one: Optional[StrictStr] = Field(None, description="First line of the address.")
    address_line_two: Optional[StrictStr] = Field(None, description="Second line of the address.")
    country: Optional[StrictStr] = Field(None, description="Country Name.")
    country_code: Optional[StrictStr] = Field(None, description="Country Code.")
    state: Optional[StrictStr] = Field(None, description="State Name.")
    state_code: Optional[StrictStr] = Field(None, description="State Code.")
    city: Optional[StrictStr] = Field(None, description="City Name.")
    pin_code: Optional[StrictStr] = Field(None, description="Pin Code/Zip Code.")
    phone: Optional[StrictStr] = Field(None, description="Customer Phone Number.")
    email: Optional[StrictStr] = Field(None, description="Cutomer Email Address.")
    __properties = ["name", "address_line_one", "address_line_two", "country", "country_code", "state", "state_code", "city", "pin_code", "phone", "email"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AddressDetails:
        """Create an instance of AddressDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AddressDetails:
        """Create an instance of AddressDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "name, address_line_one, address_line_two, country, country_code, state, state_code, city, pin_code, phone, email" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> AddressDetails:
        """Create an instance of AddressDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressDetails.parse_obj(obj)

        _obj = AddressDetails.parse_obj({
            "name": obj.get("name"),
            "address_line_one": obj.get("address_line_one"),
            "address_line_two": obj.get("address_line_two"),
            "country": obj.get("country"),
            "country_code": obj.get("country_code"),
            "state": obj.get("state"),
            "state_code": obj.get("state_code"),
            "city": obj.get("city"),
            "pin_code": obj.get("pin_code"),
            "phone": obj.get("phone"),
            "email": obj.get("email")
        })
        return _obj


