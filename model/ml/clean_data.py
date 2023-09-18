import pandas as pd
import logging 

from pathlib import Path
import os
path = Path(__file__)


logging.basicConfig(
    filename='./train_logs/data.log',
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
        df = pd.read_csv(path)
        logging.info('SUCCESS: file {} \
            loaded successfully'.format(path,))
    except FileNotFoundError as err:
        logging.error('ERROR: file {} \
            not found'.format(path,))
        raise err
    return df
