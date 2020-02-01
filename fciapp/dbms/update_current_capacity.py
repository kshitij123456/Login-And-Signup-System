import json
import random
import uuid
import pandas as pd

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import silo_storage

from datetime import date

import numpy as np

# Load config for SQL
with open("sql_config.json") as f:
    config = json.load(f)
    
Base = declarative_base()
engine = create_engine(config["mysql_url"])

Session = sessionmaker(bind=engine)
session = Session()

df = pd.read_sql("SELECT * FROM silo_details", engine).drop("id", axis= 1)

storage_df = pd.read_sql("SELECT * FROM silo_storage", engine).drop(["id", "silo_current_capacity"], axis= 1)

trans_df = pd.read_sql("SELECT * FROM transactions", engine).drop("id", axis= 1)

def calc_grain_amount(trans_df):
    a = trans_df.groupby(["to_silo_id", "type_grain"]).sum()["value_grain"].reset_index().rename(columns= {"to_silo_id": "silo_id", "value_grain": "sum_grain"})
    try:
        b = trans_df.groupby(["from_silo_id", "type_grain"]).sum()["value_grain"].reset_index().rename(columns= {"from_silo_id": "silo_id", "value_grain": "sub_grain"})
    except:
        b = pd.DataFrame(columns= ["silo_id", "type_grain", "sub_grain"])
    f = pd.merge(a, b, how= "outer", on= ["silo_id", "type_grain"]).fillna(0)
    f["value_grain"] = f["sum_grain"] - f["sub_grain"]
    return f.drop(["sum_grain", "sub_grain"], axis= 1)

curr_cap = calc_grain_amount(trans_df)

output = pd.merge(storage_df, curr_cap, on=["silo_id", "type_grain"]).rename(columns= {"value_grain": "silo_current_capacity"})

# print(output.sort_values(["silo_id", "type_grain"]))

val = session.query(silo_storage).all()

for i in val:
    try:
        i.silo_current_capacity = int(output[(output["silo_id"] == i.silo_id) & (output["type_grain"] == i.type_grain)]["silo_current_capacity"].iloc[0])
    except IndexError:
        continue
try:
    session.commit()
except Exception as e:
    session.rollback()
    session.close()
    raise e