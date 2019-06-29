from elasticsearch import helpers, Elasticsearch
import csv
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    index = sys.argv[2]
    doc_type = sys.argv[3]
    print(filename, index, doc_type)
    es = Elasticsearch()

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter='|')
        helpers.bulk(es, reader, index=index, doc_type=doc_type)
