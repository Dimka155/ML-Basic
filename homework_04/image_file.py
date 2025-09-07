from datetime import datetime
from typing import Dict, Any
from media_file import MediaFile


class ImageFile(MediaFile):
    """Класс для работы с изображениями"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 width: int = 0, height: int = 0, color_space: str = "RGB"):
        super().__init__(name, size, created_at, owner)
        self.width = width  # ширина в пикселях
        self.height = height  # высота в пикселях
        self.color_space = color_space  # цветовое пространство

    def get_type(self) -> str:
        return "Image"

    def extract_metadata(self) -> Dict[str, Any]:
        """Извлекает метаданные из изображения"""
        # Здесь была бы реальная логика извлечения метаданных из изображения
        self.metadata = {
            "width": self.width,
            "height": self.height,
            "color_space": self.color_space
        }
        return self.metadata

    def resize(self, new_width: int, new_height: int) -> bool:
        """Изменяет размер изображения"""
        # Реализация изменения размера
        print(f"Resizing {self.name} to {new_width}x{new_height}")
        self.width = new_width
        self.height = new_height
        return True

    def apply_filter(self, filter_name: str) -> bool:
        """Применяет фильтр к изображению"""
        # Реализация применения фильтра
        print(f"Applying filter '{filter_name}' to {self.name}")
        return True
