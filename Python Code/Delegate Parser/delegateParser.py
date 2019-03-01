# Args: <input file> <output file>

import country
import sys
import enumerations

columns = enumerations.columns()

def yearFromDate(date):
    return date[0] + date[1] + date[2] + date[3]

def parseLine(currentLine):
    line = str(currentLine).split("|")
    code = line[columns.CC]
    year = yearFromDate(line[columns.date])
    
    if len(line[columns.CC]) == 2:
        if not checkCountry(code):
            newCountry(code)
        
        if (line[columns.type] == "asn"):
            getCountry(code).addASN(year, line[columns.value])
            World.addASN(year, line[columns.value])
            
        elif (line[columns.type] == "ipv4") or (line[columns.type] == "ipv6"):
            getCountry(code).addIP(year, line[columns.value])
            World.addIP(year, line[columns.value])
        
def outputAll():
    output = "# Country Code|Year|IPs|ASNs|Cumulative IPs| Cumulative ASNs \n"
    for key in countries:
        output += countries[key].outputCountry()
    output += World.outputCountry()
    return output

def newCountry(code):
    countries[code] = country.country()
    countries[code].setName(code)

def checkCountry(code):
    if code in countries:
        return True
    else:
        return False

def getCountry(code):
    return countries[code]

file = open(sys.argv[1],"r")
outputFile = open(sys.argv[2], "w")

countries = {}

World = country.country()
World.setName("World")

currentLine = file.readline()
while len(currentLine) > 1:
    parseLine(currentLine)
    currentLine = file.readline()
outputFile.write(outputAll())
