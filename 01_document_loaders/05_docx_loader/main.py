from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("data/company_policy.docx")

documents = loader.load()

print(type(documents))
print(len(documents))

for document in documents:
    print(document.page_content)
    print(document.metadata)