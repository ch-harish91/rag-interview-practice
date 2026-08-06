from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Open Chroma Database
vector_db = Chroma(
    collection_name="my_first_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# User Query
query = "Artificial Intelligence"

# Search with Metadata Filter
results = vector_db.similarity_search(
    query=query,
    k=2,
    filter={"source": "python.pdf"}
)

print("=" * 60)
print("Filtered Search Results")
print("=" * 60)

for i, doc in enumerate(results, start=1):
    print(f"\nRank {i}")
    print("Content:")
    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)

    print("-" * 60)