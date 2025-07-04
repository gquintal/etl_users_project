import requests
import logging
from typing import List, Dict, Any, Optional

#create logger for this class
logger = logging.getLogger(__name__)

class Extract:
    
    def __init__(self, url: str, counter: int = 100):
        self.url = url
        self.counter = counter

        self.url_full = f"{self.url}?results={self.counter}"
    
    def extract_data(self) -> List[Dict]:

        try:
            logger.info(f"Extracting {self.counter} users from {self.url}")

            # Make a GET request to the API endpoint with the specified count
            response = requests.get(self.url_full, timeout=30)
            response.raise_for_status()

            data = response.json()
            logger.info(f"Data successfully extracted {len(data.get('results', []))} users")
            # Check if 'results' key exists in the response data
            return data.get('results', [])
        
        except requests.RequestException as e:
            logger.error(f"Error extracting data: {e}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error: {timeout_err}")
        except Exception as e:
                logger.error(f"Unexpected error during extraction: {e}")
        return []
