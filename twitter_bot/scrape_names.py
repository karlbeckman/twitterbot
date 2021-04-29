#!/usr/bin/env python3
#
# Karl Beckman
# kbeckman@kth.se
#
# input: 
#   - a class name of a td element
# return:
#   - a list of name day names

from bs4 import BeautifulSoup
import urllib.request
import re 

def namsdagsNamn(className = "today"):
    # Read url and parse data
    webUrl = urllib.request.urlopen('https://www.kalender.se/')
    data = webUrl.read()
    soup = BeautifulSoup(data, 'html.parser')

    # Extract correct content from the html, where the names are
    today = soup.find("table", { "class" : "monthback" }).find("td", {"class": className})
    nameContainer = today.find("div", {"class": "V10"})
    nameContainer = str(nameContainer)
    
    # Extract the names into a list
    pattern = re.compile('>{1}(\w+,?\s*\w*)<br/>{1}')
    names = pattern.findall(nameContainer)[0]
    names = names.split(',')
    names = [n.strip() for n in names]
    
    return names
    
def main():
    className = "monthreg"
    namnsdagsbarn = namsdagsNamn(className)
    print(namnsdagsbarn)
  
if __name__ == "__main__":
    main()

