import csv
import os
import logging
from typing import List, Dict, Any
from dotenv import load_dotenv

#create logger for this class
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the output filename from environment variable or use default
filename = os.getenv('OUTPUT_FILENAME', 'users_cleaned.csv')

# Get the output directory from environment variable or use default
output_dir = os.getenv('OUTPUT_DIR', 'output')

class Load:
    def __init__(self, output_dir: str = output_dir):
        self.output_dir = output_dir

    def load_file(self, users: List[Dict[str, Any]], filename: str = filename) -> bool:

        if not users:
            logger.warning("No users to load. Exiting load process.")
            return False
        
        #create the output directory if it does not exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logger.info(f"Output directory created: {self.output_dir}")

        #directory and file path for the CSV output
        file_path = os.path.join(self.output_dir, filename)

        #columns in order required by the CSV file
        fieldnames = ['id', 'name', 'email', 'full_address']

        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                # Write each user to the CSV file
                for user in users:
                    writer.writerow(user)
            logger.info(f"CSV file written successfully: {file_path}")
            return True
        
        except FileNotFoundError as fnf_error:
            logger.error(f"File not found error: {fnf_error}")
            raise
        except Exception as e:
            logger.error(f"Error writing CSV file: {e}")
            raise
