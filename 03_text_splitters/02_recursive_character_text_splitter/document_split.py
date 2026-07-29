from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


document = Document(
    page_content="""
ABC Technologies provides different benefits to employees.

Employees are expected to work from 9 AM to 6 PM from Monday to Friday.

Employees who complete one year of service are eligible for 12 days of casual leave annually.

Work from home is allowed with approval from the reporting manager.

Employees must follow company information security policies and should never share passwords.
""",
    metadata={
        "source": "employee_handbook.pdf",
        "department": "HR",
        "page": 5
    }
)

documents = [document]


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)


chunks = splitter.split_documents(documents)


print("Type:", type(chunks))
print("Total chunks:", len(chunks))


for index, chunk in enumerate(chunks):
    print("=" * 60)

    print("Chunk:", index + 1)

    print("Content:")
    print(chunk.page_content)

    print("Length:", len(chunk.page_content))

    print("Metadata:")
    print(chunk.metadata)