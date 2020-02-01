import json
import random
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from silodatabase import SiloDatabase
from datetime import date

# Load config for SQL
with open("sql_config.json") as f:
    config = json.load(f)
    
Base = declarative_base()
engine = create_engine(config["mysql_url"])

df = pd.read_sql("SELECT * FROM silo_details", engine).drop("id", axis= 1)

locs = ["U. P.", "Delhi", "Rajasthan"]
types = ["warehouse", "silo", "type c"]

for i in range(100):
    values = {
        "silo_name": "silo_{}".format(i),
        "silo_id": "silo_{}".format(i),
        "silo_address": "a",
        "silo_district": "a",
        "silo_city": "a",
        "silo_state": random.choice(locs),
        "lease_expiry": date(2022, 1, 1),
        "contact_person_id": "person_{}".format(i%10),
        "silo_type": random.choice(types)
    }
    df = df.append(values, ignore_index= True)

print(df)

df.to_sql("silo_details", engine, if_exists= "append", index= False)