# Fortune100BestPlacesToWork
Extracting data from from Fortute.com to decide where to apply

## Overview:
This code works by using BeautifulSoup html parser to parse and loop through Fortune's list of top 100 places to work. The URL to the best company (salesforce) is passed into it and the program parses the information and generates the link for the next company to parse. 
** There is a known issue with company #75 Atlantic Health Sytstem, where fortune.come/best-companies/atlantic-health-sytstem/ doesn't always load and thus crashes the program. A simple check was put in to skip that company. All the information that is extracted is printed to a csv file. 

## Copyright:
I made this myself and am fine with anyone improving it or using it. I'd love to hear your thoughts on the project!
