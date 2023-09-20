import pandas as pd
import logging 
import numpy as np
from pathlib import Path
import os
path = Path(__file__)
log_path = os.path.join(
    path.absolute().parents[1],
    'train_logs',
    'data.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")

def load_data(path):
    """
    return dataframe for the csv found at path

    input:
        path: a path to the csv
    
    output:
        df: pandas dataframe
    """

    try:
        df = pd.read_csv(path, skipinitialspace=True)
        logging.info('SUCCESS: file {} \
            loaded successfully'.format(path,))
        df.replace({'?': np.nan}, inplace=True)
        df.dropna(inplace=True)
    except FileNotFoundError as err:
        logging.error('ERROR: file {} \
            not found'.format(path,))
        raise err
    return df



DATA_PATH = Path('/home/salma/Desktop/MLops/MLops-Project/data/census.csv')





if __name__ == "__main__":
    df = load_data(DATA_PATH)
    df.to_csv(DATA_PATH.parent/'census_cleaned.csv', index=False)