from typing import Dict, Optional, List

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from files.managers import TransactionManager
from files.serializers import TransactionSerializer
from common.validations import validate_allowed_fields


class TransactionService:
    __data: Dict

    @staticmethod
    def get_detail_transaction(transaction_id: str) -> Dict:
        data = TransactionManager.get_by_transaction_id(transaction_id=transaction_id)
        if data:
            data = TransactionSerializer(instance=data, many=False).data
            return data
        else:
            raise APIException(
                detail=f'The transaction with id {transaction_id} is not found.',
                code=HTTP_400_BAD_REQUEST
            )

    def get_transactions(self, params: Dict) -> Optional[List]:
        self.__data = params
        validate_allowed_fields(
            data=self.__data,
            allowed_fields={
                'transaction_id',
                'transaction_date',
                'transaction_amount',
                'client_id',
                'client_name',
                'page',
                'per_page',
                'order_by'
            }
        )

        data = TransactionManager.get_all_by_params(params=self.__data)
        data = TransactionSerializer(instance=data, many=True).data
        return data
