from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text, Date, Search, Document
from elasticsearch.helpers import bulk, scan
from elasticsearch import Elasticsearch
from . import models
import pprint

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index
class BlogPostIndex(Document):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Index:
        name = 'blogpost-index'
        settings = {
          "number_of_shards": 2,
        }

# Bulk indexing function, run in shell
def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=[b.indexing() for b in BlogPostIndex.objects.all().iterator()])

# Simple search function
def search(author):
    es = Elasticsearch()
    response = scan(es,
    query={"query": {"match": {"author": "pranav"}}},
    index="blogpost-index",
    doc_type="_doc"
    )
    pprint.pprint(response)

    return response 

    # s = Search().filter('term', author=author)
    # response = s.execute()
    # return response