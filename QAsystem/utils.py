from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from dotenv import load_dotenv
import os

load_dotenv()

def pinecone_config():
    document_store = PineconeDocumentStore(api_key=os.getenv('PINECONE_API_KEY'), index='default', 
                                           namespace='default', dimension=768)
    return document_store
