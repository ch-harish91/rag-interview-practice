from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Documents
documents = [
    "Python is a programming language.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Football is played by eleven players."
]

# Generate document embeddings
document_vectors = embeddings.embed_documents(documents)

# User Query
query = "What is Artificial Intelligence?"

# Generate query embedding
query_vector = embeddings.embed_query(query)


# Cosine Similarity Function
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


print("=" * 60)
print("User Query:", query)
print("=" * 60)

best_score = -1
best_document = ""

for document, vector in zip(documents, document_vectors):

    score = cosine_similarity(query_vector, vector)

    print(f"\nDocument : {document}")
    print(f"Similarity Score : {score:.4f}")

    if score > best_score:
        best_score = score
        best_document = document

print("\n" + "=" * 60)
print("Most Similar Document")
print(best_document)
print("Score:", round(best_score, 4))
print("=" * 60)