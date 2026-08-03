from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is a programming language.

It is widely used for Artificial Intelligence.

It supports Object-Oriented Programming.

Python is also used for Web Development.

Python has a huge community.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print(type(chunks))
print("Total Chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print("=" * 50)
    print(f"Chunk {index + 1}")
    print(chunk)