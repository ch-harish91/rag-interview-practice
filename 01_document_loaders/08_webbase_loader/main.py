from langchain_community.document_loaders import WebBaseLoader


# Step 1: Create WebBaseLoader
loader = WebBaseLoader(
    "https://example.com/"
)


# Step 2: Load website content
documents = loader.load()


# Step 3: Check return type
print(type(documents))


# Step 4: Check number of documents
print(len(documents))


# Step 5: Print documents
for document in documents:

    print("=" * 70)

    print("PAGE CONTENT:")
    print(document.page_content)

    print("\nMETADATA:")
    print(document.metadata)