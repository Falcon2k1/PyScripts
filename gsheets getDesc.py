import json
import pyperclip
import gspread
import requests
import time
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from collections import defaultdict

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gcloud_client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("FC ItemList").get_worksheet(1)

# Extract all of the values
# all_records = sheet.get_all_records()

# find the description column, save as var
description_column = sheet.find("Description").col
name_column = sheet.find("name").col
srd_column = sheet.find("srd").col

# Extract the RIGHT values
# Ye Olde Range A1 : AL2044
records = sheet.range('A1:AL1131')
cell_gen = (cell for cell in records \
    if cell.col == description_column \
    and not cell.value)
    #cell if cell.col == description_column for cell in records)

for cell in cell_gen:
    name_cell = str(list(filter(lambda x: x.row == cell.row and x.col == name_column, records))[0].value)
    srd_cell = str(list(filter(lambda x: x.row == cell.row and x.col == srd_column, records))[0].value)
    if srd_cell:
        API_call = "https://api.open5e.com/search/?name="+name_cell
        pprint(API_call)
        response = requests.get(API_call)
        apiResponse = response.json()
        pprint(apiResponse['results'])
        time.sleep(.5)

