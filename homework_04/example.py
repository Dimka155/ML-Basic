from datetime import datetime

# Импорт классов медиа-файлов
from audio_file import AudioFile
# from video_file import VideoFile
# from image_file import ImageFile

# Импорт провайдеров хранилища
from local_storage_provider import LocalStorageProvider
from cloud_storage_provider import CloudStorageProvider
from remote_server_storage_provider import RemoteServerStorageProvider

# Импорт классов для работы с хранилищами
# from storable_audio_file import StorableAudioFile
from storable_video_file import StorableVideoFile
# from storable_image_file import StorableImageFile


# Пример использования обычных медиа-файлов
audio = AudioFile(
    name="song.mp3",
    size=5242880,
    created_at=datetime.now(),
    owner="user1",
    duration=240,
    bitrate=320,
    artist="Some Artist",
    album="Great Album"
)

metadata = audio.extract_metadata()
print(f"Audio metadata: {metadata}")
audio.convert_format("wav")

# Пример использования медиа-файлов с хранилищами
local_storage = LocalStorageProvider(base_path="/media/files")
cloud_storage = CloudStorageProvider(
    bucket_name="my-media-bucket",
    access_key="access_key_123",
    secret_key="secret_key_456"
)
remote_storage = RemoteServerStorageProvider(
    host="media-server.example.com",
    username="admin",
    password="secure_password"
)

cloud_video = StorableVideoFile(
    name="cloud_movie.mp4",
    size=1073741824,
    created_at=datetime.now(),
    owner="user2",
    storage_provider=cloud_storage,
    file_path="videos/movie.mp4",
    duration=7200,
    resolution="1920x1080"
)

cloud_video.save()
if cloud_video.exists():
    print("Video exists in cloud storage")
    cloud_video.extract_frame(3600)
