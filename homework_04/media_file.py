from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any


class MediaFile(ABC):
    """Абстрактный базовый класс для всех медиа-файлов"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner
        self.metadata = {}

    @abstractmethod
    def get_type(self) -> str:
        """Возвращает тип медиа-файла"""
        pass

    @abstractmethod
    def extract_metadata(self) -> Dict[str, Any]:
        """Извлекает метаданные из файла"""
        pass

    def save(self) -> bool:
        """Сохраняет файл"""
        # Реализация сохранения файла
        print(f"Saving {self.get_type()} file: {self.name}")
        return True

    def delete(self) -> bool:
        """Удаляет файл"""
        # Реализация удаления файла
        print(f"Deleting {self.get_type()} file: {self.name}")
        return True

    def update(self, **kwargs) -> bool:
        """Обновляет атрибуты файла"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return True

    def __str__(self) -> str:
        return f"{self.get_type()}: {self.name} ({self.size} bytes)"
