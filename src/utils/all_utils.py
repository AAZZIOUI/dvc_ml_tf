import yaml
import os
import json
import shutil # will be having a copy function
from tqdm import tqdm # get a progress bar to check the progress in for loops
import logging


def read_yaml(path_to_yaml: str) -> dict :
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"directory created at {dir_path}")

def save_local_df(df,df_path, index_status=False):
    """
    We use this function to store train and test data
    args:
    df: is the dataframe we want to save/store
    df_path: is the path where we want to store the dataframe df
    """
    df.to_csv(df_path,index=index_status)
    logging.info(f"data is saved at: {df_path}")

def save_reports(report: dict, report_path: str, indentation = 4):
    with open(report_path,"w") as f:
        json.dump(report, f, indent=indentation)
    logging.info(f"reports are saved at: {report_path}")

    
def copy_file(source, local):
    list_of_files = os.listdir(source)
    num_of_files = len(list_of_files)
    for file in tqdm(list_of_files, total = num_of_files, desc = f"Copying file from {source} to {local}",
                      colour = "green" ):
        src = os.path.join(source,file)
        dest = os.path.join(local,file)
        shutil.copy(src,dest)