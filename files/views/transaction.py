from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

from files.services import TransactionService


@api_view(['GET'])
def detail_transaction(request: Request, transaction_id: str):
    data = TransactionService.get_detail_transaction(transaction_id=transaction_id)

    return Response(data=data, status=HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_transactions(request: Request):
    service = TransactionService()
    data = service.get_transactions(params=request.query_params)

    return Response(data=data, status=HTTP_202_ACCEPTED)
