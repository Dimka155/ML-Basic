from abc import ABC, abstractmethod
from typing import Optional, BinaryIO


class StorageProvider(ABC):
    """Абстрактный класс для провайдеров хранилища"""

    @abstractmethod
    def save(self, file_path: str, data: BinaryIO) -> bool:
        """Сохраняет файл в хранилище"""
        pass

    @abstractmethod
    def load(self, file_path: str) -> Optional[BinaryIO]:
        """Загружает файл из хранилища"""
        pass

    @abstractmethod
    def delete(self, file_path: str) -> bool:
        """Удаляет файл из хранилища"""
        pass

    @abstractmethod
    def exists(self, file_path: str) -> bool:
        """Проверяет существование файла в хранилище"""
        pass
