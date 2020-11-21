from typing import Dict

from django.db.transaction import atomic as atomic_transaction
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

import pandas as pd

class FileService:

    __data: Dict

    def upload_file(self, file: Dict) -> Dict:
        self.__data = file
