# transfer ship data to a MongoDB collection

# get a connection to MongoDB
from pymongo import MongoClient

user = 'mwj7'
dbpath = 'nosql.dcs.aber.ac.uk/mwj7'
password = 'ZcnrlM19FX'
connection_string = 'mongodb://'+user+':'+password+'@'+dbpath

client = MongoClient(connection_string)

db = client.mwj7

# walk the ship data directory to find the excel files

import os
import get_ships

#import regular expressions
import re

all_ships = []
import pdb; pdb.set_trace()
ships_dir = '/impacs/mwj7/Documents/data-mining-practical-content/Prac2/ABERSHIP_transcription_vtls004566921'

for root, dirs, files in os.walk(ships_dir):
    for file in files:
        name, ext = os.path.splitext(file)
        if ext == '.xlsx' and not re.match("^~&*", name):
            print("Included: " + os.path.join(root,file))
            all_ships += get_ships.get_ships( os.path.join(root, file) )
        else:
            print("Excluded: " + os.path.join(root, file))

    print("Directories covered: " + str(len(dirs)))
    for d in dirs:
        print(os.path.join(root,d))


result = db.mwj7.insert_many(all_ships)
print(result)
