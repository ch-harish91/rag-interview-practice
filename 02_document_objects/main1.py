from langchain_core.documents import Document

doc1 = Document(
    page_content="Employees receive 12 days of casual leave.",
    metadata={
        "source": "employee_handbook.pdf",
        "department": "HR"
    }
)

doc2 = Document(
    page_content="Employees must change passwords every 90 days.",
    metadata={
        "source": "security_policy.pdf",
        "department": "IT"
    }
)

doc3 = Document(
    page_content="Employees can work from home two days per week.",
    metadata={
        "source": "work_policy.pdf",
        "department": "HR"
    }
)

documents = [doc1, doc2, doc3]

print(type(documents))
print("Total Documents:", len(documents))

for document in documents:
    print("=" * 50)
    print("Content:", document.page_content)
    print("Metadata:", document.metadata)