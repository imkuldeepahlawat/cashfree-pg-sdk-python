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


from typing import List, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

class CartItem(BaseModel):
    """
    Each item in the cart.
    """
    item_id: Optional[StrictStr] = Field(None, description="Unique identifier of the item")
    item_name: Optional[StrictStr] = Field(None, description="Name of the item")
    item_description: Optional[StrictStr] = Field(None, description="Description of the item")
    item_tags: Optional[Annotated[List[StrictStr], Field()]] = Field(None, description="Tags attached to that item")
    item_details_url: Optional[StrictStr] = Field(None, description="Item details url")
    item_image_url: Optional[StrictStr] = Field(None, description="Item image url")
    item_original_unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Original price")
    item_discounted_unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Discounted Price")
    item_currency: Optional[StrictStr] = Field(None, description="Currency of the item.")
    item_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Quantity if that item")
    __properties = ["item_id", "item_name", "item_description", "item_tags", "item_details_url", "item_image_url", "item_original_unit_price", "item_discounted_unit_price", "item_currency", "item_quantity"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CartItem:
        """Create an instance of CartItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CartItem:
        """Create an instance of CartItem from a JSON string"""
        temp_dict = json.loads(json_str)
        if "item_id, item_name, item_description, item_tags, item_details_url, item_image_url, item_original_unit_price, item_discounted_unit_price, item_currency, item_quantity" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> CartItem:
        """Create an instance of CartItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CartItem.parse_obj(obj)

        _obj = CartItem.parse_obj({
            "item_id": obj.get("item_id"),
            "item_name": obj.get("item_name"),
            "item_description": obj.get("item_description"),
            "item_tags": obj.get("item_tags"),
            "item_details_url": obj.get("item_details_url"),
            "item_image_url": obj.get("item_image_url"),
            "item_original_unit_price": obj.get("item_original_unit_price"),
            "item_discounted_unit_price": obj.get("item_discounted_unit_price"),
            "item_currency": obj.get("item_currency"),
            "item_quantity": obj.get("item_quantity")
        })
        return _obj


