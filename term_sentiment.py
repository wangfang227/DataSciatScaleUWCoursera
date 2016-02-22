import sys
import json
import os
import string

def main():
    
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    #print 'scores',len(scores)
    tweet_file = open(sys.argv[2])
    tweets = []
    
    for line in tweet_file:
      try: 
        tweets.append(json.loads(line))
      except:
        pass
    
    word_score={}
    word_count={}
    allscore=[]
    for tweet in tweets:
    #print tweet
        tweetscore=0
        if "text" in tweet.keys():
            text=tweet["text"].split()
    #print text            
        for word in text:
            if not (word.encode('utf-8', 'ignore') == ""):
                word=word.encode('utf-8','ignore')
                #word=word.rstrip('_:/\|><@_#$"&%*^()'+"'"+'')
                word=word.rstrip(string.punctuation+'_:/\|><@_#$"&%*^()'+"'"+'')
                word=word.replace("\n", "")
                #word=word.replace("\t", "")
                #word=word.replace("\x", "")
                word=word.lower()
                if word in scores.keys():
                    tweetscore=tweetscore+scores[word]   
        for word in text:
            if not (word.encode('utf-8', 'ignore') == ""):
                word=word.encode('utf-8','ignore')
                #word=word.rstrip('_:/\|><@_#$"&%*^()'+"'"+'')
                word=word.rstrip(string.punctuation+'_:/\|><@_#$"&%*^()'+"'"+'')
                word=word.replace("\n", "")
                #word=word.replace("\t", "")
                #word=word.replace("\x", "")
                word=word.lower()
                if word not in scores.keys():
                    if word not in word_score.keys():
                        word_score[word]=tweetscore
                        word_count[word]=1
                    if word in word_score.keys():
                        word_score[word]=word_score[word]+tweetscore
                        word_count[word]=word_count[word]+1
                    
    word_score_final={}
    for word in word_count.keys():
        word_score_final[word]=word_score[word]/word_count[word]
            
    for key, value in word_score_final.items():
        print key,value
        
if __name__ == '__main__':
    main()

