from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
RAG stands for Retrieval-Augmented Generation.

Document loaders read data from different sources such as PDF, CSV, DOCX, and websites.

Text splitters divide large documents into smaller chunks so that retrieval can be more precise.

Embeddings convert chunks into numerical vector representations.

Vector databases store these vectors and allow similarity search.

The retriever finds relevant chunks based on the user's query.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print("Type:", type(chunks))
print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print("=" * 60)
    print("Chunk:", index + 1)
    print(chunk)
    print("Length:", len(chunk))