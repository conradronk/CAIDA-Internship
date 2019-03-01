# Args: <input file> <graph output directory>

import country
import enumerations
import sys
from subprocess import call

column = enumerations.sourceFile

# Open files
input = open(sys.argv[1], 'r')

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

def writeConfig(CC, outputPath, outputFile):
    config = open("plot.gnuplot", 'w')
    xLabel = "ASNs"
    yLabel = "GDP"
    startYear = 1998
    
    config.write("set term png size 520,350 \n")
    
    # X-Axis label
    config.write("set xlabel \"" + xLabel + "\"\n")
    
    # Y-Axis Label
    config.write("set ylabel \"" + yLabel + "\"\n")
    
    # Key Position
    config.write("set key top left\n")
    
    config.write("set output '" + outputPath + "'.'" + outputFile + "'\n")
    config.write("plot '-' using 1:2 title \"Years\"\n")
    
    # Begin data output
    # should be in the format:
    # GDP_Change IPs_Change
    
    i = startYear
    while i < 2013:
    	
        try:
            if float(countries[CC].getGDP(startYear)) != 0:
                GDPpercentChange = (float(countries[CC].getGDP(i)) - float(countries[CC].getGDP(startYear)))/float(countries[CC].getGDP(startYear))
            else:
                GDPpercentChange = 0
                print("Country: " + CC + " does not have a GDP value for year " + str(i))
        except KeyError:
            print(CC + " doesn't not have the key " + str(i))
            GDPpercentChange = 0
            
        try:
            if float(countries[CC].getCumulativeASNs(startYear)) != 0:
                ASNpercentChange = (int(countries[CC].getCumulativeASNs(i)) - int(countries[CC].getCumulativeASNs(startYear)))/int(countries[CC].getCumulativeASNs(startYear))
            else:
                ASNpercentChange = 0
                print("Country: " + CC + " does not have an IP value for year " + str(i))
        except KeyError:
            print(CC + " doesn't not have the key " + str(i))
            ASNpercentChange = 0
        
        config.write("\t " + str(ASNpercentChange)  + "\t" + str(GDPpercentChange) + "\n")
        i += 1
    config.write("EOF\n")
    
    
#   i = startYear
#     while i < 2013:
#         try:
#             if float(countries[CC].getCumulativeIPs(startYear)) != 0:
#                 percentChange = (int(countries[CC].getCumulativeIPs(i)) - int(countries[CC].getCumulativeIPs(startYear)))/int(countries[CC].getCumulativeIPs(startYear))
#             else:
#                 percentChange = 0
#                 print("Country: " + CC + " does not have an IP value for year " + str(i))
#         except KeyError:
#             print(CC + " doesn't not have the key " + str(i))
#             percentChange = 0
#             
#         config.write("\t " + str(i)  + "\t" + str(percentChange) + "\n")
#         i += 1
#     config.write("EOF\n")
    
    config.write("unset output")
    config.close()


# Begin main:

countries = {}

currentLine = input.readline()
while len(currentLine) > 1:
    parseLine(currentLine)
    currentLine = input.readline()

for key in countries:
    print(key,"{")
    writeConfig(key, str(sys.argv[2]), (key + ".png"))
    print("}\n")
    call(["gnuplot","plot.gnuplot"])