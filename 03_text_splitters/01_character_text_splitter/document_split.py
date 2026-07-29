from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter


# Step 1: Create a Document
document = Document(
    page_content="""
Employees work from 9 AM to 6 PM.

Employees receive 12 days of casual leave every year.

Employees can work from home with manager approval.

Employees must follow company security policies.
""",
    metadata={
        "source": "employee_handbook.pdf",
        "department": "HR"
    }
)


# Step 2: Put Document inside a list
documents = [document]


# Step 3: Create splitter
splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=70,
    chunk_overlap=10
)


# Step 4: Split Documents
chunks = splitter.split_documents(documents)


# Step 5: Check output
print(type(chunks))
print("Total chunks:", len(chunks))


# Step 6: Print each chunk
for index, chunk in enumerate(chunks):

    print("=" * 50)
    print("Chunk:", index + 1)

    print("Content:")
    print(chunk.page_content)

    print("Metadata:")
    print(chunk.metadata)