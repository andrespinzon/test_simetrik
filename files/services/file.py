from typing import Dict
import pandas as pd


from django.db.transaction import atomic as atomic_transaction
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from common.validations import \
    validate_allowed_fields, \
    validate_allowed_fields_filters, \
    validate_allowed_type_files, \
    validate_required_fields

from common.external_apis import MinioAPI


class FileService:

    __data: Dict

    def upload_file(self, file: Dict) -> Dict:
        field = 'file'

        self.__data = file
        validate_required_fields(data=self.__data, required_fields={field})
        validate_allowed_fields(data=self.__data, allowed_fields={field})
        validate_allowed_type_files(data=self.__data, field=field, type_files={'csv'})

        print(self.__data)
        #try:

        service = MinioAPI()
        service.upload_object(
            file=self.__data['file']
        )






