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


from typing import Optional, Union
from pydantic import ConfigDict, BaseModel, StrictFloat, StrictInt, StrictStr

class SettlementEntity(BaseModel):
    """
    Settlement entity object
    """
    cf_payment_id: Optional[StrictStr] = None
    cf_settlement_id: Optional[StrictStr] = None
    settlement_currency: Optional[StrictStr] = None
    order_id: Optional[StrictStr] = None
    entity: Optional[StrictStr] = None
    order_amount: Optional[Union[StrictFloat, StrictInt]] = None
    payment_time: Optional[StrictStr] = None
    service_charge: Optional[Union[StrictFloat, StrictInt]] = None
    service_tax: Optional[Union[StrictFloat, StrictInt]] = None
    settlement_amount: Optional[Union[StrictFloat, StrictInt]] = None
    settlement_id: Optional[StrictInt] = None
    transfer_id: Optional[StrictInt] = None
    transfer_time: Optional[StrictStr] = None
    transfer_utr: Optional[StrictStr] = None
    __properties = ["cf_payment_id", "cf_settlement_id", "settlement_currency", "order_id", "entity", "order_amount", "payment_time", "service_charge", "service_tax", "settlement_amount", "settlement_id", "transfer_id", "transfer_time", "transfer_utr"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SettlementEntity:
        """Create an instance of SettlementEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> SettlementEntity:
        """Create an instance of SettlementEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cf_payment_id, cf_settlement_id, settlement_currency, order_id, entity, order_amount, payment_time, service_charge, service_tax, settlement_amount, settlement_id, transfer_id, transfer_time, transfer_utr" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> SettlementEntity:
        """Create an instance of SettlementEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettlementEntity.parse_obj(obj)

        _obj = SettlementEntity.parse_obj({
            "cf_payment_id": obj.get("cf_payment_id"),
            "cf_settlement_id": obj.get("cf_settlement_id"),
            "settlement_currency": obj.get("settlement_currency"),
            "order_id": obj.get("order_id"),
            "entity": obj.get("entity"),
            "order_amount": obj.get("order_amount"),
            "payment_time": obj.get("payment_time"),
            "service_charge": obj.get("service_charge"),
            "service_tax": obj.get("service_tax"),
            "settlement_amount": obj.get("settlement_amount"),
            "settlement_id": obj.get("settlement_id"),
            "transfer_id": obj.get("transfer_id"),
            "transfer_time": obj.get("transfer_time"),
            "transfer_utr": obj.get("transfer_utr")
        })
        return _obj


