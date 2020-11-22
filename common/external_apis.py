from minio import Minio
from minio.error import ResponseError
import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


class MinioAPI:

    def __init__(self):
        self.miniClient = Minio(
            'localhost:9000',
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )

    def upload_object(self, file):
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
