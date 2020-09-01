#=======================================
# Title: User Update
# Author: Professor Krasso
# Date: 8/31/20
# Modified by: Rochelle Markham
# Description: pymongo update 
#=======================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
        
    {"employee_id": "0000008"},
        
    {
        "$set": {
            "email": "rmarkham@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))
