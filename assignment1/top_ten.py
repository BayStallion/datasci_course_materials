import sys
import json
import re



def main():
    hashtags_map = {}

    tweet_file = open(sys.argv[1])

    for tweet in tweet_file.readlines():
    	parsed_tweet = json.loads(tweet)

        if ("entities" not in parsed_tweet):
            continue

        entities = parsed_tweet["entities"]

        if "hashtags" not in entities:
            continue

        hashtags = entities["hashtags"]

        for tag in hashtags:
            if "text" in tag:
                text = tag["text"]

                if (text in hashtags_map):
                    hashtags_map[text] = hashtags_map[text] + 1
                else:
                    hashtags_map[text] = 1

    hashtagslist = sorted([(k, v) for (k, v) in hashtags_map.items()], key = lambda tup: tup[1], reverse = True)

    for item in hashtagslist[:10]:
        print item[0], ' ', item[1]

if __name__ == '__main__':
    main()
