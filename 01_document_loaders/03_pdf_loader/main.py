from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/employee_handbook.pdf")

documents = loader.load()
print(type(documents))
print(len(documents))

for document in documents:
    print(document)