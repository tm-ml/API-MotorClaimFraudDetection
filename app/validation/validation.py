'''Module with validation classes.'''
# import json

from pydantic import BaseModel, ValidationError
from typing import Optional


# def validate_input(*, input_data: json):
#     relevant_data = input_data.copy()
#     errors = None
#
#     try:
#         validated_data = InputSchema(**relevant_data[0])
#         print("Validation succeed!")
#         print(validated_data)
#     except ValidationError as error:
#         print("Validation bugs:")
#         errors = error.json()
#     return relevant_data, errors


class InputSchema(BaseModel):
    """input schema for validating a single input record"""
    Month: Optional[str]
    WeekOfMonth: Optional[int]
    DayOfWeek: Optional[str]
    Make: Optional[str]
    AccidentArea: Optional[str]
    DayOfWeekClaimed: Optional[str]
    MonthClaimed: Optional[str]
    WeekOfMonthClaimed: Optional[int]
    Sex: Optional[str]
    MaritalStatus: Optional[str]
    Age: Optional[int]
    Fault: Optional[str]
    PolicyType: Optional[str]
    VehicleCategory: Optional[str]
    VehiclePrice: Optional[str]
    PolicyNumber: Optional[int]
    RepNumber: Optional[int]
    Deductible: Optional[int]
    DriverRating: Optional[int]
    Days_Policy_Accident: Optional[str]
    Days_Policy_Claim: Optional[str]
    PastNumberOfClaims: Optional[str]
    AgeOfVehicle: Optional[str]
    AgeOfPolicyHolder: Optional[str]
    PoliceReportFiled: Optional[str]
    WitnessPresent: Optional[str]
    AgentType: Optional[str]
    NumberOfSuppliments: Optional[str]
    AddressChange_Claim: Optional[str]
    NumberOfCars: Optional[str]
    Year: Optional[int]
    BasePolicy: Optional[str]


class PredictionOut(BaseModel):
    """Schema of result of predict function"""
    Result: int