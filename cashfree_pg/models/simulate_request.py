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



from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr
from cashfree_pg.models.entity_simulation_request import EntitySimulationRequest

class SimulateRequest(BaseModel):
    """
    simulate payment request object
    """
    entity: StrictStr = Field(..., description="Entity type should be PAYMENTS or SUBS_PAYMENTS only.")
    entity_id: StrictStr = Field(..., description="If the entity type is PAYMENTS, the entity_id will be the transactionId. If the entity type is SUBS_PAYMENTS, the entity_id will be the merchantTxnId")
    entity_simulation: EntitySimulationRequest = Field(...)
    __properties = ["entity", "entity_id", "entity_simulation"]

    @field_validator('entity')
    @classmethod
    def entity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PAYMENTS', 'SUBS_PAYMENTS'):
            raise ValueError("must be one of enum values ('PAYMENTS', 'SUBS_PAYMENTS')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SimulateRequest:
        """Create an instance of SimulateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> SimulateRequest:
        """Create an instance of SimulateRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "entity, entity_id, entity_simulation" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entity_simulation
        if self.entity_simulation:
            _dict['entity_simulation'] = self.entity_simulation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SimulateRequest:
        """Create an instance of SimulateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SimulateRequest.parse_obj(obj)

        _obj = SimulateRequest.parse_obj({
            "entity": obj.get("entity"),
            "entity_id": obj.get("entity_id"),
            "entity_simulation": EntitySimulationRequest.from_dict(obj.get("entity_simulation")) if obj.get("entity_simulation") is not None else None
        })
        return _obj


