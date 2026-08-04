from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# User query
query = "What is Artificial Intelligence?"

# Generate embedding
vector = embeddings.embed_query(query)

# Output
print("Query:")
print(query)

print("\nVector Length:")
print(len(vector))

print("\nFirst 10 Values:")
print(vector[:10])