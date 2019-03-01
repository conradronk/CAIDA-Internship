class country(object):
    name = ""
    def __init__(this):
        this.ASNs = {}
        this.IPs = {}
    
    def getIP(this, year):
        return this.IPs[year]
    
    def getASN(this, year):
        return this.ASNs[year]
    
    def setName(this, value):
        this.name = str(value)
    
    def addIP(this, year, value):
        if year in this.IPs:
            this.IPs[year] += int(value)
        else:
            this.IPs[year] = int(value)
                    
        if year not in this.ASNs:
            this.ASNs[year] = 0
    
    def addASN(this, year, value):
        if year in this.ASNs:
            this.ASNs[year] += int(value)
        else:
            this.ASNs[year] = int(value)
            
        if year not in this.IPs:
            this.IPs[year] = 0
    
    def outputCountry(this):
        output = ""
        cumulativeASNs = 0
        cumulativeIPs = 0
        
        for key in sorted(this.ASNs.keys()):
            cumulativeIPs += int(this.IPs[key])
            cumulativeASNs += int(this.ASNs[key])
            output += this.name + "|" + str(key) + "|" + str(this.IPs[key]) + "|" + str(this.ASNs[key]) + "|" + str(cumulativeIPs) +"|" + str(cumulativeASNs) + "\n"
        return output