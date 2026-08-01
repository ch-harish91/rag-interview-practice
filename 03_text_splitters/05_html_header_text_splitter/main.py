from langchain_text_splitters import HTMLHeaderTextSplitter

html_string = """
<html>
    <body>

        <h1>RAG</h1>
        <p>RAG combines retrieval with generation.</p>

        <h2>Document Loaders</h2>
        <p>Load PDF, DOCX, CSV and HTML documents.</p>

        <h2>Text Splitters</h2>
        <p>Split large documents into smaller chunks.</p>

        <h3>CharacterTextSplitter</h3>
        <p>Uses character count.</p>

        <h3>RecursiveCharacterTextSplitter</h3>
        <p>Uses recursive separators.</p>

    </body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

splitter = HTMLHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(html_string)

print(type(documents))
print("Total Documents:", len(documents))

for index, document in enumerate(documents):
    print("=" * 60)
    print("Document:", index + 1)

    print("\nContent:")
    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)