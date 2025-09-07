from datetime import datetime
from storage_provider import StorageProvider
from video_file import VideoFile
from storable_media_file import StorableMediaFile


class StorableVideoFile(StorableMediaFile, VideoFile):
    """Видео файл с поддержкой различных хранилищ"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 storage_provider: StorageProvider, file_path: str = None,
                 duration: int = 0, resolution: str = "", fps: int = 0):
        StorableMediaFile.__init__(self, name, size, created_at, owner, storage_provider, file_path)
        self.duration = duration
        self.resolution = resolution
        self.fps = fps
        