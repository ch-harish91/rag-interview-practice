from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Step 1: Create the DirectoryLoader object
loader = DirectoryLoader(
    path="data",
    glob="*.txt",
    loader_cls=TextLoader
)

# Step 2: Load all documents
documents = loader.load()

# Step 3: Print the type of the returned object
print(type(documents))

# Step 4: Print total number of documents
print(len(documents))

# Step 5: Print every document
for document in documents:
    print(document)