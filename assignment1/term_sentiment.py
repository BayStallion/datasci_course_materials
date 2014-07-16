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

    new_terms = {}

    for tweet in tweet_file.readlines():
    	parsed_tweet = json.loads(tweet)

    	sent = 0
    	
    	if ("text" in parsed_tweet):
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
    				
    		ungraded_words = []
    		for word in words_list:
    			#print "Word = '" + word + "'"
    			if (word in scores):
    				sent = sent + scores[word]
    			else:
    				ungraded_words.append(word)

    		for word in ungraded_words:
    			if word in new_terms:
    				entry = new_terms[word]
    				new_terms[word] = (entry[0] + sent, entry[1] + 1)
    			else:
    				new_terms[word] = (sent, 1)

    for term in new_terms:
    	print term, " ", new_terms[term][0]/new_terms[term][1]

if __name__ == '__main__':
    main()
