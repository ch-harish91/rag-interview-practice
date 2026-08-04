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
    "Football is played by eleven players.",
    "Artificial Intelligence is transforming healthcare.",
    "Cricket is one of the most popular sports in India."
]

# Generate Document Embeddings
document_vectors = embeddings.embed_documents(documents)

# User Query
query = "Explain Artificial Intelligence"

# Generate Query Embedding
query_vector = embeddings.embed_query(query)


# Cosine Similarity Function
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


# Store Results
results = []

# Compare Query with Every Document
for document, vector in zip(documents, document_vectors):

    score = cosine_similarity(query_vector, vector)

    results.append((document, score))


# Sort by Similarity Score (Highest First)
results.sort(
    key=lambda x: x[1],
    reverse=True
)

# Print Top 3 Results
print("=" * 60)
print("User Query:", query)
print("=" * 60)

print("\nTop 3 Most Similar Documents\n")

for rank, (document, score) in enumerate(results[:3], start=1):
    print(f"Rank {rank}")
    print("Document :", document)
    print("Similarity Score :", round(score, 4))
    print("-" * 60)