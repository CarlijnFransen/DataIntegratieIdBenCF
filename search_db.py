"""
Author: Carlijn Fransen
Date: 11 June 2020
Project: functions for querying mongodb database
"""

def connection_db():
    client = pymongo.MongoClient("mongodb://localhost/")
    db = client['cancer_api']
    col = db['exome_data']
    return col

def create_query(api_input_list, col):
    for x in api_input_list:
        query = {"_id": x}


def get_query(col, query):
    doc = col.find(query)
