from langchain_text_splitters import TokenTextSplitter

text = """
Python is a programming language.

Python supports Object-Oriented Programming.

Python is widely used for Artificial Intelligence.

Python is also used for Web Development.

Python has a huge community.
"""

splitter = TokenTextSplitter(
    chunk_size=20,
    chunk_overlap=5
)

chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(chunk)