import os
from src.utils.all_utils import read_yaml, create_directory, copy_file
import argparse
import pandas as pd
from tqdm import tqdm # get a progress bar to check the progress in for loops


def get_data(config_path):
    config = read_yaml(config_path)
    
    # 1. We determine source of data and directory where to locally put it (from config.yaml file).
    source_download_dirs = config["source_download_dirs"] 
    local_data_dirs = config["local_data_dirs"]

    # 2.
    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs), 
                                                    total = 2, desc = "list of folders", colour="red"):
        # first we need to create the local directory :
        create_directory([local_data_dir])
        copy_file(source_download_dir,local_data_dir )

if __name__ == '__main__': 
    
    """ this stays as it was in the previous dvc ML demo, 
    since it just reads data from config"""

    args = argparse.ArgumentParser()
    
    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)