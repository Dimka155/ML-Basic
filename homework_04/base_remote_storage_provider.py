from typing import Optional, BinaryIO
from storage_provider import StorageProvider


class BaseRemoteStorageProvider(StorageProvider):
    """Базовый класс для провайдеров удаленного хранилища"""

    def __init__(self, storage_name: str):
        self.storage_name = storage_name

    def save(self, file_path: str, data: BinaryIO) -> bool:
        """Сохраняет файл в удаленное хранилище"""
        print(f"Saving file to {self.storage_name}: {file_path}")
        return self._save_implementation(file_path, data)

    def load(self, file_path: str) -> Optional[BinaryIO]:
        """Загружает файл из удаленного хранилища"""
        print(f"Loading file from {self.storage_name}: {file_path}")
        return self._load_implementation(file_path)

    def delete(self, file_path: str) -> bool:
        """Удаляет файл из удаленного хранилища"""
        print(f"Deleting file from {self.storage_name}: {file_path}")
        return self._delete_implementation(file_path)

    def exists(self, file_path: str) -> bool:
        """Проверяет существование файла в удаленном хранилище"""
        print(f"Checking if file exists in {self.storage_name}: {file_path}")
        return self._exists_implementation(file_path)

    def _save_implementation(self, file_path: str, data: BinaryIO) -> bool:
        """Реализация сохранения файла"""
        # Должна быть переопределена в подклассах
        return True

    def _load_implementation(self, file_path: str) -> Optional[BinaryIO]:
        """Реализация загрузки файла"""
        # Должна быть переопределена в подклассах
        return None

    def _delete_implementation(self, file_path: str) -> bool:
        """Реализация удаления файла"""
        # Должна быть переопределена в подклассах
        return True

    def _exists_implementation(self, file_path: str) -> bool:
        """Реализация проверки существования файла"""
        # Должна быть переопределена в подклассах
        return True
