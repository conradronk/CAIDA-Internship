# Arguments: <delegations file> <gdp file> <output file>

import sys
import country
import enumerations

GDPFile = enumerations.GDP

delegationsFile = enumerations.delegations

# Output Format:
# CC|Year|IPs|ASNs|Cumulative IPs|Cumulative ASNs|GDP

def parseGDPs():
    # Runs through the GDP file
    currentLine = GDP.readline()
    while len(currentLine) > 1:
    
        #Checks to make sure line is not a comment
        if currentLine[0] != '#':
            parseLineGDP(currentLine)
        currentLine = GDP.readline()

def parseLineGDP(currentLine):
    line = currentLine.split('|')
    if line[GDPFile.CC] not in countries:
        countries[line[GDPFile.CC]] = country.country()
        countries[line[GDPFile.CC]].setName(str(line[GDPFile.CC]))
    
    countries[line[GDPFile.CC]].addGDP(line[GDPFile.year], line[GDPFile.value][:-1])

def parseDelegations():
    # Runs through all the lines of the delegations file input
    currentLine = delegations.readline()
    while len(currentLine) > 1:

        # Checks to make sure line is not a comment
        if currentLine[0] != '#':
            parseLineDelegation(currentLine)
        currentLine = delegations.readline()  

def parseLineDelegation(currentLine):
    line = currentLine.split('|')
    if line[delegationsFile.CC] not in countries:
        countries[line[delegationsFile.CC]] = country.country()
        countries[line[delegationsFile.CC]].setName(str(line[GDPFile.CC]))
    
    countries[line[delegationsFile.CC]].addIPs(line[delegationsFile.year], line[delegationsFile.IPs])
    countries[line[delegationsFile.CC]].addASNs(line[delegationsFile.year], line[delegationsFile.ASNs])
    countries[line[delegationsFile.CC]].addCumulativeIPs(line[delegationsFile.year], line[delegationsFile.cumulativeIPs])
    countries[line[delegationsFile.CC]].addCumulativeASNs(line[delegationsFile.year], line[delegationsFile.cumulativeASNs][:-1]) 

def outputAll():
    output = "# Country|Year|IPs|ASNs|Cumulative IPs|Cumulative ASNs|GDP \n"
    for key in countries:
        output += countries[key].output()
    return output

countries = {}

# Opens both the input files and output file
delegations = open(sys.argv[1], 'r')
GDP = open(sys.argv[2],'r')
outputFile = open(sys.argv[3], 'w')


parseGDPs()
parseDelegations()
outputFile.write(outputAll())