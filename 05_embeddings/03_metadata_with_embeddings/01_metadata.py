from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    {
        "text": "Python is a programming language.",
        "metadata": {
            "source": "python.pdf",
            "page": 10,
            "author": "Guido"
        }
    },
    {
        "text": "Machine Learning is a subset of AI.",
        "metadata": {
            "source": "ai_book.pdf",
            "page": 25,
            "author": "Andrew Ng"
        }
    }
]

for document in documents:

    vector = embeddings.embed_query(document["text"])

    print("=" * 60)
    print("Text:")
    print(document["text"])

    print("\nVector Dimension:")
    print(len(vector))

    print("\nMetadata:")
    print(document["metadata"])