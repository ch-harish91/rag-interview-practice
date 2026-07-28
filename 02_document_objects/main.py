from langchain_core.documents import Document

document = Document(
    page_content="Employees are eligible for 12 days of casual leave per year.",
    metadata={
        "source": "employee_handbook.pdf",
        "page": 12,
        "department": "HR"
    }
)

print(document)
print(document.page_content)
print(document.metadata)