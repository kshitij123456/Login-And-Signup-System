import json
import random
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# from silodatabase import SiloDatabase
from datetime import date

import numpy as np

# Load config for SQL
with open("sql_config.json") as f:
    config = json.load(f)
    
Base = declarative_base()
engine = create_engine(config["mysql_url"])

df = pd.read_sql("SELECT * FROM silo_details", engine).drop("id", axis= 1)

types = ["wheat", "corn", "maize", "rice"]

storage_df = pd.read_sql("SELECT * FROM silo_storage", engine).drop("id", axis= 1)

for silo_id in df["silo_id"].unique():
    vals = np.random.choice(types, 2, replace= False)
    for val in vals:
        values = {
            "silo_id": silo_id,
            "grain_type": val,
            "capacity": random.randint(1, 1000)
        }
        storage_df = storage_df.append(values, ignore_index= True)

print(storage_df)

storage_df.to_sql("silo_storage", engine, if_exists= "replace", index= False)