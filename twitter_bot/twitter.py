#!/usr/bin/env python3 
#
# Karl Beckman
# kbeckman@kth.se
#
import tweepy
import json 


class Twetter:
    def __init__(self, credentials = None, tweetString = ''):
        self.__credentials = credentials
        self.__tweetString = tweetString
        self.__auth = None
        self.__api = None
        self.__apiOK = False

    def setCredentials(self, filename):
        with open(filename, 'rb') as f:
            self.__credentials = json.load(f)

    def setAuth(self):
        if self.__credentials == None:
            print("No credentials, can't set up authentication.")
            return 
        else: 
            self.__auth = tweepy.OAuthHandler(self.__credentials["consumer_key"], self.__credentials["consumer_secret"])
            self.__auth.set_access_token(self.__credentials["access_token"], self.__credentials["access_token_secret"])
            print("Authentication set.")
    
    def setApi(self):
        self.__api = tweepy.API(self.__auth)

        try:
            self.__api.verify_credentials()
            print("Authentication OK!")
            self.__apiOK = True 
        except:
            print("Error during authentication.")
    
    def setTweetString(self, tweetString):
        self.__tweetString = tweetString

    def tweet(self):
        if self.__apiOK and len(self.__tweetString) > 0:
            self.__api.update_status(self.__tweetString)
            print("I just tweeted!")
        else:
            print("Couldn't tweet.")


def main():
    filename = "credentials.json"
    with open(filename, 'rb') as f:
        credentials = json.load(f)
    
    tweetString = "Test tweet using Tweepy"
    tweetObj = Twetter(credentials, tweetString)
    
    tweetObj.setAuth()
    tweetObj.setApi()
    #tweetObj.tweet()
if __name__ == "__main__":
    main()


