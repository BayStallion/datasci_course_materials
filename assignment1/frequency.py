import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    terms = {}

    total_terms = 0.0

    for tweet in tweet_file.readlines():
    	parsed_tweet = json.loads(tweet)

    	if ("text" in parsed_tweet):
    		words = parsed_tweet["text"].lower().split()

    		for word in words:
    			if (word in terms):
    				terms[word] = terms[word] + 1
    			else:
    				terms[word] = 1

    			total_terms = total_terms + 1

    for term in terms:
    	print term, " ", terms[term]/total_terms

if __name__ == '__main__':
    main()
