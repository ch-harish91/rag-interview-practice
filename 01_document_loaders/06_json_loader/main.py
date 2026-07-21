from langchain_community.document_loaders import JSONLoader


# Step 1: Create JSONLoader
loader = JSONLoader(
    file_path="data/employees.json",
    jq_schema=".[]",
    text_content=False
)


# Step 2: Load JSON data
documents = loader.load()


# Step 3: Check returned type
print(type(documents))


# Step 4: Check number of Documents
print(len(documents))
for document in documents:
    print(document)

