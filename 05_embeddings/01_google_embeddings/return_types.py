from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Query Embedding
query_vector = embeddings.embed_query("What is Python?")

# Document Embeddings
document_vectors = embeddings.embed_documents([
    "Python is a programming language.",
    "Machine Learning is a subset of AI."
])

print("=" * 50)
print("embed_query() Return Type")
print(type(query_vector))

print("\nVector Length:")
print(len(query_vector))

print("\nFirst 5 Values:")
print(query_vector[:5])

print("\n" + "=" * 50)
print("embed_documents() Return Type")
print(type(document_vectors))

print("\nTotal Vectors:")
print(len(document_vectors))

print("\nType of First Vector:")
print(type(document_vectors[0]))

print("\nFirst Vector Length:")
print(len(document_vectors[0]))

print("\nFirst 5 Values:")
print(document_vectors[0][:5])