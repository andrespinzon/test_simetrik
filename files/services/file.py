from typing import Dict
import pandas as pd
from datetime import date


from django.db.transaction import atomic as atomic_transaction
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST
from concurrent.futures import ThreadPoolExecutor

from config.extension import engine
from common.external_apis import MinioAPI
from common.validations import \
    validate_allowed_fields, \
    validate_allowed_type_files, \
    validate_required_fields
from files.managers import FileManager, TransactionManager
from files.models import Transaction
from files.serializers import TransactionSerializer


class FileService:

    __data: Dict

    def __read_file_and_store_data(self, file_path: str):
        pd_data = pd.read_csv(file_path)
        pd_data.to_sql(
            Transaction.__tablename__,
            con=engine,
            if_exists='append',
            index=False
        )

    def upload_file(self, file: Dict) -> Dict:
        field = 'file'

        self.__data = file
        validate_required_fields(data=self.__data, required_fields={field})
        validate_allowed_fields(data=self.__data, allowed_fields={field})
        validate_allowed_type_files(data=self.__data, field=field, type_files={'csv'})

        service = MinioAPI()
        file_path = service.upload_object(
            file=self.__data['file']
        )

        try:
            with atomic_transaction():
                file_data = {
                    'name': self.__data['file'].name,
                    'created_at': date.today()
                }
                FileManager.create(data=file_data)

                ex = ThreadPoolExecutor(max_workers=2)
                process = ex.submit(self.__read_file_and_store_data, file_path)
                process.result()

                transaction_data = TransactionManager.get_all()

                data = TransactionSerializer(
                    instance=transaction_data,
                    many=True
                ).data

                return data
        except:
            raise APIException(
                detail='The operation is invalid',
                code=HTTP_400_BAD_REQUEST
            )
