#%%
import os
import kaggle

DATASET_PATH = os.path.join('datasets')
COMPETITION_NAME = 'tabular-playground-series-sep-2021'
#function for downloading data from kaggle
def fetch_comp_data(dataset_path=DATASET_PATH, competition_name=COMPETITION_NAME):
    os.makedirs(dataset_path, exist_ok=True)
    os.system('kaggle competitions download '+competition_name+' -p '+dataset_path)
    #now unzip the file
    #this is a work in progress



    
#%%