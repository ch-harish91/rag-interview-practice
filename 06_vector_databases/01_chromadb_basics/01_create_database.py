from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Create Chroma Database
vector_db = Chroma(
    collection_name="my_first_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

print("=" * 60)
print("Chroma Database Created Successfully!")
print("Collection Name: my_first_collection")
print("Database Folder: chroma_db")
print("=" * 60)