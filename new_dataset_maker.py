import csv 
import time
from dateutil.parser import parse
import os

def create_dataset_by_year(dataset, by_year):
        print ("CRIANDO NOVO DATASET: ANO %s\n" % by_year)
        with open(dataset, 'r') as data:
                row = []
                reader = csv.reader(data, delimiter = ',')
                for [created_at,favorite_count,retweet_count,text] in reader:
                        createdAt = parse(created_at, ignoretz = True)
                        date = '%s' % (createdAt)
                        day_format = time.strptime(date, "%Y-%m-%d %H:%M:%S")
                        year = time.strftime("%Y", day_format)
                        if (year == by_year):
                                row.append(created_at)
                                row.append(favorite_count)
                                row.append(retweet_count)
                                row.append(text)
                        with open('%s/patio-belem-dataset_%s.csv' % (os.getcwd(), by_year), 'a') as new_dataset:
                                writer = csv.writer(new_dataset, delimiter = ',')
                                writer.writerow(row)       
                        row = []

        print("NOVO DATASET CRIADO\n")

def create_dataset_by_month(dataset, by_year, by_month):
        print ("CRIANDO NOVO DATASET: ANO %s / MES %s\n" % (by_year,by_month))
        with open(dataset, 'r') as data:
                row = []
                reader = csv.reader(data, delimiter = ',')
                for [created_at,favorite_count,retweet_count,text] in reader:
                        createdAt = parse(created_at, ignoretz = True)
                        date = '%s' % (createdAt)
                        day_format = time.strptime(date, "%Y-%m-%d %H:%M:%S")
                        year = time.strftime("%Y", day_format)
                        month = time.strftime("%m", day_format)
                        if (year == by_year and month == by_month):
                                row.append(created_at)
                                row.append(favorite_count)
                                row.append(retweet_count)
                                row.append(text)
                        else:
                                continue                    
                        with open('%s/patio-belem-dataset_%s_%s.csv' % (os.getcwd(), by_year, by_month), 'a') as new_dataset:
                                writer = csv.writer(new_dataset, delimiter = ',')
                                writer.writerow(row)    
                        row = []

        print("NOVO DATASET CRIADO\n")
