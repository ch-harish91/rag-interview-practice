from langchain_text_splitters import HTMLHeaderTextSplitter

html = """
<html>
<body>

<h1>Python</h1>
<p>Python is a programming language.</p>

<h2>Variables</h2>
<p>Variables store values.</p>

<h2>Functions</h2>
<p>Functions perform tasks.</p>

</body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
]

splitter = HTMLHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(html)

print("Total Chunks:", len(documents))

for i, doc in enumerate(documents, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(doc.page_content)
    print(doc.metadata)