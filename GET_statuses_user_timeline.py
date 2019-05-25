# -*- coding: UTF-8 -*-
##### BEGIN IMPORT #####

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
import csv 
import time
from dateutil.parser import parse
from new_dataset_maker import *

##### END IMPORT #####

##### BEGIN AUTHENTICATION #####

access_token = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# conect to REST API
twitter_rest = Twitter(auth = oauth)

##### END AUTHENTICATION #####

print ("\nEXTRACAO INICIADA\n")

# get a number of tweets of @user_name
tweets = twitter_rest.statuses.user_timeline(screen_name = "@user_name", count = 200)
number_of_tweets = len(tweets)
print("EXTRAINDO " + str(number_of_tweets) + " tweets")

# save them to a .txt file
with open('@user_name-tweets.txt', 'w') as json_archive:
	for tweet in tweets:
		json_archive.write(json.dumps(tweet, indent = 4, sort_keys = True))
		json_archive.write('\n')

# making a simple database in a .csv file
# fields: CREATED_AT, FAVORIRE_COUNT, RETWEET_COUNT, TEXT
# save them to a .csv file
with open('@user_name-tweets-database.csv', 'w') as s_t:
	row = []
	writer = csv.writer(s_t, delimiter = ',')
	for tweet in tweets:
		row.append(str(tweet['created_at']))
		row.append(str(tweet['favorite_count']))
		row.append(str(tweet['retweet_count']))
		row.append(str(tweet['text'].replace('\n', ' ').replace('\r', '')))
		writer.writerow(row)
		row = []

# get a number of tweets of @patiobelem and save them to a .txt file
while (len(tweets) != 0):
	tweets = twitter_rest.statuses.user_timeline(screen_name = "@user_name", count = 200, max_id = tweets[len(tweets)-1]['id']-1)
	number_of_tweets = number_of_tweets + len(tweets)
	print("EXTRAINDO " + str(number_of_tweets) + " tweets")

	with open('@user_name-tweets.txt', 'a') as json_archive:
		for tweet in tweets:
			json_archive.write(json.dumps(tweet, indent = 4, sort_keys = True))
			json_archive.write('\n')

	with open('@user_name-tweets-database.csv', 'a') as s_t:
		row = []
		writer = csv.writer(s_t, delimiter = ',')
		for tweet in tweets:
			row.append(str(tweet['created_at']))
			row.append(str(tweet['favorite_count']))
			row.append(str(tweet['retweet_count']))
			row.append(str(tweet['text'].replace('\n', ' ').replace('\r', '')))
			writer.writerow(row)
			row = []

print ("\nEXTRACAO CONCLUIDA\n")

new_dataset_by_year = create_dataset_by_year('@user_name-tweets-database.csv', '2017')
new_dataset_by_month = create_dataset_by_month('@user_name-tweets-database.csv', '2017', '01')

