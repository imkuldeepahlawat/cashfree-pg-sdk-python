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

from datetime import datetime
from typing import Dict, List, Optional, Union
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cashfree_pg.models.order_meta import OrderMeta
from cashfree_pg.models.payment_link_customer_details import PaymentLinkCustomerDetails
from cashfree_pg.models.vendor_split import VendorSplit
from typing_extensions import Annotated

class PaymentLinkOrderEntity(BaseModel):
    """
    The complete order entity
    """
    cf_order_id: Optional[StrictStr] = Field(None, description="unique id generated by cashfree for your order")
    link_id: Optional[StrictStr] = Field(None, description="link id of the order")
    order_id: Optional[StrictStr] = Field(None, description="order_id sent during the api request")
    entity: Optional[StrictStr] = Field(None, description="Type of the entity.")
    order_currency: Optional[StrictStr] = Field(None, description="Currency of the order. Example INR")
    order_amount: Optional[Union[StrictFloat, StrictInt]] = None
    order_status: Optional[StrictStr] = Field(None, description="Possible values are  - `ACTIVE`: Order does not have a sucessful transaction yet - `PAID`: Order is PAID with one successful transaction - `EXPIRED`: Order was not PAID and not it has expired. No transaction can be initiated for an EXPIRED order. ")
    payment_session_id: Optional[StrictStr] = None
    order_expiry_time: Optional[datetime] = None
    order_note: Optional[StrictStr] = Field(None, description="Additional note for order")
    created_at: Optional[datetime] = Field(None, description="When the order was created at cashfree's server")
    order_splits: Optional[Annotated[List[VendorSplit], Field()]] = None
    customer_details: Optional[PaymentLinkCustomerDetails] = None
    order_meta: Optional[OrderMeta] = None
    order_tags: Optional[Dict[str, Annotated[str, StringConstraints(strict=True, max_length=255, min_length=1)]]] = Field(None, description="Custom Tags in thr form of {\"key\":\"value\"} which can be passed for an order. A maximum of 10 tags can be added")
    __properties = ["cf_order_id", "link_id", "order_id", "entity", "order_currency", "order_amount", "order_status", "payment_session_id", "order_expiry_time", "order_note", "created_at", "order_splits", "customer_details", "order_meta", "order_tags"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PaymentLinkOrderEntity:
        """Create an instance of PaymentLinkOrderEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentLinkOrderEntity:
        """Create an instance of PaymentLinkOrderEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cf_order_id, link_id, order_id, entity, order_currency, order_amount, order_status, payment_session_id, order_expiry_time, order_note, created_at, order_splits, customer_details, order_meta, order_tags" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in order_splits (list)
        _items = []
        if self.order_splits:
            for _item in self.order_splits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['order_splits'] = _items
        # override the default output from pydantic by calling `to_dict()` of customer_details
        if self.customer_details:
            _dict['customer_details'] = self.customer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_meta
        if self.order_meta:
            _dict['order_meta'] = self.order_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentLinkOrderEntity:
        """Create an instance of PaymentLinkOrderEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentLinkOrderEntity.parse_obj(obj)

        _obj = PaymentLinkOrderEntity.parse_obj({
            "cf_order_id": obj.get("cf_order_id"),
            "link_id": obj.get("link_id"),
            "order_id": obj.get("order_id"),
            "entity": obj.get("entity"),
            "order_currency": obj.get("order_currency"),
            "order_amount": obj.get("order_amount"),
            "order_status": obj.get("order_status"),
            "payment_session_id": obj.get("payment_session_id"),
            "order_expiry_time": obj.get("order_expiry_time"),
            "order_note": obj.get("order_note"),
            "created_at": obj.get("created_at"),
            "order_splits": [VendorSplit.from_dict(_item) for _item in obj.get("order_splits")] if obj.get("order_splits") is not None else None,
            "customer_details": PaymentLinkCustomerDetails.from_dict(obj.get("customer_details")) if obj.get("customer_details") is not None else None,
            "order_meta": OrderMeta.from_dict(obj.get("order_meta")) if obj.get("order_meta") is not None else None,
            "order_tags": obj.get("order_tags")
        })
        return _obj


