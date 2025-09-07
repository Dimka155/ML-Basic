from datetime import datetime
from storage_provider import StorageProvider
from audio_file import AudioFile
from storable_media_file import StorableMediaFile


class StorableAudioFile(StorableMediaFile, AudioFile):
    """Аудио файл с поддержкой различных хранилищ"""

    def __init__(self, name: str, size: int, created_at: datetime, owner: str,
                 storage_provider: StorageProvider, file_path: str = None,
                 duration: int = 0, bitrate: int = 0, artist: str = "", album: str = ""):
        StorableMediaFile.__init__(self, name, size, created_at, owner, storage_provider, file_path)
        self.duration = duration
        self.bitrate = bitrate
        self.artist = artist
        self.album = album
