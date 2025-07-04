import requests
import logging
from typing import Dict, Any, Optional

#create logger for this class
logger = logging.getLogger(__name__)

class Extract:
    
    def __init__(self, url: str):
        self.url = url
    
    def extract_data(self, count: int = 100) -> Optional[Dict[str, Any]]:

        try:
            logger.info(f"Extracting {count} users from {self.url}")

            # Make a GET request to the API endpoint with the specified count
            response = requests.get(self.url+str(count), timeout=30)
            response.raise_for_status()

            data = response.json()
            logger.info(f"Data successfully extracted {len(data.get('results', []))} users")
            return data
        
        except requests.RequestException as e:
            logger.error(f"Error extracting data: {e}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error: {timeout_err}")
            return None
        except Exception as e:
                logger.error(f"Unexpected error during extraction: {e}")
        return None
