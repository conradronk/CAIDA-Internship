CONTENTS
	[1] Package Information
	[2] Data Sources/URLS
	[3.1] Script Summary
	[3.2] Script Details



[1] Information
As a whole, the scripts in this package produce a variety of graphs and CSV files to facilitate the
analysis of the relationship between a country's GDP and its consumption of internet address resources

Unless otherwise noted, all scripts should be executed with Python 3.X. Python 3.3.3 was used.

All the graphing scripts use GNUPlot. GNUPlot 4.6 was used.

The results/output are available in the Results folder.

Created by Conrad Ronk, 2014
conradronk@gmail.com



[2] Data sources:

	Delegation files: ftp://ftp.apnic.net/pub/stats [/arin, /afrinic, /apnic, /lanic, /ripe-ncc/]
		Each RIR has it's own directory. 
		The delegations files can be found under their respective RIRs, in the format: 
			delegated-RIR-YYYYMMDD.txt
	
	GDP information: http://data.worldbank.org/indicator/NY.GDP.MKTP.CD
		Download Data -> CSV
		Columns B through D (B,C,D) need to be removed manually. This can be done with any spreadsheet software.



[3.1] Script Summary:

|Input                   |Script                  |Result                  |
|------------------------|------------------------|------------------------|
|GDP CSV                 |GDPConvert.py           |formatted GDP           |
|------------------------|------------------------|------------------------|
|delegations files       |preProcessor.py         |delegations file (clean)|
|------------------------|------------------------|------------------------|
|delegations file (clean)|delegateParser.py       |formatted delegations   |
|------------------------|------------------------| ------------------------|
|formatted delegations   |combine.py              |formatted data wo/RIRs  |
|formatted GDP           |                        |                        |
|------------------------|------------------------|------------------------|


Graphing/plotting
|Input                   |Script                  |Result                  |
|------------------------|------------------------|------------------------|
|Formatter data wo/RIRs  |plot.py                 |PNG graphs              | # this plotting script is required because
|                        |                        |codes file              | # it checks the completeness of the data
|------------------------|------------------------|------------------------|
|The following scripts are optional                                        |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |IPPlot.py               |PNG Graphs              |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |ASNPlot.py              |PNG Graphs              |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |PCP_LinePlot.py         |PNG Graphs              |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |PCP_IPPlot.py           |PNG Graphs              |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |PCP_ASNPlot.py          |PNG Graphs              |
|------------------------|------------------------|------------------------|


|Input                   |Script                  |Result                  |
|------------------------|------------------------|------------------------|
|formatted data wo/RIRs  |correlationCoeffecient.p|correlations CSV        |
|codes file              |y                       |                        |
|delegations file        |                        |                        |
|------------------------|------------------------|------------------------|
|codes file              |format.py               |HTML file               | # Produces an HTML file which display all the graphs and correlation values
|------------------------|------------------------|------------------------|



[3.2] Script Details:

GDPConvert.py - Re-formats the CSV GDP files from the World Bank
	- /GDP Processing/GDPConvert.py
	
	- Args: <Input file> <Output file> <NoNull>
		- Input File: The manually-formatted CSV file
		- Output file: desired output file location
		- NoNull: Whether or not to output null years. 0 = output all values, 1 = output only valid values.
	
	- Notes:
		- The CSV file provided by the World bank includes several redundant columns.
		  Columns B through D need to be removed manually. For reference, see GDP_Source.csv
		- Requires Python 2.X, as the countryutils module was not written for Python 3.X


preProcessor.py - Combines and cleans the delegations files
	- /Pre-Processor/preProcessor.py
	
	- Args: <Output file> <Delegations file 1> <Delegations file 2> <Delegations file n>
		- Output file: desired output file location
		- Delegations file n: All delegations files to be processed

	- Notes:
		- Requires Python 2.X, as the countryutils module was not written for Python 3.X


delegateParser.py - Sums and reformats the delegations file
	- /Delegate Parser/delegateParser.py
	
	- Args: <Input file> <Output file>
		- Input file: The output from preProcessor.py
		- Output file: Desired output file location


combine.py - Combines the GDP and parser delegations file
	- /Combine/combine.py
	
	- Args: <Delegations file> <GDP file> <Output File>
		- Delegations file: The output from delegateParser.py
		- GDP file: The output from GDPConvert.py
		- Output file: desired output file location


plot.py - Generates line graphs of precent change over start of GDP, IPs, and ASNs
	- /Graphing/plotter/plot.py

	- Args: <Input file> <codes> <graph output directory> <threshold (float)>
		- Input file: The output from combine.py
		- codes: desired output file location, which will list all countries that meet or exceed the threshold
		- graph output directory: directory for all the graph images
		- threshold: a float value between 0 and 1 specifying the minimun percent of complete data



ASNPlot.py - Generates scatterplots of GDP against ASNs
	- /Graphing/scattererASNs/ASNPlot.py
	
	- Args: <Input file> <graph output directory>
		- Input file: The output from combine.py
		- graph output directory: directory for all the graph images



IPPlot.py - Generates scatterplots of GDP against IPs
	- /Graphing/scattererIPs/IPPlot.py
	
	- Args: <Input file> <graph output directory>
		- Input file: The output from combine.py
		- graph output directory: directory for all the graph images



PCP_LinePlot.py - Generates line graphs of precent change over previous of GDP, IPs, and ASNs
	- /Graphing/PCP_plotter/PCP_LinePlot.py
	
	- Args: <Input file> <codes> <graph output directory> <threshold (float)>
		- Input file: The output from combine.py
		- codes: desired output file location, which will list all countries that meet or exceed the threshold
		- graph output directory: directory for all the graph images
		- threshold: a float value between 0 and 1 specifying the minimun percent of complete data



PCP_ASNPlot.py - Generates scatterplots of GDP against ASNs, but instead uses percent change over previous
	- /Graphing/PCP_ scattererASNs/PCP_ASNPlot.py
	
	- Args: <Input file> <graph output directory>
		- Input file: The output from combine.py
		- graph output directory: directory for all the graph images



PCP_IPPlot.py - Generates scatterplots of GDP against IPs, but instead uses percent change over previous
	- /Graphing/PCP_scattererIPs/PCP_IPPlot.py
	
	- Args: <Input file> <graph output directory>
		- Input file: The output from combine.py
		- graph output directory: directory for all the graph images



correlationCoeffecient.py - Calculates the Pearson product-moment correlation coefficient of between GDP and IPs/ASNs
	- /Correlation/correlationCoeffecient.py
	
	- Args: <Codes file> <Input file> <Delegations file> <Output file>
		- Codes file: The countries with sufficient data accuracy - the output from plot.py
		- Input file: The output from correlationCoeffecient.py
		- Delegations file: The output from delegationParser.py
		- Output file: Desired output file location




format.py - Creates an HTML file which presented the graphs and correlation data
	- /Formatter/format.py
	
	- Args: <Codes file> <Correlations file> <Output HTMl file>
		- Codes file: The countries with sufficient data accuracy - the output from plot.py
		- Correlations file: The output from correlationCoeffecient.py
		- Output HTMl file: Desired output file location
	
	- Notes:
		- The produced HTML file references images from pre-defined folders.
		  Referto the /Formatter/ folder for placeholders