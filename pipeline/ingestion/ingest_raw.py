import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR / "pipeline"))

import requests
import os
import time
import logging
from utils.storage import AzureBlobStorage

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "raw")

storage = AzureBlobStorage(AZURE_CONNECTION_STRING, CONTAINER_NAME)

API_URLS = {
    
    "race": "https://api.openf1.org/v1/sessions?date_start>=2023-12-01&session_name=Race",
    "race_result": "https://api.openf1.org/v1/session_result?driver_number=1&driver_number=81&driver_number=4",
    "weather": "https://api.openf1.org/v1/weather?date>=2023-12-01",
    "drivers": "https://api.openf1.org/v1/drivers",
    "race_control": "https://api.openf1.org/v1/race_control?date>=2023-12-01&driver_number=1&driver_number=81&driver_number=4",
    "position": "https://api.openf1.org/v1/position?driver_number=81&driver_number=1&driver_number=4&date>=2023-12-01"
}


def fetch_api(url: str, retries: int = 3, delay: int = 5) -> dict | list:
    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Tentativa {attempt}/{retries}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.warning(f"Falhou: {e}")
            if attempt < retries:
                time.sleep(delay)
            else:
                logger.error(f"Não foi possível acessar após {retries} tentativas")
                return {} if attempt > 1 else []
            
def ingest_all_raw():    
    for key, url in API_URLS.items():
        logger.info(f"\nFetching: {key}")
        data = fetch_api(url)
        
        if data:
            blob_path = f"raw/{key}.json"
            storage.upload_json(data, blob_path)
            logger.info(f"{key} concluído")
        else:
            logger.warning(f"{key} retornou vazio")

    logger.info("INGESTÃO CONCLUÍDA")

if __name__ == "__main__":
    ingest_all_raw()
