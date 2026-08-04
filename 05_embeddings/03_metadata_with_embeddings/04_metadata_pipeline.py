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
    {
        "id": 1,
        "text": "Python is a programming language.",
        "metadata": {
            "source": "python.pdf",
            "department": "Programming",
            "page": 10
        }
    },
    {
        "id": 2,
        "text": "Machine Learning is a subset of Artificial Intelligence.",
        "metadata": {
            "source": "ai_book.pdf",
            "department": "AI",
            "page": 25
        }
    },
    {
        "id": 3,
        "text": "Football is played by eleven players.",
        "metadata": {
            "source": "sports.pdf",
            "department": "Sports",
            "page": 8
        }
    }
]

# Store Records
records = []

for document in documents:

    embedding = embeddings.embed_query(document["text"])

    record = {
        "id": document["id"],
        "text": document["text"],
        "embedding": embedding,
        "metadata": document["metadata"]
    }

    records.append(record)


# User Query
query = "Explain Artificial Intelligence"

query_vector = embeddings.embed_query(query)


# Cosine Similarity Function
def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


# Filter by Metadata
search_department = "AI"

results = []

for record in records:

    if record["metadata"]["department"] == search_department:

        score = cosine_similarity(
            query_vector,
            record["embedding"]
        )

        results.append((record, score))


# Sort Results
results.sort(
    key=lambda x: x[1],
    reverse=True
)


# Output
print("=" * 70)
print("User Query:", query)
print("Department Filter:", search_department)
print("=" * 70)

for rank, (record, score) in enumerate(results, start=1):

    print(f"\nRank {rank}")

    print("ID:", record["id"])

    print("Text:")
    print(record["text"])

    print("\nSimilarity Score:")
    print(round(score, 4))

    print("\nMetadata:")
    print(record["metadata"])

    print("-" * 70)