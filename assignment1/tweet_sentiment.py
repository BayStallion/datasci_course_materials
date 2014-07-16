import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])

    tweet_file = open(sys.argv[2])

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] = int(score)

    for tweet in tweet_file.readlines():
    	parsed_tweet = json.loads(tweet)

    	sent = 0
    	
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

    	print sent

if __name__ == '__main__':
    main()
