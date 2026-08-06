from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Load API Key
load_dotenv()

# Create Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Create/Open Chroma Database
vector_db = Chroma(
    collection_name="my_first_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Documents
documents = [
    Document(
        page_content="Python is a programming language.",
        metadata={"source": "python.pdf", "page": 1}
    ),
    Document(
        page_content="Machine Learning is a subset of Artificial Intelligence.",
        metadata={"source": "ai.pdf", "page": 5}
    ),
    Document(
        page_content="Football is played by eleven players.",
        metadata={"source": "sports.pdf", "page": 2}
    )
]

# Add Documents
vector_db.add_documents(documents)

print("=" * 60)
print("Documents Added Successfully!")
print("Total Documents Added:", len(documents))
print("=" * 60)

for document in documents:
    print(document.page_content)