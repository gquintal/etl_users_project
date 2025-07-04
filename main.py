import logging
import os
import sys
from dotenv import load_dotenv
from etl import Extract, Transform, Load

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('etl.log')
        ]
    )


def main():

    setup_logging()
    logger = logging.getLogger(__name__)

    load_dotenv()

    # Get environment variables
    url = os.getenv('USERS_API_URL')
    counter = os.getenv('USERS_COUNT')

    output_dir = os.getenv('OUTPUT_DIR', 'output')
    filename = os.getenv('OUTPUT_FILENAME', 'users_cleaned.csv')
    
    logger.info("Starting ETL process")

    try:
        # Vakidate URL
        if not url.startswith('http'):
            raise ValueError("The URL must start with 'http' or 'https'")
        logger.info("The URL is valid")
    
    except ValueError as ve:
        logger.error(f"Invalid URL provided: {ve}")
        return
    
    try:
        #Extract
        logger.info("Starting data extraction")
        extract = Extract(url, counter)
        raw_data = extract.extract_data()
        
        if not raw_data:
            logger.error("No data extracted, exiting ETL process")
            return False
        
        #Transform
        logger.info("Starting data transformation")
        transform = Transform()
        users_transformed = transform.transform(raw_data)

        if not users_transformed:
            logging.error("No data transformed, exiting ETL process")
            return False
                
        #Load
        logger.info("Starting data loading")
        load = Load(output_dir)
        load.load_file(users_transformed, filename)

        if load:
            logger.info("Data loaded successfully")
            return True
        else:
            logger.error("Data loading failed")
            return False

    except Exception as e:
        logging.error(f"An error occurred during the ETL process: {e}")
        return False
    
if __name__ == "__main__":
    main()
