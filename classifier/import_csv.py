from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('movies_merged.csv') as f:
    reader = csv.DictReader(f, delimiter='|')
    helpers.bulk(es, reader, index='movies', doc_type='csv')
