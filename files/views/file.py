from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED


@api_view(['POST'])
def upload_file_view(request: Request) -> Response:
    data={}
    return Response(data=data, status=HTTP_202_ACCEPTED)
