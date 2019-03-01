import countryutils
import sys
import csv

def c3_c2(input):
    good = True
    try:
        code = countryutils.cca3_to_ccn(input)
    except KeyError:
        good = False
        print("Code: " + input + " does not refer to a country")
    if good:
        return countryutils.ccn_to_cca2(code)
    else:
        return "*"

def parseCountry(input):
    name = input["Country Code"]
    countries[name] = {}
    for key in input:
         if key != "Country Code":
             countries[name][key] = input[key]

def outputCountry(code):
    country = countries[code]
    output = ""
        
    for key in country:
        if (c3_c2(code) != "*"):
            output +=c3_c2(code) + "|" + key + "|" + country[key] + "\n"
    return output

def outputCountryNoNull(code):
    country = countries[code]
    output = ""
    
    for key in country:
        if country[key] != "":
            if (c3_c2(code) != "*"):
                output +=c3_c2(code) + "|" + key + "|" + country[key] + "\n"
    return output

output = open(sys.argv[2], 'w')

try:
	if sys.argv[3] == '1':
		noNull = True
	else:
		noNull = False
except IndexError:
	noNull = False

# holds CC -> [year -> value]
countries = {}

with open(sys.argv[1], 'rb') as csvfile:
    file = csv.DictReader(csvfile, delimiter=',')
    for row in file:
        parseCountry(row)

finalOutput = ""



for key in countries:
	if not noNull:
	    finalOutput += outputCountry(key)
	elif noNull:
		finalOutput += outputCountryNoNull(key)

output.write(finalOutput)