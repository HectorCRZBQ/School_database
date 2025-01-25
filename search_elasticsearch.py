# Author 1: Álvaro Rivas Álvarez
# Author 2: Héctor de la Cruz Baquero

from elasticsearch import Elasticsearch, exceptions as es_exceptions
from elasticsearch.helpers import bulk
from bs4 import BeautifulSoup
import requests

def create_index_if_not_exists(es, index):
    try:
        es.indices.create(index)
        print(f"Index '{index}' created successfully.")
    except es_exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            print(f"Index '{index}' already exists.")
            pass
        else:
            print(f"Failed to create index '{index}': {ex}")


def extract_links_with_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    unique_links = set()
    links_with_names = []
    for idx, link in enumerate(soup.find_all('a')):
        name = link.text.strip()
        href = link.get('href')
        if name and href:
            if href not in unique_links:
                unique_links.add(href)
                links_with_names.append({'id': idx, 'name': name, 'href': href})
    return links_with_names


def index_links_to_elasticsearch(links):
    es = Elasticsearch()
    index_name = 'links'
    
    try:
        es.delete_by_query(index=index_name, body={"query": {"match_all": {}}})
        print("Existing documents in 'links' index deleted successfully.")
    except es_exceptions.ConnectionError as e:
        print(f"Failed to connect to Elasticsearch: {e}")
    
    create_index_if_not_exists(es, index_name)
    
    actions = [
        {
            "_index": index_name,
            "_type": "link",
            "_source": link
        }
        for link in links
    ]
    try:
        bulk(es, actions)
        print("Links indexed successfully.")
    except es_exceptions.ConnectionError as e:
        print(f"Failed to connect to Elasticsearch: {e}")

def search_links_in_elasticsearch(keyword):
    es = Elasticsearch()
    index_name = 'links'
    res = es.search(index=index_name, body={'query': {'match': {'name': {'query': keyword, 'fuzziness': 'AUTO'}}}})
    hits = res['hits']['hits']
    search_results = [(hit['_source']['name'], hit['_source']['href']) for hit in hits]
    return search_results

def elasticsearch_main(url):
    links_with_names = extract_links_with_names(url)
    index_links_to_elasticsearch(links_with_names)