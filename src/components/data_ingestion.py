import os
import sys
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Ensure the src directory is included in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifact", "train.csv")
    test_data_path: str = os.path.join("artifact", "test.csv")
    raw_data_path: str = os.path.join("artifact", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingetion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Saved raw data at {self.ingestion_config.raw_data_path}")

            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info(f"Saved train data at {self.ingestion_config.train_data_path}")

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Saved test data at {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingetion()  # Call the function
