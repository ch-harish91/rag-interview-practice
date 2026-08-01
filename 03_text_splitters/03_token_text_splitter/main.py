from langchain_text_splitters import TokenTextSplitter

text = """
RAG combines retrieval with generation.

Document loaders load documents from multiple sources.

Text splitters divide documents into smaller chunks.

Embeddings convert chunks into vectors.

Vector databases perform similarity search.

Large Language Models generate answers.
"""

splitter = TokenTextSplitter(
    chunk_size=20,
    chunk_overlap=5
)

chunks = splitter.split_text(text)

print(type(chunks))
print("Total Chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print("=" * 50)
    print("Chunk:", index + 1)
    print(chunk)