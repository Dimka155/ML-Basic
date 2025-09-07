from typing import Optional, BinaryIO
from base_remote_storage_provider import BaseRemoteStorageProvider


class RemoteServerStorageProvider(BaseRemoteStorageProvider):
    """Провайдер для работы с удаленным сервером по SSH/SFTP"""

    def __init__(self, host: str, username: str, password: str = None, key_path: str = None):
        super().__init__(f"remote server ({host})")
        self.host = host
        self.username = username
        self.password = password
        self.key_path = key_path

    def _save_implementation(self, file_path: str, data: BinaryIO) -> bool:
        """Реализация сохранения на удаленный сервер"""
        # Здесь будет специфичная для удаленного сервера логика
        return True

    def _load_implementation(self, file_path: str) -> Optional[BinaryIO]:
        """Реализация загрузки с удаленного сервера"""
        # Здесь будет специфичная для удаленного сервера логика
        return None

    def _delete_implementation(self, file_path: str) -> bool:
        """Реализация удаления с удаленного сервера"""
        # Здесь будет специфичная для удаленного сервера логика
        return True

    def _exists_implementation(self, file_path: str) -> bool:
        """Реализация проверки существования на удаленном сервере"""
        # Здесь будет специфичная для удаленного сервера логика
        return True
