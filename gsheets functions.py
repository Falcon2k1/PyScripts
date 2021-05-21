import json
import pyperclip
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from collections import defaultdict

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gcloud_client_secret.json', scope)
client = gspread.authorize(creds)

def bracket_stripper(input,item):
    """Strips out irritating brackets from the thingy"""
    #fix variables
    

    if "{=genericBonus}" in input: 
        gbonus = str(item['inherits/genericBonus'])
        input = input.replace("{=genericBonus}","+%s" % gbonus)
    
    if "{=dmgType" in input:
        input = input.replace("{=dmgType} damage","damage of the weapon's type")

    repl_list = [
        " {@dice",
        "{@i ",
        "{@skill ",
        "{@condition ",
        "{@creature ",
        "{@spell ",
        "{@italic ",
    ]

    for repl_str in repl_list:
        input = input.replace(repl_str,"")
        input = input.replace("}","",1)

    return input

def content_filler(input,tempDict,item):
    #appending time!
    if input != 'entries': tempDict[input] = defaultdict(str)
    for key, value in item.items():
        if input in key and value:
            slash_index = key.rfind("/")+1
            true_key = key[slash_index:]
            #oh god how does descriptions work
            if 'entries' in key:
                if type(value) == str: 
                    value = bracket_stripper(value,item)
                    if value not in tempDict['inherits']['description']:
                        tempDict['inherits']['description'] += "%s\n" % value
                else:
                    tempDict['inherits']['description'] += "%s: " % value
            else:
                # if something's in the value, and it's just a string, make it a list
                if len(tempDict[input][true_key]) is not 0 and type(tempDict[input][true_key]) == str:
                    tempDict[input][true_key] = [tempDict[input][true_key],value]
                # if it's already a list, append:
                elif len(tempDict[input][true_key]) is not 0 and type(tempDict[input][true_key]) == list:
                    tempDict[input][true_key].append(value)
                # or if nothing else, string!
                else:
                    tempDict[input][true_key] = value

def list_builder(wsNum):
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("FC ItemList").get_worksheet(wsNum)

    # Extract and print all of the values
    all_records = sheet.get_all_records()

    zee_big_list=[]

    for item in all_records:

        #tempDict = defaultdict(dict)
        tempDict = {}

        #initialize dictionary
        tempDict['name'] = item['name']
        tempDict['inherits'] = {}
        tempDict['inherits']['description'] = ""

        list_of_categories=[
            'requires',
            'excludes',
            'inherits',
            'entries',
        ]

        for cat in list_of_categories:
            content_filler(cat,tempDict,item)
        
        pprint(tempDict, width=140)
        #pprint(tempDict['requires'])
        #pprint(tempDict['excludes'])

        zee_big_list.append(tempDict)

list_builder(2)

#pprint(sorted(zee_big_list))
#jsonlist = json.dumps(zee_big_list)
#pprint(jsonlist)
#pyperclip.copy(jsonlist)