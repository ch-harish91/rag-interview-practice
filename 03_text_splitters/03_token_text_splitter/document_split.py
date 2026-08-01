from langchain_core.documents import Document
from langchain_text_splitters import TokenTextSplitter

# Step 1: Create a Document
document = Document(
    page_content="""
ABC Technologies Employee Handbook

Employees work from 9 AM to 6 PM.

Employees receive 12 casual leave days every year.

Work from home requires manager approval.

Employees must protect company credentials and confidential information.
""",
    metadata={
        "source": "employee_handbook.pdf",
        "department": "HR",
        "page": 1
    }
)

# Step 2: Put the Document into a list
documents = [document]

# Step 3: Create the TokenTextSplitter
splitter = TokenTextSplitter(
    chunk_size=30,
    chunk_overlap=5
)

# Step 4: Split the Documents
chunks = splitter.split_documents(documents)

# Step 5: Print Results
print(type(chunks))
print("Total Chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print("=" * 50)
    print("Chunk:", index + 1)

    print("Content:")
    print(chunk.page_content)

    print("Metadata:")
    print(chunk.metadata)