from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from dotenv import load_dotenv
import os

load_dotenv()

def pinecone_config():
    document_store = PineconeDocumentStore(
		index="newindex",
		namespace="default",
		dimension=768,
        metric="cosine",
        spec={"serverless": {"region": "us-east-1", "cloud": "aws"}}
)

    return document_store
