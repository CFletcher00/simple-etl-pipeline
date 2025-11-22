import pandas as pd
from extract import extract
from transform import transform
from load import load
import logging
import os

logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    logging.info("ETL pipeline started")

    file_path = "../data/transactions.csv"
    db_path = "../database/etl.db"

    try:
        df = extract(file_path)
        logging.info("Extraction complete")

        df = transform(df)
        logging.info("Transformation complete")

        load(df, db_path)
        logging.info("Load complete")

        logging.info("ETL pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run()
