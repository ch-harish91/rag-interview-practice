from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Documents with Metadata
documents = [
    {
        "id": 1,
        "text": "Python is a programming language.",
        "metadata": {
            "source": "python.pdf",
            "page": 10,
            "author": "Guido"
        }
    },
    {
        "id": 2,
        "text": "Machine Learning is a subset of Artificial Intelligence.",
        "metadata": {
            "source": "ai_book.pdf",
            "page": 25,
            "author": "Andrew Ng"
        }
    },
    {
        "id": 3,
        "text": "Football is played by eleven players.",
        "metadata": {
            "source": "sports.pdf",
            "page": 8,
            "author": "FIFA"
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

# Print Stored Records
for record in records:

    print("=" * 60)

    print("ID:")
    print(record["id"])

    print("\nText:")
    print(record["text"])

    print("\nEmbedding Dimension:")
    print(len(record["embedding"]))

    print("\nMetadata:")
    print(record["metadata"])