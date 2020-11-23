from minio import Minio
from minio.error import ResponseError
import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.exceptions import APIException


class MinioAPI:

    def __init__(self):
        self.miniClient = Minio(
            f'{settings.MINIO_HOST}:9000',
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )
        if not self.miniClient.bucket_exists(settings.MINIO_BUCKET):
            self.miniClient.make_bucket(settings.MINIO_BUCKET)

    def upload_object(self, file) -> str:

        try:
            path = default_storage.save(f'tmp/{file.name}', ContentFile(file.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            file_stat = os.stat(path)
            with open(tmp_file, 'rb') as data:
                self.miniClient.put_object(
                    bucket_name=settings.MINIO_BUCKET,
                    object_name=str(path[4:]),
                    data=data,
                    length=file_stat.st_size,
                    content_type='text/csv',
                )
            return tmp_file
        except Exception as error:
            raise APIException(detail=error)
