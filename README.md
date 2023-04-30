# langchain-cohere-qdrant-doc-retrieval
This Flask backend API takes a document in multiple formats (.txt, .docx, .pptx, .jpg, .png, .eml, .html, and .pdf) and allows you to perform a semantic search in 100+ languages supported by Cohere Multilingual API. Qdrant vector database is used to save embeddings.

### Installation

Install all the python dependencies using pip

```bash
pip install -r requirements.txt
```

Documents are read and extracted using a library named [Unstructured](https://unstructured-io.github.io/unstructured/index.html) which requires addition installations using Brew

```bash
brew install libmagic poppler tesseract libxml2 libxslt
```

### Qdrant setup

Please make an account on [Qdrant](https://qdrant.tech/) and create a new cluster. You will then be able to get the qdrant_url and qdrant_api_key used in the section below.

### Environment variables

Please assign environment variables as follows.
```
cohere_api_key="insert here"
openai_api_key="insert here"
qdrant_url="insert here"
qdrant_api_key="insert here"
```

### Run the app

Run the app using Gunicorn command

```bash
gunicorn app:app
```

The app should now be running with an api route ```/embed``` and another api route ```/retrieve```.

Feel free to reach out if any questions on [Twitter](https://twitter.com/MisbahSy)

