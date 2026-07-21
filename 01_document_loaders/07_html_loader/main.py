from langchain_community.document_loaders import BSHTMLLoader


# Step 1: Create HTML Loader
loader = BSHTMLLoader(
    "data/company_website.html"
)


# Step 2: Load HTML file
documents = loader.load()


# Step 3: Check return type
print(type(documents))


# Step 4: Check number of Documents
print(len(documents))


# Step 5: Print each Document
for document in documents:

    print("=" * 70)

    print("PAGE CONTENT:")
    print(document.page_content)

    print("\nMETADATA:")
    print(document.metadata)