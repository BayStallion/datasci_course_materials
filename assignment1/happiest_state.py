import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])

    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] = int(score)

    state_sentiments = {}

    for tweet in tweet_file.readlines():
    	parsed_tweet = json.loads(tweet)

    	sent = 0

        if ("place" not in parsed_tweet):
            continue

        place = parsed_tweet["place"]

        if place is None or "country" not in place or place["country"] != "United States" or "place_type" not in place or place["place_type"] != "city":
            continue

        full_name = place["full_name"]

        m = re.search('(?<=,\s)\w{2}', full_name)

        if (m is None):
            continue
        
        state = m.group(0)

    	if ("text" in parsed_tweet):
    		#print "Text: '" + parsed_tweet["text"] + "'"
    		words = parsed_tweet["text"].lower().split()

    		words_list = []

    		#first examine the pairs
    		for i in range(0, len(words) - 2):
    			pair = words[i] + " " + words[i + 1]
    			if (pair in scores):
    				sent = sent + scores[pair]
    				i = i + 1
    			else:
    				words_list.append(words[i])
    				if (i == len(words) - 2):
    					words_list.append(words[i + 1])
    				
    		for word in words_list:
    			#print "Word = '" + word + "'"
    			if (word in scores):
    				sent = sent + scores[word]

        if state in state_sentiments:
            state_sentiments[state] = (state_sentiments[state][0] + sent, state_sentiments[state][1] + 1)
        else:
            state_sentiments[state] = (sent, 1)            

    max_sent = -99999999
    happiest_state = 'UNDEF'
    for state in state_sentiments:
        avg_sent = state_sentiments[state][0]/state_sentiments[state][1]
        if (avg_sent > max_sent):
            max_sent = avg_sent
            happiest_state = state

    print happiest_state

if __name__ == '__main__':
    main()
