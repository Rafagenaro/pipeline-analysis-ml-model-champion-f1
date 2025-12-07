from azure.storage.blob import BlobServiceClient
import os
import json
import logging

logger = logging.getLogger(__name__)

class AzureBlobStorage:
    def __init__(self, connection_string: str, container: str):
        self.connection_string = connection_string
        self.container_name = container
        self.client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_client = self.client.get_container_client(self.container_name)

    def upload_json(self, data: dict, filename: str) -> None:
        blob_client = self.container_client.get_blob_client(filename)
        blob_client.upload_blob(json.dumps(data), overwrite=True)
        logger.info(f"Upload JSON: {filename}")

    def download_json(self, filename: str) -> dict:
        blob_client = self.container_client.get_blob_client(filename)
        downloaded_bytes = blob_client.download_blob().readall()
        data = json.loads(downloaded_bytes)
        logger.info(f"Download JSON: {filename}")
        return data

    def upload_parquet(self, filepath: str, blob_name: str = None) -> None:
        if blob_name is None:
            blob_name = os.path.basename(filepath)
        
        with open(filepath, "rb") as f:
            self.container_client.upload_blob(name=blob_name, data=f, overwrite=True)
        logger.info(f"Upload Parquet: {blob_name}")

    def list_blobs(self, prefix: str = "") -> list:
        return [b.name for b in self.container_client.list_blobs(name_starts_with=prefix)]