
# Document Loaders — Interview Questions and Answers

## RAG Interview Preparation

This document contains interview questions and professional answers related to **Document Loaders in Retrieval-Augmented Generation (RAG)**.

Topics covered:

- Document Loaders
- LangChain Document Objects
- TextLoader
- DirectoryLoader
- PyPDFLoader
- CSVLoader
- Docx2txtLoader
- JSONLoader
- WebBaseLoader
- BSHTMLLoader
- UnstructuredLoader
- Metadata
- Parsing
- Dependencies
- Production considerations
- Scenario-based questions

---

# SECTION 1 — FUNDAMENTAL QUESTIONS

---

## Q1. What is a Document Loader?

### Answer

A Document Loader is a component responsible for reading data from different sources such as text files, PDFs, Word documents, CSV files, JSON files, HTML files, or websites and converting the extracted content into standardized LangChain `Document` objects.

A Document typically contains:

- `page_content` — the extracted textual content
- `metadata` — information about the source

The resulting Document objects can then be passed to downstream RAG components such as text splitters, embedding models, and vector databases.

### Short Interview Answer

> A Document Loader reads data from a source and converts it into standardized Document objects containing page content and metadata for downstream RAG processing.

---

## Q2. Why do we need Document Loaders in RAG?

### Answer

RAG applications receive knowledge from different data sources and formats.

For example:

```text
PDF
DOCX
CSV
JSON
HTML
TXT
Web Pages
```

Each format stores information differently.

Document Loaders provide an ingestion layer that reads these different formats and converts the extracted information into a common Document representation.

```text
Different Data Sources
        ↓
Document Loaders
        ↓
Standardized Documents
        ↓
Text Splitters
        ↓
Embeddings
        ↓
Vector Database
```

Without this normalization, downstream RAG components would need separate processing logic for every source format.

---

## Q3. What is a LangChain Document?

### Answer

A LangChain `Document` is a standardized data structure used to represent loaded textual content together with information about its source.

The two most important fields are:

```text
Document
│
├── page_content
└── metadata
```

`page_content` stores the actual textual content.

`metadata` stores information such as:

- Source file
- Page number
- Row number
- URL
- Document title
- Language

---

## Q4. What is `page_content`?

### Answer

`page_content` contains the actual textual information extracted from the source document.

Example:

```python
document.page_content
```

could contain:

```text
Employees should work from 9 AM to 6 PM.
```

This content can later be split into chunks and converted into embeddings.

---

## Q5. What is metadata?

### Answer

Metadata is additional information that describes the source or properties of a Document.

Example:

```python
{
    "source": "data/employee_handbook.pdf",
    "page": 2
}
```

Metadata is useful for:

- Source attribution
- Citations
- Filtering
- Debugging
- Access control
- Retrieval analysis

---

## Q6. Does one file always produce one Document?

### Answer

No.

The number and granularity of Document objects depend on the loader and its loading strategy.

### Example 1

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

### Example 2

```text
1 CSV
 ↓
8 Rows
 ↓
8 Document Objects
```

Therefore, it is incorrect to assume:

```text
1 File = 1 Document
```

---

## Q7. What does `loader.load()` return?

### Answer

In LangChain document loaders, `load()` returns a list of Document objects.

Conceptually:

```text
loader.load()
      ↓
List[Document]
```

Even when only one Document is created, the return value is still a list.

Example:

```python
documents = loader.load()

print(type(documents))
```

Output:

```text
<class 'list'>
```

---

## Q8. Why does `load()` return a list?

### Answer

A single data source can produce multiple Documents.

For example:

```text
PDF
 ↓
Multiple Pages
 ↓
Multiple Documents
```

or:

```text
CSV
 ↓
Multiple Rows
 ↓
Multiple Documents
```

Returning a list provides a consistent interface whether the loader creates one Document or many Documents.

---

# SECTION 2 — TEXTLOADER

---

## Q9. What is TextLoader?

### Answer

`TextLoader` is a LangChain document loader used to load plain-text files.

It reads the textual content of the file and converts it into a LangChain Document.

```text
TXT File
   ↓
TextLoader
   ↓
Read Text
   ↓
Document
```

---

## Q10. Which package provides TextLoader?

### Answer

`TextLoader` is provided through the LangChain community integrations package used in this practice.

Installation:

```bash
uv add langchain-community
```

Import:

```python
from langchain_community.document_loaders import TextLoader
```

---

## Q11. Why don't we run `uv add TextLoader`?

### Answer

Because `TextLoader` is a Python class, not a standalone package.

The hierarchy is:

```text
langchain-community
        ↓
langchain_community
        ↓
document_loaders
        ↓
TextLoader
```

Therefore:

```bash
uv add langchain-community
```

installs the package.

Then:

```python
from langchain_community.document_loaders import TextLoader
```

imports the class into the program.

---

# SECTION 3 — DIRECTORYLOADER

---

## Q12. What is DirectoryLoader?

### Answer

`DirectoryLoader` is used to load multiple files from a directory.

It can use a glob pattern to select files and another loader class to process each matching file.

Example:

```python
loader = DirectoryLoader(
    path="data",
    glob="*.txt",
    loader_cls=TextLoader
)
```

---

## Q13. What does `path` mean in DirectoryLoader?

### Answer

`path` specifies the directory containing the files that should be loaded.

Example:

```python
path="data"
```

means:

> Search for files inside the `data` directory.

---

## Q14. What is `glob`?

### Answer

A glob pattern specifies which files should be selected.

Example:

```python
glob="*.txt"
```

means:

> Select all files ending with `.txt`.

Here:

```text
* = wildcard
```

Example matches:

```text
policy.txt
employees.txt
holidays.txt
```

---

## Q15. What is `loader_cls`?

### Answer

`loader_cls` specifies which loader class should be used to read each selected file.

Example:

```python
loader_cls=TextLoader
```

means:

> Use TextLoader to read each matching file.

Workflow:

```text
DirectoryLoader
      ↓
Find *.txt
      ↓
TextLoader
      ↓
Read Each File
      ↓
Documents
```

---

## Q16. What is the difference between DirectoryLoader and TextLoader?

### Answer

`TextLoader` reads a specific text file.

`DirectoryLoader` manages loading multiple files from a directory and delegates the actual file reading to another loader.

Example:

```text
TextLoader
   ↓
Read one text file
```

versus:

```text
DirectoryLoader
      ↓
Find multiple files
      ↓
TextLoader
      ↓
Read each file
```

---

# SECTION 4 — PYPDFLOADER

---

## Q17. What is PyPDFLoader?

### Answer

`PyPDFLoader` is a LangChain document loader used to extract textual content from PDF documents.

In the page-oriented behavior practiced in this project, each PDF page is represented as a separate Document.

```text
PDF
 ↓
PyPDFLoader
 ↓
Parse PDF
 ↓
Extract Page Text
 ↓
Documents
```

---

## Q18. Why do we install `pypdf`?

### Answer

`PyPDFLoader` is the LangChain loader interface, while `pypdf` provides the underlying PDF parsing functionality.

```text
PyPDFLoader
     ↓
uses
     ↓
pypdf
     ↓
Parse PDF
```

Therefore:

```bash
uv add langchain-community
uv add pypdf
```

---

## Q19. If a PDF has 10 pages, will PyPDFLoader always return 10 Documents?

### Answer

With the page-oriented loading mode practiced here, it generally creates one Document per PDF page.

However, a professional answer should avoid assuming that every PDF-loading strategy always behaves identically.

Document granularity depends on:

- Loader
- Loader configuration
- Loading mode
- Document-processing strategy

---

## Q20. Can PyPDFLoader extract text from every PDF?

### Answer

No.

Text-based PDFs usually work well when the PDF contains an extractable text layer.

Scanned PDFs may contain page images instead of machine-readable text.

```text
Scanned PDF
    ↓
Image
    ↓
Normal Text Extraction May Fail
    ↓
OCR / Vision Processing Required
```

---

# SECTION 5 — CSVLOADER

---

## Q21. What is CSVLoader?

### Answer

`CSVLoader` is used to load CSV data and convert rows into LangChain Documents.

Conceptually:

```text
CSV
 ↓
CSVLoader
 ↓
Rows
 ↓
Documents
```

---

## Q22. How does CSVLoader represent a CSV row?

### Answer

CSV column names and values are converted into textual content.

For example:

```text
name: Rahul
department: Engineering
role: Software Engineer
```

This becomes the Document's `page_content`.

Metadata can contain source and row information.

---

## Q23. Why can one CSV create many Documents?

### Answer

Because the loader can represent each data row as an individual Document.

Example:

```text
100 CSV Rows
      ↓
CSVLoader
      ↓
100 Document Objects
```

This allows individual records to be retrieved independently.

---

# SECTION 6 — DOCX2TXTLOADER

---

## Q24. What is Docx2txtLoader?

### Answer

`Docx2txtLoader` is used to extract textual content from Microsoft Word `.docx` documents and convert it into LangChain Documents.

```text
DOCX
 ↓
Docx2txtLoader
 ↓
docx2txt
 ↓
Extract Text
 ↓
Document
```

---

## Q25. Why is `docx2txt` required?

### Answer

`Docx2txtLoader` provides the LangChain loader integration, while the `docx2txt` package performs the underlying text extraction from `.docx` files.

Therefore:

```bash
uv add langchain-community
uv add docx2txt
```

---

# SECTION 7 — JSONLOADER

---

## Q26. What is JSONLoader?

### Answer

`JSONLoader` loads data from JSON files and converts selected JSON content into LangChain Documents.

Because JSON can contain nested structures, the loader can use a jq schema to specify which data should be selected.

---

## Q27. What is `jq_schema`?

### Answer

`jq_schema` defines which part of a JSON structure should be selected and processed.

Example:

```python
jq_schema=".[]"
```

For a JSON array, `.[]` selects each array element.

Workflow:

```text
JSON
 ↓
jq_schema
 ↓
Select Required Data
 ↓
Documents
```

---

## Q28. Why does JSONLoader need `jq`?

### Answer

The `jq` dependency provides JSON query and transformation functionality used to select the required data from the JSON structure.

Therefore:

```bash
uv add jq
```

may be required for this loader configuration.

---

# SECTION 8 — WEBBASELOADER

---

## Q29. What is WebBaseLoader?

### Answer

`WebBaseLoader` is used to load content from web pages.

It retrieves the webpage content, parses the HTML, extracts textual information, and converts it into LangChain Documents.

```text
URL
 ↓
WebBaseLoader
 ↓
HTTP Request
 ↓
HTML
 ↓
Parse
 ↓
Extract Text
 ↓
Document
```

---

## Q30. What metadata can WebBaseLoader provide?

### Answer

Depending on the webpage and loader behavior, metadata may contain information such as:

```text
source
title
language
```

Example:

```python
{
    "source": "https://example.com/",
    "title": "Example Domain",
    "language": "en"
}
```

---

## Q31. Can WebBaseLoader load every website perfectly?

### Answer

No.

A basic webpage loader may have difficulty with:

- JavaScript-rendered content
- Authentication
- Anti-bot protection
- Dynamic applications
- Rate limits
- Complex HTML structures

A browser-based or specialized ingestion approach may be required depending on the website.

---

# SECTION 9 — BSHTMLLOADER

---

## Q32. What is BSHTMLLoader?

### Answer

`BSHTMLLoader` is used to load and parse local HTML files.

It uses Beautiful Soup for HTML processing and can use `lxml` as its parser.

```text
Local HTML
    ↓
BSHTMLLoader
    ↓
BeautifulSoup
    ↓
lxml
    ↓
Parse HTML
    ↓
Extract Text
    ↓
Document
```

---

## Q33. What is the difference between WebBaseLoader and BSHTMLLoader?

### Answer

The major difference is the source.

```text
Web URL
   ↓
WebBaseLoader
```

while:

```text
Local HTML File
       ↓
BSHTMLLoader
```

WebBaseLoader retrieves content from a URL.

BSHTMLLoader processes an HTML file that already exists locally.

---

## Q34. Why is `lxml` required?

### Answer

In the configuration practiced here, `BSHTMLLoader` uses Beautiful Soup with the `lxml` parser by default.

Therefore:

```bash
uv add lxml
```

was required.

---

# SECTION 10 — UNSTRUCTUREDLOADER

---

## Q35. What is UnstructuredLoader?

### Answer

`UnstructuredLoader` is a LangChain integration that uses the Unstructured ecosystem for document ingestion and partitioning.

It can be useful for heterogeneous or more complex document-processing requirements.

```text
Document
 ↓
UnstructuredLoader
 ↓
Parse
 ↓
Partition
 ↓
Extract Elements
 ↓
LangChain Documents
```

---

## Q36. What does parsing mean?

### Answer

Parsing means reading data and understanding its structure so that useful information can be extracted.

Memory formula:

```text
Parse
 =
Read
 +
Understand Structure
```

### Example 1

HTML:

```html
<h1>Employee Policy</h1>
```

The parser recognizes that the content is a heading.

### Example 2

PDF:

A PDF parser understands the internal PDF representation and extracts text and other relevant information from it.

---

## Q37. What does partitioning mean?

### Answer

Partitioning means breaking document content into meaningful elements.

For example:

```text
Title
Paragraph
List
Table
```

A document could conceptually become:

```text
Employee Handbook → Title

Leave Policy → Heading

Employees receive 12 casual leaves. → Narrative Text
```

---

## Q38. Why not use UnstructuredLoader for every document?

### Answer

Because richer processing introduces additional dependencies, complexity, resource requirements, and deployment considerations.

For a simple text file:

```text
TextLoader
```

may be sufficient.

For heterogeneous or complex documents:

```text
Unstructured-based processing
```

may provide more useful capabilities.

The loader should be selected based on the requirements rather than simply choosing the most complex option.

---

# SECTION 11 — INTERMEDIATE INTERVIEW QUESTIONS

---

## Q39. Where do Document Loaders fit in the RAG pipeline?

### Answer

Document Loaders are part of the ingestion/indexing side of a RAG system.

```text
Raw Documents
      ↓
Document Loaders
      ↓
Documents
      ↓
Text Splitters
      ↓
Chunks
      ↓
Embedding Model
      ↓
Vectors
      ↓
Vector Database
```

They are generally one of the first processing components in the indexing pipeline.

---

## Q40. What happens after documents are loaded?

### Answer

The loaded Documents are generally passed to a text-splitting or chunking component.

```text
Documents
    ↓
Text Splitter
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Database
```

Large documents are usually divided into smaller chunks before embedding and retrieval.

---

## Q41. Why is metadata important for production RAG?

### Answer

Metadata provides information that can be used beyond semantic similarity.

It can support:

- Source citations
- Metadata filtering
- Access control
- Tenant filtering
- Document versioning
- Debugging
- Retrieval evaluation

For example:

```python
{
    "department": "HR",
    "source": "employee_handbook.pdf",
    "page": 12
}
```

can help the system filter retrieval to HR documents and provide the original source to the user.

---

## Q42. Should metadata be converted into embeddings?

### Answer

Not necessarily.

Usually the primary textual content is embedded, while metadata is stored alongside the vector and used for filtering, source tracking, or other application logic.

However, whether metadata should also influence the embedded text depends on the retrieval design.

The correct decision depends on the use case.

---

## Q43. What happens if the loader extracts bad text?

### Answer

Bad extraction damages the entire downstream RAG pipeline.

```text
Bad Extraction
      ↓
Bad Chunks
      ↓
Poor Embeddings
      ↓
Poor Retrieval
      ↓
Poor Context
      ↓
Poor LLM Answer
```

Therefore, document extraction quality must be validated before indexing.

---

## Q44. Is successful `.load()` execution enough to confirm ingestion quality?

### Answer

No.

A loader can execute successfully while producing:

- Empty content
- Broken text
- Repeated headers
- Missing tables
- Incorrect character encoding
- Navigation noise
- Poorly extracted layouts

Production systems should validate:

```text
Content Quality
Metadata Quality
Document Count
Encoding
Expected Sections
```

---

## Q45. What is lazy loading?

### Answer

Lazy loading processes or yields Documents incrementally instead of loading the complete dataset into memory at once.

Conceptually:

```text
Large Dataset
     ↓
Load Document 1
     ↓
Process
     ↓
Load Document 2
     ↓
Process
     ↓
...
```

This can reduce memory consumption for large ingestion workloads.

---

## Q46. What is the difference between `load()` and lazy loading?

### Answer

Conceptually:

`load()` collects the Documents and returns them as a list.

```text
All Documents
     ↓
List[Document]
```

Lazy loading yields Documents incrementally.

```text
Document 1 → Process
Document 2 → Process
Document 3 → Process
```

For very large datasets, incremental processing can be more memory-efficient.

---

# SECTION 12 — SCENARIO-BASED QUESTIONS

---

## Q47. You have 5,000 text files in one directory. Which loader would you use?

### Answer

I would consider `DirectoryLoader` with an appropriate underlying loader such as `TextLoader`.

```text
Directory
 ↓
DirectoryLoader
 ↓
glob="*.txt"
 ↓
TextLoader
 ↓
Documents
```

For production-scale ingestion, I would also consider lazy/incremental processing, batching, error handling, and observability rather than blindly loading all files into memory at once.

---

## Q48. You have a 500-page PDF. What would you consider before indexing it?

### Answer

I would consider:

1. Whether the PDF contains machine-readable text or scanned images.
2. Extraction quality.
3. Page and section structure.
4. Headers and footers.
5. Tables and images.
6. Metadata preservation.
7. Chunking strategy.
8. Memory and processing requirements.

I would not immediately embed the raw extraction without validating its quality.

---

## Q49. You have scanned invoices. Would you use PyPDFLoader alone?

### Answer

Not necessarily.

If the invoices contain scanned images without a machine-readable text layer, standard PDF text extraction may not be sufficient.

The pipeline may require:

```text
Scanned PDF
    ↓
OCR / Vision Extraction
    ↓
Structured Content
    ↓
Documents
    ↓
RAG Pipeline
```

---

## Q50. Your company has PDF, DOCX, HTML, and PowerPoint files. What would you do?

### Answer

I would first evaluate the complexity and extraction requirements of each format.

For straightforward documents, dedicated loaders may provide simpler and more predictable processing.

For heterogeneous documents requiring richer partitioning, I would evaluate an Unstructured-based ingestion pipeline or another suitable document-processing framework.

The correct choice depends on:

- Layout complexity
- Tables
- Images
- Required metadata
- Scale
- Accuracy requirements
- Infrastructure complexity

---

## Q51. A website loads its content only after JavaScript executes. WebBaseLoader returns almost empty content. Why?

### Answer

Because a basic HTTP-based webpage loader may receive the initial HTML before JavaScript dynamically renders the actual content.

Conceptually:

```text
Initial HTML
    ↓
Almost No Main Content
    ↓
JavaScript Executes in Browser
    ↓
Actual Content Appears
```

A browser-based or JavaScript-capable extraction approach may be required.

---

## Q52. The loader successfully reads a PDF, but retrieval quality is terrible. What would you check first?

### Answer

I would not immediately blame the embedding model.

First, I would inspect the ingestion pipeline:

```text
PDF
 ↓
Extraction Quality
 ↓
Document Structure
 ↓
Chunking Quality
 ↓
Metadata
 ↓
Embeddings
 ↓
Retrieval
```

If extraction produced broken or incomplete content, changing the embedding model will not solve the root problem.

---

# SECTION 13 — PRODUCTION-LEVEL QUESTIONS

---

## Q53. How would you design a production document ingestion pipeline?

### Answer

A production ingestion pipeline could conceptually include:

```text
Data Sources
     ↓
Source Discovery
     ↓
File Type Detection
     ↓
Loader / Parser Selection
     ↓
Content Extraction
     ↓
Validation / Cleaning
     ↓
Metadata Enrichment
     ↓
Chunking
     ↓
Embedding
     ↓
Vector Storage
     ↓
Index Tracking / Monitoring
```

I would also consider:

- Retry handling
- Failed-document queues
- Logging
- Metrics
- Idempotency
- Incremental indexing
- Versioning
- Security
- Access control
- Deduplication

---

## Q54. How would you handle loader failures in production?

### Answer

I would avoid allowing one failed document to crash the entire ingestion pipeline.

A production design should include:

```text
Document
 ↓
Try Processing
 ↓
Success → Continue Pipeline

Failure
 ↓
Log Error
 ↓
Record Failed Document
 ↓
Retry / Dead-Letter Workflow
```

The system should capture enough information to identify:

- Source
- Error type
- Loader
- Processing stage
- Retry count

---

## Q55. How would you prevent duplicate documents from being indexed?

### Answer

Possible approaches include:

- Source identifiers
- Content hashes
- File checksums
- Document IDs
- Version IDs
- Last-modified timestamps

Example:

```text
Document
 ↓
Calculate Content Hash
 ↓
Check Existing Index
 ↓
Already Exists?
   ↓
Skip / Update
```

The exact strategy depends on the source system and update requirements.

---

## Q56. How would you handle document updates?

### Answer

I would maintain a stable document identifier and version information.

Conceptually:

```text
Document Updated
      ↓
Detect Change
      ↓
Identify Old Chunks
      ↓
Remove / Replace Old Index Entries
      ↓
Reprocess Changed Content
      ↓
Generate New Embeddings
      ↓
Update Vector Database
```

This avoids leaving outdated chunks in the retrieval index.

---

## Q57. Why is observability important in document ingestion?

### Answer

Because ingestion failures can silently damage retrieval quality.

Useful metrics include:

- Number of documents discovered
- Number successfully processed
- Number failed
- Empty documents
- Processing latency
- Chunk count
- Extraction size
- Duplicate count

Without observability, a pipeline may appear healthy while indexing incomplete or corrupted content.

---

## Q58. How would you choose between a simple loader and a sophisticated document-processing framework?

### Answer

I would choose based on actual document requirements.

For simple documents:

```text
Simple Loader
 ↓
Lower Complexity
 ↓
Fewer Dependencies
 ↓
Easier Deployment
```

For complex documents:

```text
Complex Layout
Tables
Multiple Elements
Heterogeneous Formats
      ↓
Richer Document Processing
```

Using the most sophisticated tool for every document is not automatically better.

---

# SECTION 14 — COMMON INTERVIEW MISTAKES

---

## Mistake 1

### Incorrect

> Every file becomes one Document.

### Correct

> Document granularity depends on the loader and loading strategy.

---

## Mistake 2

### Incorrect

> TextLoader is a package.

### Correct

> TextLoader is a class provided by an installed package.

---

## Mistake 3

### Incorrect

> WebBaseLoader can perfectly load every website.

### Correct

> JavaScript-heavy, authenticated, protected, or dynamically rendered websites may require specialized extraction approaches.

---

## Mistake 4

### Incorrect

> PyPDFLoader can read every PDF perfectly.

### Correct

> Scanned or complex PDFs may require OCR, vision processing, or specialized parsers.

---

## Mistake 5

### Incorrect

> If `loader.load()` succeeds, the data is ready for production RAG.

### Correct

> Successful execution does not guarantee good extraction quality. Content and metadata must be validated.

---

## Mistake 6

### Incorrect

> UnstructuredLoader should always be used because it supports many formats.

### Correct

> Loader selection should depend on document complexity, extraction requirements, operational cost, dependencies, and deployment constraints.

---

# SECTION 15 — RAPID REVISION QUESTIONS

Use these questions for quick daily revision.

1. What is a Document Loader?
2. Why are Document Loaders required in RAG?
3. What is a LangChain Document?
4. What is `page_content`?
5. What is metadata?
6. What does `load()` return?
7. Why does `load()` return a list?
8. What is TextLoader?
9. What is DirectoryLoader?
10. What is `glob`?
11. What does `*.txt` mean?
12. What is `loader_cls`?
13. What is PyPDFLoader?
14. Why is `pypdf` required?
15. What is CSVLoader?
16. What is Docx2txtLoader?
17. Why is `docx2txt` required?
18. What is JSONLoader?
19. What is `jq_schema`?
20. What is WebBaseLoader?
21. What is BSHTMLLoader?
22. WebBaseLoader vs BSHTMLLoader?
23. What is UnstructuredLoader?
24. What does parsing mean?
25. What does partitioning mean?
26. Why is metadata important?
27. Does one file always create one Document?
28. What happens after document loading?
29. How would you handle scanned PDFs?
30. How would you design production document ingestion?

---

# SECTION 16 — ONE-MINUTE INTERVIEW EXPLANATION

> Document Loaders are the ingestion components of a RAG pipeline. They read data from sources such as text files, PDFs, CSV files, Word documents, JSON, HTML, or web pages and convert the extracted information into standardized LangChain Document objects. A Document typically contains `page_content`, which stores the textual content, and `metadata`, which stores source-related information such as filename, page number, row number, or URL. Different loaders can produce different Document granularities; for example, a page-oriented PDF loader may create one Document per page while CSVLoader may create one Document per row. After loading, the Documents are generally passed to text splitters for chunking before embeddings are generated and stored in a vector database.

---

# SECTION 17 — WHITEBOARD EXPLANATION

If an interviewer asks:

**"Explain where Document Loaders fit into RAG."**

Draw:

```text
             DATA SOURCES
                  │
    ┌─────────────┼─────────────┐
    │             │             │
   PDF           CSV           TXT
    │             │             │
PyPDFLoader   CSVLoader    TextLoader
    │             │             │
    └─────────────┼─────────────┘
                  ↓
             Documents
                  ↓
       page_content + metadata
                  ↓
             Text Splitter
                  ↓
                Chunks
                  ↓
              Embeddings
                  ↓
          Vector Database
                  ↓
              Retrieval
                  ↓
                 LLM
```

---

# SECTION 18 — FINAL INTERVIEW SUMMARY

The most important points to remember are:

```text
1. Different sources require appropriate ingestion strategies.

2. Document Loaders convert source data into Documents.

3. Documents contain page_content and metadata.

4. load() returns List[Document].

5. One file does not necessarily mean one Document.

6. Metadata is critical for production RAG.

7. Successful loading does not guarantee good extraction.

8. Scanned PDFs may require OCR.

9. Dynamic websites may require browser-based extraction.

10. Loader selection should be based on the actual document requirements.

11. Simple loaders reduce complexity when advanced processing is unnecessary.

12. Document loading quality directly affects downstream retrieval quality.
```

---

# Daily Practice Question

## Question

**What is a Document Loader, why is it required in a RAG system, and what happens after a document is loaded?**

Write your answer without looking at the answer above.

Try to explain it in approximately **5–7 sentences** as if you were answering an interviewer.

Your answer should include:

```text
Document Loader
      ↓
Different Data Sources
      ↓
Document Objects
      ↓
page_content + metadata
      ↓
Text Splitting
      ↓
Chunks
      ↓
Embeddings
```
