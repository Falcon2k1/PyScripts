from pprint import pprint
import openpyxl
import os
import code

# setting this up for script
os.chdir('C:\\Users\\Will Jones\\OneDrive\\Code\\python\\scripts')

# set up the link to document
db = openpyxl.load_workbook(filename = 'erannorth_db.xlsx')

# set up vars for the two worksheets
race_ws = db["races"]
class_ws = db["classes"]

# set up the race dictionaries
race_dict = {}
class_dict = {}

for work_dict_tuple in [(race_ws, race_dict), (class_ws,class_dict)]:
    for row in work_dict_tuple[0].iter_rows(values_only=True):
        name = ""
        for cell in row:
            if name == "":
                work_dict_tuple[1][cell] = []
                flag = True
                name = cell
            elif cell: work_dict_tuple[1][name].append(cell)
# populate both

# safety check to remove empty values
tempList = []
for char_class in class_dict:
    if class_dict[char_class] == []:
        tempList.append(char_class)

for char_class in tempList:
    class_dict.pop(char_class)

# okay, now for output

for char_race in race_dict:
    print_string = "\n" + char_race.capitalize().center(40,"-") + "\n"
    print_string += "Affinities: "
    for affinity in race_dict[char_race]:
        print_string += affinity.capitalize() + ", "
    print_string = print_string.rstrip(", ") + "\n"
    print_string += "Compatible Classes:"
    for char_class in class_dict:
        list_comparison = set(race_dict[char_race]) & set(class_dict[char_class])
        if list_comparison:
            print_string += "\n" + char_class.capitalize() + ": "
            for affinity in list_comparison:
                print_string += affinity.capitalize() + ", "
        print_string = print_string.rstrip(", ")
    print(print_string)


#code.interact(local=locals())