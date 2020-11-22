from typing import Dict

from config.extension import session
from files.models import File


class FileManager:

    @staticmethod
    def create(data: Dict):
        file: File = File(**data)
        session.add(file)
        session.commit()
