file = open('CountryCodeGDP.csv', 'r')
output = open('GDPOutput.csv', 'r+')

listLength = 252

country = [None] * listLength
y1999 = [None] * listLength
y2000 = [None] * listLength
y2001 = [None] * listLength
y2002 = [None] * listLength
y2003 = [None] * listLength
y2004 = [None] * listLength
y2005 = [None] * listLength
y2006 = [None] * listLength
y2007 = [None] * listLength
y2008 = [None] * listLength
y2009 = [None] * listLength
y2010 = [None] * listLength
y2011 = [None] * listLength
y2012 = [None] * listLength

currentLine = file.readline()
i = 0
j = 0
while (len(str(currentLine)) > 1):
    lineList = currentLine.split(",")

    country[i] = lineList[0]

    
    y1999[i] = lineList[1]
    y2000[i] = lineList[2]
    y2001[i] = lineList[3]
    y2002[i] = lineList[4]
    y2003[i] = lineList[5]
    y2004[i] = lineList[6]
    y2005[i] = lineList[7]
    y2006[i] = lineList[8]
    y2007[i] = lineList[9]
    y2008[i] = lineList[10]
    y2009[i] = lineList[11]
    y2010[i] = lineList[12]
    y2011[i] = lineList[13]
    y2012[i] = lineList[14]
    
    i = i+1
    
    currentLine = file.readline()

h = 0
while (h < 252):
    output.write(country[h] + "|1999|" + str(y1999[h]) + "\n")
    output.write(country[h] + "|2000|" + str(y2000[h]) + "\n")
    output.write(country[h] + "|2001|" + str(y2001[h]) + "\n")
    output.write(country[h] + "|2002|" + str(y2002[h]) + "\n")
    output.write(country[h] + "|2003|" + str(y2003[h]) + "\n")
    output.write(country[h] + "|2004|" + str(y2004[h]) + "\n")
    output.write(country[h] + "|2005|" + str(y2005[h]) + "\n")
    output.write(country[h] + "|2006|" + str(y2006[h]) + "\n")
    output.write(country[h] + "|2007|" + str(y2007[h]) + "\n")
    output.write(country[h] + "|2008|" + str(y2008[h]) + "\n")
    output.write(country[h] + "|2009|" + str(y2009[h]) + "\n")
    output.write(country[h] + "|2010|" + str(y2010[h]) + "\n")
    output.write(country[h] + "|2011|" + str(y2011[h]) + "\n")
    output.write(country[h] + "|2012|" + str(y2012[h]))
    h = h + 1
