import sys
import json
import os

def main():
    
    tweet_file = open(sys.argv[1])
    
    import json
    tweets = []
    for line in tweet_file:
      try: 
        tweets.append(json.loads(line))
      except:
        pass
    
    tagscore={}
    for tweet in tweets:
        #print tweet
        if 'entities' and 'text' in tweet.keys():
            for ht in tweet["entities"]['hashtags']:
                #print ht
                tag=ht['text']
                if tag in tagscore.keys():
                    tagscore[tag]=tagscore[tag]+1
                else:
                    tagscore[tag]=1
                
    tagscore2=sorted(tagscore.items(),key=lambda x:x[1],reverse=True)
    for score in tagscore2[:10]:
        print score[0], score[1]
    #for key, value in tagscore2.items():
    #    print key,value
        
if __name__ == '__main__':
    main()

