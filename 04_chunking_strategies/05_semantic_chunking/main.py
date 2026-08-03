from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


text = """
Python is a programming language.

Python supports Object-Oriented Programming.

Functions are reusable blocks of code.

Classes are used to create objects.

Football is played by eleven players.

Cricket is very popular in India.

Lionel Messi is a football player.

Artificial Intelligence is transforming healthcare.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning uses neural networks.
"""

splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation"
)

documents = splitter.create_documents([text])

print("Total Chunks:", len(documents))

for i, doc in enumerate(documents, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(doc.page_content)
