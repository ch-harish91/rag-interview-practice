from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Python

Python is a programming language.

## Variables

Variables store values.

## Functions

Functions perform tasks.

## Classes

Classes support OOP.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(markdown_text)

print("Total Chunks:", len(documents))

for i, doc in enumerate(documents, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(doc.page_content)
    print(doc.metadata)