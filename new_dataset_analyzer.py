# coding: utf-8
import csv
import time
from dateutil.parser import parse
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

dataset_path = ''

dataset = pd.read_csv(dataset_path, names = ['CREATED_AT','FAVORITE_COUNT','RETWEET_COUNT','TEXT'])

day_list = []
for data in dataset.CREATED_AT:
    created_at = parse(data, ignoretz = True)
    day_list.append(created_at.day)
day_list.reverse()

new_day_list = []
number_of_tweets = []
for data in day_list:
    if data not in new_day_list:
        new_day_list.append(data)
        number_of_tweets.append(day_list.count(data))

fav_list = []
for data in dataset.FAVORITE_COUNT:
    fav_list.append(data)
fav_list.reverse()

retweet_list = []
for data in dataset.RETWEET_COUNT:
    retweet_list.append(data)
retweet_list.reverse()

favorite_count_list = []
retweet_count_list = []
index = 0
while index < len(day_list):
    start = index
    end = start + day_list.count(day_list[index])
    favorite_count_list.append(sum(fav_list[start:end]))
    retweet_count_list.append(sum(retweet_list[start:end]))
    index = end

print(new_day_list)
print(len(new_day_list))
print(number_of_tweets)
print(len(number_of_tweets))
print(favorite_count_list)
print(len(favorite_count_list))
print(retweet_count_list)
print(len(retweet_count_list))

x = np.array(new_day_list).astype(np.int)
y1 = number_of_tweets
y2 = favorite_count_list
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
plt.xticks(x)
plt.grid(True)
plt.ylabel('Number of tweets')
plt.xlabel('Dias')
plt.subplot(212)
plt.plot(x, y2, color = 'r')
plt.xticks(x)
plt.grid(True)
plt.ylabel('Number of favorites')
plt.xlabel('Dias')
plt.show()