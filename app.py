from flask import Flask, request
from flask_cors import CORS
import json
import urllib.request

# Loading environment variables
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.environ.get('openai_api_key')
cohere_api_key = os.environ.get('cohere_api_key')
qdrant_url = os.environ.get('qdrant_url')
qdrant_api_key = os.environ.get('qdrant_api_key')

#Flask config
app = Flask(__name__)
CORS(app)

# Test default route
@app.route('/')
def hello_world():
    return {"Hello":"World"}

## Embedding code
from langchain.embeddings import CohereEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.vectorstores import Qdrant

@app.route('/embed', methods=['POST'])
def embed_pdf():
    collection_name = request.json.get("collection_name")
    file_url = request.json.get("file_url")

    #download the file from the url provided
    folder_path = f'./'
    os.makedirs(folder_path, exist_ok=True) # Create the folder if it doesn't exist
    filename = file_url.split('/')[-1] # Filename for the downloaded file
    file_path = os.path.join(folder_path, filename) # Full path to the downloaded file
    
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    urllib.request.urlretrieve(file_url, file_path) # Download the file and save it to the local folder

    # document embedding
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split()
    print(docs)
    embeddings = CohereEmbeddings(model="multilingual-22-12", cohere_api_key=cohere_api_key)
    print(embeddings)
    print('embedding done')
    qdrant = Qdrant.from_documents(docs, embeddings, url=qdrant_url, collection_name=collection_name, prefer_grpc=True, api_key=qdrant_api_key)
    print(qdrant)
    os.remove(file_path) # Delete downloaded file
    return {"collection_name":qdrant.collection_name}

# Retrieve information from a collection
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from qdrant_client import QdrantClient

@app.route('/retrieve', methods=['POST'])
def retrieve_info():
    collection_name = request.json.get("collection_name")
    query = request.json.get("query")

    client = QdrantClient(url=qdrant_url, prefer_grpc=True, api_key=qdrant_api_key)

    embeddings = CohereEmbeddings(model="multilingual-22-12", cohere_api_key=cohere_api_key)
    qdrant = Qdrant(client=client, collection_name=collection_name, embedding_function=embeddings.embed_query)
    search_results = qdrant.similarity_search(query, k=2)
    chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key,temperature=0.2), chain_type="stuff")
    results = chain({"input_documents": search_results, "question": query}, return_only_outputs=True)
    
    return {"results":results["output_text"]}