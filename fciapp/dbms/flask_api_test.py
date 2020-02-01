from flask import Flask, request
from flask_restful import Resource, Api

import json
import random
import uuid
import pandas as pd
from datetime import date
import numpy as np

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

with open("sql_config.json") as f:
    config = json.load(f)
    
Base = declarative_base()
engine = create_engine(config["mysql_url"])

Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)
api = Api(app)

class BasicSiloDetails(Resource):
    def get(self, silo_id):
        det_q = "SELECT * FROM silo_details WHERE silo_id = \"{}\"".format(silo_id)
        stor_q = "SELECT * FROM silo_storage WHERE silo_id = \"{}\"".format(silo_id)
        trans_q = "SELECT * FROM transactions WHERE to_silo_id = \"{}\" or from_silo_id = \"{}\"".format(silo_id, silo_id)

        det_df = pd.read_sql(det_q, engine).drop(["id", "silo_id"], axis= 1).astype(str)
        stor_df = pd.read_sql(stor_q, engine).drop(["id", "silo_id"], axis= 1).astype(str)
        # trans_df = pd.read_sql(trans_q, engine).drop("id", axis= 1).head(2).astype(str)
        
        # f_dict = {"silo_details": det_df.to_dict(), "silo_storage": stor_df.to_dict(), "transactions": trans_df.to_dict()}
        f_dict = {"silo_details": det_df.to_dict(), "silo_storage": stor_df.to_dict()}
        # print(*[(key, val) for key, val in f_dict.items()], sep= "\n")
        return json.dumps(f_dict)

    def put(self, **kwargs):
        return "Not allowed"

class SiloTransactions(Resource):
    def get(self, silo_id, loc, count):
        trans_q = "SELECT * FROM transactions WHERE {}_silo_id = \"{}\" or from_silo_id = \"{}\"".format(loc, silo_id, silo_id)
        trans_df = pd.read_sql(trans_q, engine).drop("id", axis= 1).head(count).astype(str)
        return json.dumps(trans_df.astype(str).to_dict())


api.add_resource(BasicSiloDetails, '/basicsilo/<string:silo_id>/')
api.add_resource(SiloTransactions, '/fullsilo/<string:silo_id>/<string:loc>/<int:count>/')

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True)
