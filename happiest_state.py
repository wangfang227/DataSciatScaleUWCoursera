import sys
import json
import os

def main():
    
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
    
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    statescore={}
    for tweet in tweets:
        #print tweet
        if "text" and "place" in tweet.keys():
            if tweet["place"] is not None:
                if 'full_name' and 'country' in tweet['place'].keys():
                    if tweet['place']['country']=='United States':
                        state=tweet['place']['full_name'][-2:]
                else:
                    state=[]
                if  state in states:
                        tweetscore=0            
                        text=tweet["text"].split()
                        #print text
                        for word in text:
                            word=word.encode('utf-8')
                            #word=word.rstrip('?:!.,;"@#$')
                            word=word.rstrip('_:/\|><@_#$"&%*^()'+"'"+'')
                            word=word.replace("\n", "")
                            word=word.replace("\t", "")
                            word=word.lower()
                            #word=word.translate((word.maketrans("",""), string.punctuation))
                            #print word
                            if word in scores.keys():
                                tweetscore=tweetscore+scores[word]   
                        if state in statescore.keys():
                            statescore[state]=statescore[state]+tweetscore
                        else:
                            statescore[state]=tweetscore
    
    statescore2=sorted(statescore.items(),key=lambda x:x[1],reverse=True)
    print statescore2[0][0]
        
if __name__ == '__main__':
    main()

