#!/usr/bin/env python3 
#
# Karl Beckman
# kbeckman@kth.se
#
import json

from scrape_names import namsdagsNamn
from rovarspraket import rovarSpraket
from twitter import Twetter

def createString(nameList):
    if len(nameList) == 0:
        tweetStr = "Idag har tyvärr ingen namnsdag. Hellshot!"
    else:
        tweetStr = """Idag har {0} namnsdag. På rövarspråket blir dennes namn {1}.""".format(nameList[0], rovarSpraket(nameList[0]))
        if len(nameList) == 2:
            tweetStr += """ Vi får inte heller glömma {0} som också har namnsdag. På rövarspråket blir dennes namn i sin tur {1}.""".format(nameList[1], rovarSpraket(nameList[1]))

    return tweetStr

def main():
    filename = "credentials.json"
    with open(filename, 'rb') as f:
        credentials = json.load(f)

    #className = "monthreg"
    names = namsdagsNamn()
    
    tweetStr = createString(names)

    tweetObj = Twetter(credentials, tweetString=tweetStr)
    tweetObj.setAuth()
    tweetObj.setApi()
    #tweetObj.tweet()
    
if __name__ == "__main__":
    main()
