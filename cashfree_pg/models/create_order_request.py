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


from typing import Dict, List, Optional, Union
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from cashfree_pg.models.cart_details import CartDetails
from cashfree_pg.models.customer_details import CustomerDetails
from cashfree_pg.models.order_meta import OrderMeta
from cashfree_pg.models.terminal_details import TerminalDetails
from cashfree_pg.models.vendor_split import VendorSplit
from typing_extensions import Annotated

class CreateOrderRequest(BaseModel):
    """
    Request body to create an order at cashfree
    """
    order_id: Optional[Annotated[str, StringConstraints(strict=True, max_length=45, min_length=3)]] = Field(None, description="Order identifier present in your system. Alphanumeric, '_' and '-' only")
    order_amount: Union[Annotated[float, Field(ge=1, strict=True)], Annotated[int, Field(ge=1, strict=True)]] = Field(..., description="Bill amount for the order. Provide upto two decimals. 10.15 means Rs 10 and 15 paisa")
    order_currency: StrictStr = Field(..., description="Currency for the order. INR if left empty. Contact care@cashfree.com to enable new currencies.")
    cart_details: Optional[CartDetails] = None
    customer_details: CustomerDetails = Field(...)
    terminal: Optional[TerminalDetails] = None
    order_meta: Optional[OrderMeta] = None
    order_expiry_time: Optional[StrictStr] = Field(None, description="Time after which the order expires. Customers will not be able to make the payment beyond the time specified here. We store timestamps in IST, but you can provide them in a valid ISO 8601 time format. Example 2021-07-02T10:20:12+05:30 for IST, 2021-07-02T10:20:12Z for UTC")
    order_note: Optional[Annotated[str, StringConstraints(strict=True, max_length=200, min_length=3)]] = Field(None, description="Order note for reference.")
    order_tags: Optional[Dict[str, Annotated[str, StringConstraints(strict=True, max_length=255, min_length=1)]]] = Field(None, description="Custom Tags in thr form of {\"key\":\"value\"} which can be passed for an order. A maximum of 10 tags can be added")
    order_splits: Optional[Annotated[List[VendorSplit], Field()]] = Field(None, description="If you have Easy split enabled in your Cashfree account then you can use this option to split the order amount.")
    __properties = ["order_id", "order_amount", "order_currency", "cart_details", "customer_details", "terminal", "order_meta", "order_expiry_time", "order_note", "order_tags", "order_splits"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateOrderRequest:
        """Create an instance of CreateOrderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateOrderRequest:
        """Create an instance of CreateOrderRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "order_id, order_amount, order_currency, cart_details, customer_details, terminal, order_meta, order_expiry_time, order_note, order_tags, order_splits" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cart_details
        if self.cart_details:
            _dict['cart_details'] = self.cart_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_details
        if self.customer_details:
            _dict['customer_details'] = self.customer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terminal
        if self.terminal:
            _dict['terminal'] = self.terminal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_meta
        if self.order_meta:
            _dict['order_meta'] = self.order_meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in order_splits (list)
        _items = []
        if self.order_splits:
            for _item in self.order_splits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['order_splits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateOrderRequest:
        """Create an instance of CreateOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateOrderRequest.parse_obj(obj)

        _obj = CreateOrderRequest.parse_obj({
            "order_id": obj.get("order_id"),
            "order_amount": obj.get("order_amount"),
            "order_currency": obj.get("order_currency"),
            "cart_details": CartDetails.from_dict(obj.get("cart_details")) if obj.get("cart_details") is not None else None,
            "customer_details": CustomerDetails.from_dict(obj.get("customer_details")) if obj.get("customer_details") is not None else None,
            "terminal": TerminalDetails.from_dict(obj.get("terminal")) if obj.get("terminal") is not None else None,
            "order_meta": OrderMeta.from_dict(obj.get("order_meta")) if obj.get("order_meta") is not None else None,
            "order_expiry_time": obj.get("order_expiry_time"),
            "order_note": obj.get("order_note"),
            "order_tags": obj.get("order_tags"),
            "order_splits": [VendorSplit.from_dict(_item) for _item in obj.get("order_splits")] if obj.get("order_splits") is not None else None
        })
        return _obj


