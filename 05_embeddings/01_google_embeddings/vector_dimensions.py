from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

texts = [
    "Python",
    "Machine Learning",
    "Football"
]

for text in texts:
    vector = embeddings.embed_query(text)

    print("=" * 50)
    print("Text:", text)
    print("Vector Dimension:", len(vector))
    print("First 5 Values:", vector[:5])