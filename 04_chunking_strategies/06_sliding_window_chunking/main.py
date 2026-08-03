from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is a programming language.

Python supports Object-Oriented Programming.

Python is widely used for Artificial Intelligence.

Python is also used for Web Development.

Python has a huge community.

Python supports multiple libraries.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(chunk)