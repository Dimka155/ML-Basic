from datetime import datetime
from typing import Dict, Any
from media_file import MediaFile


class VideoFile(MediaFile):
    """Класс для работы с видео файлами"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 duration: int = 0, resolution: str = "", fps: int = 0):
        super().__init__(name, size, created_at, owner)
        self.duration = duration  # длительность в секундах
        self.resolution = resolution  # разрешение (например, "1920x1080")
        self.fps = fps  # частота кадров

    def get_type(self) -> str:
        return "Video"

    def extract_metadata(self) -> Dict[str, Any]:
        """Извлекает метаданные из видео файла"""
        # Здесь была бы реальная логика извлечения метаданных из видео файла
        self.metadata = {
            "duration": self.duration,
            "resolution": self.resolution,
            "fps": self.fps
        }
        return self.metadata

    def extract_frame(self, time_position: int) -> bool:
        """Извлекает кадр из видео в указанной временной позиции"""
        # Реализация извлечения кадра
        print(f"Extracting frame at {time_position}s from {self.name}")
        return True

    def compress(self, quality: int) -> bool:
        """Сжимает видео с указанным качеством"""
        # Реализация сжатия видео
        print(f"Compressing {self.name} with quality {quality}")
        return True
