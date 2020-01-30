from openpyxl import load_workbook
wb = load_workbook( filename = 'prac1_datamining.xlsx')

import json

import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://mwj7:ZcnrlM19FX@nosql.dcs.aber.ac.uk/mwj7')
db = client.mwj7

#the active worksheet
ws = wb.active

#iterate over rows in spreadsheet
for row in ws.iter_rows(min_row=2):
	person = {}
	for cell in row:
		if not cell.value is None:
			#get column name for key 
			attr = ws.cell(column=cell.col_idx,row=1).value
			#get cell value for value
			person[attr] = cell.value
	#insert json representation of person into mongo db here
	#json_person = json.dumps(person)
	db.mwj7.insert(person)

