from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

splitter = SemanticChunker(embeddings)

text = """
Python is a programming language.

Python supports object-oriented programming.

Machine learning is a branch of Artificial Intelligence.

Virat Kohli is an Indian cricketer.

Cricket is one of the most popular sports.

Embeddings convert text into vectors.
"""

documents = splitter.create_documents([text])

for document in documents:
    print("=" * 50)
    print(document.page_content)