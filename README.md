# langchain-cohere-qdrant-doc-retrieval
This Flask backend API takes a document in multiple formats (.txt, .docx, .pptx, .jpg, .png, .eml, .html, and .pdf) and allows you to perform a semantic search in 100+ languages supported by Cohere Multilingual API. Qdrant vector database is used to save embeddings.

## Setup

The following steps will guide you on how to run the application on macOS/Linux.

### Prerequisites

- Python 3
- Git
- virtualenv
- Homebrew

### Installation

1. Clone the repository

```
git clone https://github.com/menloparklab/langchain-cohere-qdrant-doc-retrieval docQA
```

2. Change into the directory

```
cd docQA
```

3. Create and activate a virtual environment

```
python3 -m venv env
source env/bin/activate
```

4. Install the required packages

```
pip install -r requirements.txt
```

5. Install Homebrew 

Follow the installation guide on [Homebrew website](https://brew.sh/).

6. Install the following brew packages

```
brew install libmagic poppler tesseract libxml2 libxslt
```

7. Create a `.env` file and set the following environment variables:

```
cohere_api_key="insert here"
openai_api_key="insert here"
qdrant_url="insert here"
qdrant_api_key="insert here"
```

Replace the values with your own API keys and Qdrant URL.

##### Qdrant url and api keys

Please signup for a free cloud-based account of [Qdrant](https://qdrant.tech/) and create a new cluster. You will then be able to get the qdrant_url and qdrant_api_key used in the section above.

8. Run the application using the following command:

```
gunicorn app:app
```

9. Access the API endpoints

The API endpoints will be live at the following routes:

- `/embed`
- `/retrieve`

### Conclusion

You have successfully installed and ran the DocQA system on your local machine. Feel free to explore the code and make changes as per your requirements.

### Connecting to a frontend

The deployed api endpoints, `/embed` and `/retrieve` can now be called from any frontend application. For bubble users, you can watch [this video](https://youtu.be/hOrtuumOrv8) for detailed instructions.

Include headers for the API:
"Content-Type": "application/json"

JSON body for `/embed`:
<br>
`
{
"collection_name": "{collection_name}",
"file_url": "{file_url}"
}
`
<br>

JSON body for `/retrieve`:
<br>
`
{
"collection_name": "{collection_name}",
"query": "{query}"
}
`
<br>
<br>

##### For Bubble users
Embed JSON for the bubble:
<br>
`
{ 
"collection_name": "<collection_name>",
"file_url": "<file_url>"
}
`
<br>

Retrieve JSON for bubble:
<br>
`
{
"collection_name": "<collection_name>",
"query": "<query>"
}
`
<br>

Feel free to reach out if any questions on [Twitter](https://twitter.com/MisbahSy)

