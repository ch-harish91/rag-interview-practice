from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Open Existing Chroma Database
vector_db = Chroma(
    collection_name="my_first_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# User Query
query = "What is Artificial Intelligence?"

# Similarity Search
results = vector_db.similarity_search(
    query=query,
    k=3
)

print("=" * 60)
print("User Query:", query)
print("=" * 60)

for i, document in enumerate(results, start=1):

    print(f"\nRank {i}")

    print("Content:")
    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)

    print("-" * 60)