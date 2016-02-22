import sys
import json
import os

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def main():

    #AFINN-111.txt output.txt
      
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
        
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
        
    import json
    tweets = []
    
    for line in tweet_file:
      try: 
        tweets.append(json.loads(line))
      except:
        pass
    
    allscore=[]
    for tweet in tweets:
        #print tweet
        tweetscore=0
        if "text" in tweet.keys():
            text=tweet["text"].split()
            #print text
            for word in text:
                word=word.encode('utf-8')
                word=word.rstrip('_:/\|><@_#$"&%*^()'+"'"+'')
                #word=word.rstrip(string.punctuation+'_:/\|><@_#$"&%*^()'+"'"+'')
                word=word.replace("\n", "")
                word=word.replace("\t", "")
                word=word.lower()
                #word=word.translate((word.maketrans("",""), string.punctuation))
                #print word
                if word in scores.keys():
                    tweetscore=tweetscore+scores[word]
            print tweetscore
     
if __name__ == '__main__':
    main()
