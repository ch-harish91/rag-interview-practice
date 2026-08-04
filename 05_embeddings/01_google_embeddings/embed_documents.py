from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Python is a programming language.",
    "Machine Learning is a subset of AI.",
    "Football is a popular sport."
]

vectors = embeddings.embed_documents(documents)

print("Total Documents:", len(documents))
print("Total Vectors:", len(vectors))
for i, vector in enumerate(vectors, start=1):
    print(f"\nVector {i} Length: {len(vector)}")
    print(vector[:5])