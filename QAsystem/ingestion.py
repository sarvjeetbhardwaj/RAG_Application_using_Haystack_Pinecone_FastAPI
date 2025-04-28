from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path


def ingest(document_store):
    indexing = Pipeline()

    indexing.add_component('converter', PyPDFToDocument())
    indexing.add_component('splitter', DocumentSplitter(split_by='sentence', split_length=200))
    indexing.add_component('embedder', SentenceTransformersDocumentEmbedder())
    indexing.add_component('writer', DocumentWriter(document_store))

