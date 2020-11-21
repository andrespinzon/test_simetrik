from typing import Dict, Set

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST


def validate_allowed_fields(data: Dict, allowed_fields: Set) -> None:
    for key in data:
        if key not in allowed_fields:
            raise APIException(detail=f'The key {key} is not allowed', code=HTTP_400_BAD_REQUEST)


def validate_required_fields(data: Dict, required_fields: Set) -> None:
    for field in required_fields:
        if field not in data:
            raise APIException(detail=f'The field {field} is required', code=HTTP_400_BAD_REQUEST)


def validate_allowed_type_files(data: Dict, field: str, type_files: Set):
    file_extension = str(data[field]).split('.')[1]
    if file_extension not in type_files:
        raise APIException(detail=f'The file type {file_extension} is not allowed', code=HTTP_400_BAD_REQUEST)


def validate_allowed_fields_filters(field: str, allowed_field_order: Set):
    if field not in allowed_field_order:
        raise APIException(detail=f'The field {field} is not allowed for order_by', code=HTTP_400_BAD_REQUEST)
