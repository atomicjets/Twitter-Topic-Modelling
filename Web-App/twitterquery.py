from twython import Twython
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from langdetect import detect
import re


def fetchTweets(queryTopic,twitter):


    """

    fetchTweets(String, TwitterApiObject) -> listOfString

    returns a list of Tweets (strings)


    >>> APP_SECRET = ####
    >>> APP_KEY = ####
    >>> twitter = Twython(APP_KEY,APP_SECRET)
    >>> fetchTweets("Python", twitter)
        ["I love python!", "Python is the best language", "Python is great, but so it C++!",....]


    """
    
    raw_data = twitter.search(q=str(queryTopic), count= 10, lang='en')

    tweets = []

    #search through JSON data and extract the tweets only.
    for tweet in raw_data['statuses']:
        tweets.append((tweet['text']).encode('ascii', 'ignore'))
     
        
    for i in range(0,len(tweets)):
        #removing all links, because really its just gonna mess up topic modeling
        tweets[i] =re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweets[i])
        #removing #'s, '\n''s, and 'RT'
        tweets[i] = tweets[i].replace("#","")
        tweets[i] = tweets[i].replace("\n","")
        if tweets[i][:2] == "RT":
            while(tweets[i][:2] != ': '):
                tweets[i] = tweets[i][1:]
            tweets[i] = tweets[i][2:]
            
            
    tweets = filter(lambda x: len(x) > 3, tweets)
    
    return tweets
 