import sys
import json
import os

def main():

    import json
    tweets = []
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
      try: 
        tweets.append(json.loads(line))
      except:
        pass
    
    tweetword=[]
    wordcount={}
    
    for tweet in tweets:
        #wordlist=[]
        if "text" in tweet.keys():
            text=tweet["text"].split()
            for word in text:
                if not (word.encode('utf-8', 'ignore') == ""):
                    word=word.encode('utf-8','ignore')
                    word=word.rstrip('_:/\|><@_#$"&%*^()'+"'"+'')
                    word=word.replace("\n", "")
                    word=word.lower()
                    #wordlist.append(word)
                    if word in wordcount.keys():
                        wordcount[word]=wordcount[word]+1
                    else:
                        wordcount[word]=1
    
    totalsum=sum(wordcount.values())
    wordfreq={key:round(float(value)/totalsum,6) for key, value in wordcount.items()}
    
    for key, value in wordfreq.items():
        print key,value

if __name__ == '__main__':
    main()

