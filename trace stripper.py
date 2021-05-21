
print("Enter log file name.")
fileName = input()

file = open(fileName,"r")

outFile = open("output.txt","a+")

for x in file:
    if 'Ping' in x:
        print(x)
        outFile.write(x)
        