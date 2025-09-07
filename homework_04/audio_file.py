from datetime import datetime
from typing import Dict, Any
from media_file import MediaFile


class AudioFile(MediaFile):
    """Класс для работы с аудио файлами"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 duration: int = 0, bitrate: int = 0, artist: str = "", album: str = ""):
        super().__init__(name, size, created_at, owner)
        self.duration = duration  # длительность в секундах
        self.bitrate = bitrate  # битрейт в кбит/с
        self.artist = artist  # исполнитель
        self.album = album  # альбом

    def get_type(self) -> str:
        return "Audio"

    def extract_metadata(self) -> Dict[str, Any]:
        """Извлекает метаданные из аудио файла"""
        # Здесь была бы реальная логика извлечения метаданных из аудио файла
        self.metadata = {
            "duration": self.duration,
            "bitrate": self.bitrate,
            "artist": self.artist,
            "album": self.album
        }
        return self.metadata

    def convert_format(self, target_format: str) -> bool:
        """Конвертирует аудио файл в другой формат"""
        # Реализация конвертации формата
        print(f"Converting {self.name} to {target_format}")
        return True
