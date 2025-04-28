from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path
from QAsystem.utils import pinecone_config

def document_generation(file_path: str) -> list :
    converter = PyPDFToDocument()
    docs = converter.run(sources=[Path(file_path)])
    return docs['documents']

def splitter(document:list):
    splitter = DocumentSplitter(split_by="sentence", split_length=2, split_overlap=0)
    splitter.warm_up()
    result = splitter.run(documents=document)
    return result['documents']

def embedder(documents:list):
    doc_embedder = SentenceTransformersDocumentEmbedder()
    doc_embedder.warm_up()
    result = doc_embedder.run(documents=documents)
    return result['documents'][:748]

document_generation = document_generation(file_path='./data/input.pdf')
split_documents = splitter(document=document_generation)
embeddings = embedder(documents=split_documents)
document_store = pinecone_config()
document_writer = DocumentWriter(document_store=document_store)
document_writer.run(documents=embeddings)


