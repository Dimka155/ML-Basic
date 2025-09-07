from abc import ABC
from datetime import datetime
from typing import Optional, BinaryIO
from media_file import MediaFile
from storage_provider import StorageProvider


class StorableMediaFile(MediaFile, ABC):
    """Расширение MediaFile для работы с различными хранилищами"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 storage_provider: StorageProvider, file_path: str = None):
        super().__init__(name, size, created_at, owner)
        self.storage_provider = storage_provider
        self.file_path = file_path or name

    def save(self, data: BinaryIO = None) -> bool:
        """Сохраняет файл в хранилище"""
        return self.storage_provider.save(self.file_path, data)

    def load(self) -> Optional[BinaryIO]:
        """Загружает файл из хранилища"""
        return self.storage_provider.load(self.file_path)

    def delete(self) -> bool:
        """Удаляет файл из хранилища"""
        return self.storage_provider.delete(self.file_path)

    def exists(self) -> bool:
        """Проверяет существование файла в хранилище"""
        return self.storage_provider.exists(self.file_path)
