from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# RAG

RAG combines retrieval with generation.

## Document Loaders

Document loaders read data from PDF, DOCX, CSV and websites.

## Text Splitters

Text splitters divide large documents into smaller chunks.

### CharacterTextSplitter

Splits text using character count.

### RecursiveCharacterTextSplitter

Splits text using recursive separators.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(markdown_text)

print(type(documents))
print("Total Documents:", len(documents))

for index, document in enumerate(documents):
    print("=" * 60)
    print("Document:", index + 1)

    print("Content:")
    print(document.page_content)

    print("Metadata:")
    print(document.metadata)