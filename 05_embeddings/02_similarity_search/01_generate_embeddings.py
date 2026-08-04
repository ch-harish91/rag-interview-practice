from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load API key
load_dotenv()

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Documents
documents = [
    "Python is a programming language.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Football is played by eleven players."
]

# Generate embeddings
vectors = embeddings.embed_documents(documents)

# Print output
print("=" * 60)

for i, (doc, vector) in enumerate(zip(documents, vectors), start=1):
    print(f"Document {i}")
    print("Text:", doc)
    print("Vector Dimension:", len(vector))
    print("First 5 Values:", vector[:5])
    print("=" * 60)