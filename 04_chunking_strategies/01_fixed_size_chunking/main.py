from langchain_text_splitters import CharacterTextSplitter

text = """
Python is a programming language.

Python supports Object-Oriented Programming.

Python is widely used in Artificial Intelligence.

Python is also used in Web Development.

Python is easy to learn.

Python has a huge community.
"""

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=40,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

print(type(chunks))
print("Total Chunks:", len(chunks))
print("=" * 50)

for index, chunk in enumerate(chunks):
    print(f"Chunk {index + 1}")
    print(chunk)
    print("=" * 50)