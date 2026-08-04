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
            "department": "Programming"
        }
    },
    {
        "id": 2,
        "text": "Machine Learning is a subset of Artificial Intelligence.",
        "metadata": {
            "source": "ai_book.pdf",
            "page": 25,
            "department": "AI"
        }
    },
    {
        "id": 3,
        "text": "Football is played by eleven players.",
        "metadata": {
            "source": "sports.pdf",
            "page": 8,
            "department": "Sports"
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

# -------------------------------
# Metadata Filter
# -------------------------------

search_department = "AI"

print("=" * 60)
print("Searching Department:", search_department)
print("=" * 60)

found = False

for record in records:

    if record["metadata"]["department"] == search_department:

        found = True

        print("\nID:", record["id"])
        print("Text:", record["text"])
        print("Source:", record["metadata"]["source"])
        print("Page:", record["metadata"]["page"])
        print("Department:", record["metadata"]["department"])

if not found:
    print("No matching records found.")