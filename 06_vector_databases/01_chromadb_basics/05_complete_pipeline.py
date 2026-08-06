from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Create/Open Chroma Database
vector_db = Chroma(
    collection_name="complete_pipeline",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Sample Documents
documents = [
    Document(
        page_content="Python is a programming language.",
        metadata={"source": "python.pdf", "page": 1}
    ),
    Document(
        page_content="Machine Learning is a subset of Artificial Intelligence.",
        metadata={"source": "ai.pdf", "page": 5}
    ),
    Document(
        page_content="Football is played by eleven players.",
        metadata={"source": "sports.pdf", "page": 2}
    )
]

# Add Documents
vector_db.add_documents(documents)

# User Query
query = "What is Artificial Intelligence?"

# Similarity Search
results = vector_db.similarity_search(
    query=query,
    k=2
)

print("=" * 60)
print("USER QUERY")
print(query)
print("=" * 60)

for i, doc in enumerate(results, start=1):
    print(f"\nRank {i}")
    print("Content :", doc.page_content)
    print("Metadata:", doc.metadata)

print("\n" + "=" * 60)
print("Pipeline Completed Successfully!")
print("=" * 60)