from elasticsearch import AsyncElasticsearch, Elasticsearch
from starlette.config import Config

config = Config()

URL = config.get("ELASTICSEARCH_URL", default="http://rest_elasticsearch:9200")

client = Elasticsearch(URL)
async_client = AsyncElasticsearch(URL)
