from typing import Dict

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

from files.services import FileService


@api_view(['POST'])
def upload_file_view(request: Request) -> Response:
    service: FileService = FileService()
    data: Dict = service.upload_file(file=request.FILES)

    return Response(data=data, status=HTTP_202_ACCEPTED)
