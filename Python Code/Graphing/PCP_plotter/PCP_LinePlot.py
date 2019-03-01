# Args: <input file> <codes> <graph output directory> <threshold (float)>

import sys
import country
import enumerations
from subprocess import call

column = enumerations.sourceFile

# Opens necessary files
config = open("plot.gnuplot", 'w')
graphedCodes = open(sys.argv[2], 'w')
input = open(sys.argv[1], 'r')

def checkCountry(code):
    start = 1998
    end = 2012
    span = end-start
    
    threshold = sys.argv[4]
    
    IPs = span
    GDP = span
    
    # checks the cumulative IPs column for completeness
    for i in range(start, end):
        try:
            if int(float(countries[code].getCumulativeIPs(i).strip('\n'))) == 0:
                IPs -= 1
        except KeyError:
            IPs -= 1
    IPsPercent = float(IPs/span)
    
    for i in range(start, end):
        try:
            if int(float(countries[code].getGDP(i).strip('\n'))) == 0:
                GDP -= 1
        except KeyError:
            GDP -= 1
                
    GDPPercent = float(GDP/span)
    
    if (IPsPercent >= threshold) and (GDPPercent >= threshold):
        graphedCodes.write(code + "\n")
        return True
    else:
        return False

# CC|Year|IPs|ASNs|Cumulative IPs|Cumulative ASNs|GDP
def parseLine(currentLine):
    line = currentLine.split('|')
    code = line[column.CC]
    year = line[column.year]
    
    # Checks if country exists, and adds it if it doesn't
    if line[column.CC] not in countries:
        countries[code] = country.country()
        countries[code].setName(code)
    
    countries[code].addGDP(year, line[column.GDP])
    countries[code].addIPs(year, line[column.IPs])
    countries[code].addASNs(year, line[column.ASNs])
    countries[code].addCumulativeIPs(year, line[column.IPsC])
    countries[code].addCumulativeASNs(year, line[column.ASNsC])
    

# creates config file, which plots all provided files
def writeConfig(CC, outputPath, outputFile):
    config = open("plot.gnuplot", 'w')
    xLabel = "Year"
    yLabel = "Value"
    config.write("set term png size 520,350 \n")
    
    # X-Axis label
    config.write("set xlabel \"" + xLabel + "\"\n")
    
    # Y-Axis Label
    config.write("set ylabel \"" + yLabel + "\"\n")
    
    # Key Position
    config.write("set key top left\n")
    
    config.write("set output '" + outputPath + "'.'" + outputFile + "'\n")
    config.write("plot '-' using 1:2 title \"GDP\" with lines lw 2, \\\n")
    config.write("\t'-' using 1:2 title \"IPs\" with lines lw 2, \\\n")
    config.write("\t'-' using 1:2 title \"ASNs\" with lines lw 2\n")
    
    startYear = 1998
    
    i = startYear
    while i < 2013:
        try:
            if (float(countries[CC].getGDP(startYear)) != 0) and (str(int(i)-1) in countries[CC].GDP):
            	if float(countries[CC].getGDP(str(int(i)-1))) != 0:
	                percentChangeOverPrevious = (float(countries[CC].getGDP(i)) - float(countries[CC].getGDP(str(int(i)-1))))/float(countries[CC].getGDP(str(int(i)-1)))
            else:
                percentChangeOverPrevious = 0
                print("Country: " + CC + " does not have a GDP value for year " + str(i))
        except KeyError:
            print(CC + " doesn't not have the key " + str(i))
            percentChangeOverPrevious = 0
        
        config.write("\t " + str(i)  + "\t" + str(percentChangeOverPrevious) + "\n")
        i += 1
    config.write("EOF\n")
    
    countries[CC].getCumulativeIPs(str(int(i)-1))
    
    i = startYear
    while i < 2013:
        try:
            if (float(countries[CC].getCumulativeIPs(startYear)) != 0) and (str(int(i)-1) in countries[CC].cumulativeIPs):
            	if int(countries[CC].getCumulativeIPs(str(int(i)-1))) != 0:
	                percentChangeOverPrevious = (int(countries[CC].getCumulativeIPs(i)) - int(countries[CC].getCumulativeIPs(str(int(i)-1))))/int(countries[CC].getCumulativeIPs(str(int(i)-1)))
            else:
                percentChangeOverPrevious = 0
                print("Country: " + CC + " does not have an IP value for year " + str(i))
        except KeyError:
            print(CC + " doesn't not have the key " + str(i))
            percentChangeOverPrevious = 0
            
        config.write("\t " + str(i)  + "\t" + str(percentChangeOverPrevious) + "\n")
        i += 1
    config.write("EOF\n")
    
    
    i = startYear
    while i < 2013:
        try:
            if (float(countries[CC].getCumulativeASNs(startYear)) != 0) and (str(int(i)-1) in countries[CC].cumulativeASNs):
            	if int(countries[CC].getCumulativeASNs(str(int(i)-1))) != 0:
	                percentChangeOverPrevious = (int(countries[CC].getCumulativeASNs(i)) - int(countries[CC].getCumulativeASNs(str(int(i)-1))))/int(countries[CC].getCumulativeASNs(str(int(i)-1)))
            else:
                percentChangeOverPrevious = 0
                print("Country: " + CC + " does not have an ASN value for year " + str(i))
        except KeyError:
            print(CC + " doesn't not have the key " + str(i))
            percentChangeOverPrevious = 0
            
        config.write("\t " + str(i)  + "\t" + str(percentChangeOverPrevious) + "\n")
        i += 1
    config.write("EOF\n")
    
    
    config.write("unset output")
    config.close()

countries = {}

currentLine = input.readline()
while len(currentLine) > 1:
    parseLine(currentLine)
    currentLine = input.readline()


for key in countries:
    if checkCountry(key):
        print(key,"{")
        writeConfig(key, str(sys.argv[3]), (key + ".png"))
        print("}\n")
        call(["gnuplot","plot.gnuplot"])