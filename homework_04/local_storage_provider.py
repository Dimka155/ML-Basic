from typing import Optional, BinaryIO
from storage_provider import StorageProvider


class LocalStorageProvider(StorageProvider):
    """Провайдер для работы с локальным хранилищем"""

    def __init__(self, base_path: str = "."):
        self.base_path = base_path

    def save(self, file_path: str, data: BinaryIO) -> bool:
        """Сохраняет файл в локальное хранилище"""
        # Реализация сохранения в локальное хранилище
        print(f"Saving file to local storage: {file_path}")
        return True

    def load(self, file_path: str) -> Optional[BinaryIO]:
        """Загружает файл из локального хранилища"""
        # Реализация загрузки из локального хранилища
        print(f"Loading file from local storage: {file_path}")
        return None  # Здесь должен быть реальный файловый объект

    def delete(self, file_path: str) -> bool:
        """Удаляет файл из локального хранилища"""
        # Реализация удаления из локального хранилища
        print(f"Deleting file from local storage: {file_path}")
        return True

    def exists(self, file_path: str) -> bool:
        """Проверяет существование файла в локальном хранилище"""
        # Реализация проверки существования в локальном хранилище
        print(f"Checking if file exists in local storage: {file_path}")
        return True
