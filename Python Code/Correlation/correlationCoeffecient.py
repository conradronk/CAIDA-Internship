#Args: <codes file> <input file> <delegations file> <output CSV file>

import numpy
import sys
import math
import country
import enumerations


sourceFile = enumerations.sourceFile
delegationsFile = enumerations.delegationsFile

codes = open(sys.argv[1], 'r')
input = open(sys.argv[2], 'r')
delegations = open(sys.argv[3], 'r')
CSVOutput = open(sys.argv[4], 'w')

def parseLine(currentLine):
    line = currentLine.split('|')
    code = line[sourceFile.CC]
    year = line[sourceFile.year]
    
    # Checks if country exists, and adds it if it doesn't
    if line[sourceFile.CC] not in countries:
        countries[code] = country.country()
        countries[code].setName(code)
    
    countries[code].addGDP(year, line[sourceFile.GDP])
    countries[code].addIPs(year, line[sourceFile.IPs])
    countries[code].addASNs(year, line[sourceFile.ASNs])
    countries[code].addCumulativeIPs(year, line[sourceFile.IPsC])
    countries[code].addCumulativeASNs(year, line[sourceFile.ASNsC])

def extractValue(array):
    try:
        if (array[0,1] == array[1,0]):
            return(array[0,1])
        elif (math.isnan(array[0,1]) and math.isnan(array[1,0])):
            return None
        else:
            print("the values " + str(array[0,1]) + " and " + str(array[1,0]) + " from an array are not equal")
            print(array)
    except IndexError:
        print("array does not have the right dimensions:")
        print(array)

def generateListIPs(code, startYear):
    GDPs = []
    IPs = []
    
    for key in sorted(countries[code].getGDPDict().keys()):
        try:
            if int(key) >= startYear:
                GDPs.append(countries[code].getGDP(key).strip('\n'))
                IPs.append(countries[code].getIPs(key))
        except ValueError:
            print("\"" + key + "\" is not a number")
    
    list = numpy.array([GDPs,IPs])
    return list

def generateListASNs(code, startYear):
    GDPs = []
    ASNs = []
    
    for key in sorted(countries[code].getGDPDict().keys()):
        try:
            if int(key) >= startYear:
                GDPs.append(countries[code].getGDP(key).strip('\n'))
                ASNs.append(countries[code].getASNs(key))
        except ValueError:
            print("\"" + key + "\" is not a number")
    
    list = numpy.array([GDPs,ASNs])
    return list

def parseLineDelegations(currentLine):
    line = currentLine.split('|')
    if countries[line[delegationsFile.CC]].date < int(line[delegationsFile.date]):
        countries[line[delegationsFile.CC]].date = int(line[delegationsFile.date])
        countries[line[delegationsFile.CC]].RIR = line[delegationsFile.RIR]


countries = {}
CC = set()

currentLine = input.readline()
while len(currentLine) > 1:
    parseLine(currentLine)
    currentLine = input.readline()

CCurrentLine = codes.readline()
while len(CCurrentLine) > 0:
    CC.add(CCurrentLine.strip("\n"))
    CCurrentLine = codes.readline()

currentLine = delegations.readline()
while len(currentLine) > 1:
    parseLineDelegations(currentLine)
    currentLine = delegations.readline()


CSVOutput.write("# CC|RIR|2012 GDP|IP Correlation|ASN Correlation|1998 IPs|1998 ASNs\n")

for key in countries:
    IPCorrelation = extractValue(numpy.corrcoef(generateListIPs(key, 1998)))
    ASNCorrelation = extractValue(numpy.corrcoef(generateListASNs(key, 1998)))
    
    if key in CC:
        try:
            CSVOutput.write(key + "|" + countries[key].RIR + "|"+ countries[key].getGDP(2012).strip("\n") + "|" + str(IPCorrelation) + "|" + str(ASNCorrelation) + "|" + str(countries[key].getCumulativeIPs(1998)) + "|" + str(countries[key].getCumulativeASNs(1998)) + "\n")
        except KeyError:
            print("\"" + key + "\" does not have a GDP value for 2012")