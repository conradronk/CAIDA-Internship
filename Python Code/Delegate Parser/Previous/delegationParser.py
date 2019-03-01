def parseLineASN(currentLine):
    line = currentLine.split("|")
    value = 0
    
    if (line[2] == "asn"):
        value = line[4]
        if (line[1] in countriesASN):
            countriesASN[line[1]] = int(countriesASN[line[1]]) + int(value)
        else:
            countriesASN[line[1]] = int(value)

def parseLineIP(currentLine):
    line = currentLine.split("|")
    value = 0
    
    if (line[2] == "ipv4") or (line[2] == "ipv6"):
        value = line[4]
        if (line[1] in countriesIP):
            countriesIP[line[1]] = int(countriesIP[line[1]]) + int(value)
        else:
            countriesIP[line[1]] = int(value)
        return True
    else:
        return False

def outputFromKey():
    thisLine = ""
    for key, value in countriesIP.items():
        if not key in countriesASN:
            outputDict[key] = str(key) + "|" + str(date) + "|" + str(value) + "|0"
        else:
            outputDict[key] = str(key) + "|" + str(date) + "|" + str(value) + "|" + str(countriesASN[key])
        
    for key, value in countriesASN.items():
        if not key in countriesIP:
            outputDict[key] = str(key) + "|" + str(date) + "|0|" + str(value)
    
            

fileName = raw_input("source filename: \n")
file = open(fileName, 'r+')

outputFile = raw_input("output file: \n")
output = open(outputFile, "r+")

date = fileName.split("-")[2]
date = date.split(".")[0]

countriesIP = {}
countriesASN = {}


i = 0
currentLine = file.readline()

while (len(currentLine) > 1):
    IP = parseLineIP(currentLine)
    
    if not IP:
        parseLineASN(currentLine)
    
    i = i+1
    currentLine = file.readline()


outputDict = {}

outputFromKey()

for key, value in outputDict.items():
    output.write(value + "\n")
    print value

