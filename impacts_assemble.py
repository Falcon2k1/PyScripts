import pyperclip
import re

#This Regex looks for a whole line, which is followed by a line with one of the fields in the second column.
serviceRegex = re.compile(r'(^.*$)(?:=?\r|\n)(.*?(?:Healthy|Unhealthy|Degraded|Unknown).*)',re.MULTILINE)
serviceTable=pyperclip.paste()

#initializing the variable before the loop
returnPaste=''

#Iterate through the returns from the Regex, grabbing only Group 1 (the actual result), and then build a string of multiple lines from it.
for x in serviceRegex.finditer(serviceTable):
    print(x.group(1))
    returnPaste += x.group(1)+'\n'

#return the result to the clipboard
pyperclip.copy(returnPaste)