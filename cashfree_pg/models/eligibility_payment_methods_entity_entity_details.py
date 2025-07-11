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


from typing import List, Optional
from pydantic import Field, ConfigDict, BaseModel
from cashfree_pg.models.payment_mode_details import PaymentModeDetails
from typing_extensions import Annotated

class EligibilityPaymentMethodsEntityEntityDetails(BaseModel):
    """
    EligibilityPaymentMethodsEntityEntityDetails
    """
    payment_method_details: Optional[Annotated[List[PaymentModeDetails], Field()]] = None
    __properties = ["payment_method_details"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EligibilityPaymentMethodsEntityEntityDetails:
        """Create an instance of EligibilityPaymentMethodsEntityEntityDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> EligibilityPaymentMethodsEntityEntityDetails:
        """Create an instance of EligibilityPaymentMethodsEntityEntityDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "payment_method_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in payment_method_details (list)
        _items = []
        if self.payment_method_details:
            for _item in self.payment_method_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payment_method_details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EligibilityPaymentMethodsEntityEntityDetails:
        """Create an instance of EligibilityPaymentMethodsEntityEntityDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EligibilityPaymentMethodsEntityEntityDetails.parse_obj(obj)

        _obj = EligibilityPaymentMethodsEntityEntityDetails.parse_obj({
            "payment_method_details": [PaymentModeDetails.from_dict(_item) for _item in obj.get("payment_method_details")] if obj.get("payment_method_details") is not None else None
        })
        return _obj


