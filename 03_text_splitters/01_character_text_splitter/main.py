from langchain_text_splitters import CharacterTextSplitter
text = """
RAG combines retrieval with generation.

Document loaders load data from different sources.

Text splitters divide large documents into smaller chunks.

Embeddings convert text into numerical vectors.

Vector databases store and search those vectors.
"""
splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=80,
    chunk_overlap=20
)
chunks = splitter.split_text(text)
print(type(chunks))
print("Total chunks:", len(chunks))
for index, chunk in enumerate(chunks):
    print("=" * 50)
    print("Chunk:", index + 1)
    print(chunk)