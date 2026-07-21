from langchain_community.document_loaders import CSVLoader

# Step 1: Create CSVLoader
loader = CSVLoader(
    file_path="data/employees.csv"
)

# Step 2: Load CSV data
documents = loader.load()

# Step 3: Check returned type
print(type(documents))

# Step 4: Check number of Documents
print(len(documents))

for document in documents:
    print(document)
