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
from pydantic import ConfigDict, BaseModel, Field
from cashfree_pg.models.payment_methods_filters import PaymentMethodsFilters
from cashfree_pg.models.payment_methods_queries import PaymentMethodsQueries

class EligibilityFetchPaymentMethodsRequest(BaseModel):
    """
    eligibilty request to find eligible payment method
    """
    queries: PaymentMethodsQueries = Field(...)
    filters: Optional[PaymentMethodsFilters] = None
    __properties = ["queries", "filters"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EligibilityFetchPaymentMethodsRequest:
        """Create an instance of EligibilityFetchPaymentMethodsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> EligibilityFetchPaymentMethodsRequest:
        """Create an instance of EligibilityFetchPaymentMethodsRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "queries, filters" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of queries
        if self.queries:
            _dict['queries'] = self.queries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EligibilityFetchPaymentMethodsRequest:
        """Create an instance of EligibilityFetchPaymentMethodsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EligibilityFetchPaymentMethodsRequest.parse_obj(obj)

        _obj = EligibilityFetchPaymentMethodsRequest.parse_obj({
            "queries": PaymentMethodsQueries.from_dict(obj.get("queries")) if obj.get("queries") is not None else None,
            "filters": PaymentMethodsFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        return _obj


