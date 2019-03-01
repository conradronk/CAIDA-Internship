class country:

    # Holds the country code
    code = ''
    
    def __init__(this):
        this.IPs = {}
        this.ASNs ={}
        this.cumulativeIPs = {}
        this.cumulativeASNs = {}
        this.GDP = {}
    
    def setName(this, code):
        this.code = code
    
    # Fills all the dictionaries with 0 values, unless they already hold a value
    def fillRow(this, year):
        if year not in this.IPs:
            this.IPs[year] = 0
        
        if year not in this.ASNs:
            this.ASNs[year] = 0
        
        if year not in this.cumulativeIPs:
            this.cumulativeIPs[year] = 0
        
        if year not in this.cumulativeASNs:
            this.cumulativeASNs[year] = 0
            
        if year not in this.GDP:
            this.GDP[year] = 0
    
    # All these add the provided value to their respective dictionaries for a certain year
    def addGDP(this, year, value):
        this.GDP[year] = value
        this.fillRow(year)
    
    def addIPs(this, year, value):
        this.IPs[year] = value
        this.fillRow(year)
    
    def addASNs(this, year, value):
        this.ASNs[year] = value
        this.fillRow(year)
    
    def addCumulativeIPs(this, year, value):
        this.cumulativeIPs[year] = value
        this.fillRow(year)
    
    def addCumulativeASNs(this, year, value):
        this.cumulativeASNs[year] = value
        this.fillRow(year)
    
    def addGDP(this, year, value):
        this.GDP[year] = value
        this.fillRow(year)
    
    # Steps through one of the dictionaries (which all have the same keys), and outputs the values in the desired format
    def output(this):
        output = ''
        
        for year in this.IPs:
            if (this.cumulativeIPs[year] == 0) and (str(int(year)-1) in this.cumulativeIPs):
                	this.cumulativeIPs[year] = this.cumulativeIPs[str(int(year)-1)]
            if (this.cumulativeASNs[year] == 0) and (str(int(year)-1) in this.cumulativeASNs):
            	this.cumulativeASNs[year] = this.cumulativeASNs[str(int(year)-1)]
            output += this.code + '|' + str(year) + '|' + str(this.IPs[year]) + '|' + str(this.ASNs[year]) + '|' + str(this.cumulativeIPs[year]) + '|' + str(this.cumulativeASNs[year]) + '|' + str(this.GDP[year]) + '\n'
        return output



