from datetime import datetime
from storage_provider import StorageProvider
from image_file import ImageFile
from storable_media_file import StorableMediaFile


class StorableImageFile(StorableMediaFile, ImageFile):
    """Изображение с поддержкой различных хранилищ"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 storage_provider: StorageProvider, file_path: str = None,
                 width: int = 0, height: int = 0, color_space: str = "RGB"):
        StorableMediaFile.__init__(self, name, size, created_at, owner, storage_provider, file_path)
        self.width = width
        self.height = height
        self.color_space = color_space
