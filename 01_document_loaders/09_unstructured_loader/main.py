from langchain_unstructured import UnstructuredLoader


loader = UnstructuredLoader(
    file_path="data/company_policy.txt"
)

documents = loader.load()


print(type(documents))

print(len(documents))


for document in documents:

    print("=" * 70)

    print("PAGE CONTENT:")
    print(document.page_content)

    print("\nMETADATA:")
    print(document.metadata)