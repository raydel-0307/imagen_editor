# minio_model_stress_test.py
from minio import Minio
import io

class MinioManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MinioManager, cls).__new__(cls)
            cls._instance._initialized = False
            cls._instance.MINIO_ENDPOINT = "192.168.1.36:9000"
            cls._instance.MINIO_ACCESS_KEY = "minioadmin"
            cls._instance.MINIO_SECRET_KEY = "minioadmin"
            cls._instance.BUCKET_NAME = "models"
            
            cls._instance.client = Minio(
                cls._instance.MINIO_ENDPOINT,
                access_key=cls._instance.MINIO_ACCESS_KEY,
                secret_key=cls._instance.MINIO_SECRET_KEY,
                secure=False
            )
            cls._instance._initialized = True
        return cls._instance

    def __init__(self):
        pass

    def upload_model(self, model_name, model_serialized):
        """Sube un modelo a MinIO."""
        model_data = io.BytesIO(model_serialized)
        model_size = len(model_serialized)
        self.client.put_object(
            self.BUCKET_NAME, 
            model_name, 
            model_data, 
            model_size
        )

    def download_model(self, model_name):
        """Descarga un modelo de MinIO."""
        response = self.client.get_object(self.BUCKET_NAME, model_name)
        model_serialized = response.read()
        response.close()
        response.release_conn()
        return model_serialized

