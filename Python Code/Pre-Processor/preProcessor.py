import countryutils
import sys

def checkValidity(currentLine):
    line = currentLine.split("|")

    #Add tests as necessary

    #Checks for array of necessary length resulting from .split()
    #MUST GO FIRST
    try:
        line[5]
    except IndexError:
        print(currentLine + "    is not in the correct format")
        return False

    #Checks for a valid date, using unix epoch as earliest possible.
    try:
        if (int(line[5]) < 19700101):
            print(currentLine + "    the date precedes UNIX epoch")
            return False
    except ValueError:
        print(currentLine + "    the date value is invalid")
        return False

    #Checks to make sure the country-code portion is the right length
    if not len(line[1]) == 2:
        print(currentLine + "    CC is invalid (incorrect length)")
        return False
    
    #Checks to make sure country code is actually a country
        try:
            code = countryutils.cca2_to_ccn(line[1])
        except KeyError:
            print(currentLine + "    CC is invalid (not a country)")
            return False
    
    #Checks IP/ASN against previously processed ones
    #should go last, to ensure numbers set is accurate
        if str(line[3]) not in numbers:
            numbers.add(str(line[3]))
        elif str(line[3]) in numbers:
            print(currentLine + "    Duplicate address: " + line[3])
            return False
    
    return True

def combine(files):
    currentLine = ""
    
    
    for index in range(len(files)):
        currentLine = files[index].readline()
        while len(currentLine) > 0:
            if checkValidity(currentLine):
                rows.add(currentLine)
            currentLine = files[index].readline()
        
        currentLine = " "

def output():
    output = ""
    for items in rows:
        output = output + items
    return output

errors = {} 

rows = set()

numbers = set()

#List all files to be combined:
fileNames = ["delegated-apnic-20130101.txt", "delegated-arin-20130101.txt", "delegated-afrinic-20130101.txt", "delegated-lacnic-20130101.txt", "delegated-ripencc-20130101.txt"]
files = []
outputFile = open(sys.argv[1], 'w')

# Opens and inserts all file objects into a list
for index in range(len(fileNames)):
    files.append(open(fileNames[index], 'r'))

combine(files)

outputFile.write(output())