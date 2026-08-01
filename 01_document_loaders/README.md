# RAG Interview Practice

## Retrieval-Augmented Generation — Hands-On & Interview Preparation

This repository contains my structured hands-on practice for **Retrieval-Augmented Generation (RAG)**.

The purpose of this repository is not only to write LangChain code, but also to understand:

- Why each RAG component is required
- How each component works internally
- How different components are connected
- What packages and dependencies are required
- How to debug common implementation problems
- How to explain RAG concepts professionally in interviews
- How to make design decisions for real-world RAG applications
- How to move from basic RAG concepts toward production-level RAG systems

---

# 1. What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

RAG is an architecture that improves Large Language Model (LLM) responses by retrieving relevant information from an external knowledge source and providing that information as context to the LLM before generating the final answer.

Instead of depending only on the knowledge learned during model training, RAG allows the application to retrieve relevant information from external sources such as:

- PDF documents
- Text files
- Word documents
- CSV files
- JSON files
- Websites
- Databases
- Vector databases
- Enterprise knowledge bases

---

# 2. Why RAG?

Large Language Models have several limitations when used without external knowledge retrieval.

## Problems

### 1. Knowledge Cutoff

An LLM may not know information created or updated after its training period.

### 2. Private Data

An LLM does not automatically know private organizational information such as:

- Company policies
- Internal documents
- Customer information
- Product documentation
- Enterprise knowledge

### 3. Hallucination

An LLM may generate incorrect or unsupported information when it does not have sufficient context.

### 4. Domain-Specific Knowledge

General-purpose LLMs may not contain enough detailed knowledge about a company's internal or specialized domain.

---

# 3. How RAG Solves These Problems

RAG retrieves relevant information from an external knowledge source and provides that information to the LLM as context.

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Build Context
      ↓
Question + Context
      ↓
LLM
      ↓
Grounded Final Answer
```

This allows the LLM to generate answers based on retrieved information rather than relying only on its internal knowledge.

---

# 4. Three Main Stages of RAG

A RAG system can be understood through three major stages:

```text
1. Indexing
2. Retrieval
3. Generation
```

---

## Stage 1 — Indexing

During indexing, source documents are processed and stored in a searchable representation.

```text
Documents
    ↓
Document Loaders
    ↓
Document Objects
    ↓
Text Splitting
    ↓
Chunks
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Database
```

---

## Stage 2 — Retrieval

When a user asks a question, the system searches for relevant information.

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Vector Database
      ↓
Top-K Relevant Chunks
```

---

## Stage 3 — Generation

The retrieved information is provided to the LLM.

```text
Retrieved Chunks
       +
User Question
       ↓
Build Prompt
       ↓
LLM
       ↓
Final Answer
```

---

# 5. Complete RAG Workflow

```text
Documents
    ↓
Load Documents
    ↓
Document Objects
    ↓
Split Documents into Chunks
    ↓
Generate Embeddings
    ↓
Store Vectors in Vector Database
    ↓
User Asks a Question
    ↓
Generate Query Embedding
    ↓
Similarity Search
    ↓
Retrieve Top-K Relevant Chunks
    ↓
Merge / Prepare Retrieved Context
    ↓
Build Prompt
    ↓
Context + User Question
    ↓
Send to LLM
    ↓
Generate Final Answer
```

---

# 6. Repository Learning Roadmap

```text
RAG Interview Practice
│
├── 01. Document Loaders
├── 02. Document Objects
├── 03. Text Splitters
├── 04. Chunking Strategies
├── 05. Embeddings
├── 06. Vector Databases
├── 07. Indexing Pipeline
├── 08. Retrieval Pipeline
├── 09. Prompt Construction
├── 10. Basic RAG
├── 11. Advanced Retrieval
└── 12. Production RAG
```

---

# 7. Document Loaders

## What is a Document Loader?

A **Document Loader** is a component responsible for reading data from different sources and converting the extracted information into standardized LangChain `Document` objects.

Data can come from:

- TXT files
- PDFs
- CSV files
- Word documents
- JSON files
- HTML files
- Websites
- Other document sources

---

## General Document Loading Workflow

```text
Data Source
    ↓
Document Loader
    ↓
Read / Parse / Extract Content
    ↓
LangChain Document Objects
    ↓
page_content + metadata
```

---

# 8. LangChain Document Object

After loading data, LangChain represents the extracted information using `Document` objects.

A Document mainly contains:

```text
Document
│
├── page_content
│
└── metadata
```

## page_content

Contains the actual extracted textual content.

Example:

```text
Employees should work from 9 AM to 6 PM.
```

## metadata

Contains additional information about the source.

Example:

```python
{
    "source": "data/company_policy.txt"
}
```

Metadata may also contain:

- Page number
- Page label
- Total pages
- Row number
- Source URL
- Document title
- Language
- Other source information

---

# 9. Document Loaders Practiced

The following document loaders were implemented and practiced.

```text
TXT            → TextLoader

Directory      → DirectoryLoader

PDF            → PyPDFLoader

CSV            → CSVLoader

DOCX           → Docx2txtLoader

JSON           → JSONLoader

Web URL        → WebBaseLoader

Local HTML     → BSHTMLLoader

Complex /
Multi-format   → UnstructuredLoader
```

---

# 10. TextLoader

## Purpose

`TextLoader` is used to load plain text (`.txt`) files.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import TextLoader
```

## Example

```python
loader = TextLoader("data/company_policy.txt")

documents = loader.load()
```

## Workflow

```text
TXT File
   ↓
TextLoader
   ↓
Read Text
   ↓
Create Document
   ↓
page_content + metadata
```

## Important Point

A basic text file is generally represented as a Document containing the extracted text and source metadata.

---

# 11. DirectoryLoader

## Purpose

`DirectoryLoader` is used to load multiple files from a directory.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
```

## Example

```python
loader = DirectoryLoader(
    path="data",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()
```

---

## Important Parameters

### path

Specifies where the files are located.

```python
path="data"
```

Means:

```text
Look inside the data directory.
```

---

### glob

Specifies which files should be selected.

```python
glob="*.txt"
```

`*` is a wildcard.

Therefore:

```text
*.txt
```

means:

> Select all files whose names end with `.txt`.

Example:

```text
company_policy.txt     ✓
leave_policy.txt       ✓
employee_handbook.txt  ✓

resume.pdf             ✗
employees.csv          ✗
```

---

### loader_cls

Specifies which loader should read each matching file.

```python
loader_cls=TextLoader
```

Means:

> Use `TextLoader` to read every selected text file.

---

## DirectoryLoader Workflow

```text
Directory
    ↓
DirectoryLoader
    ↓
Find Matching Files
    ↓
glob="*.txt"
    ↓
TextLoader
    ↓
Read Each File
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Interview Summary

`DirectoryLoader` loads multiple files from a directory. It uses a glob pattern to select files and a specified loader class to read each matching file.

---

# 12. PyPDFLoader

## Purpose

`PyPDFLoader` is used to load and extract text from PDF documents.

## Packages

```bash
uv add langchain-community
uv add pypdf
```

## Import

```python
from langchain_community.document_loaders import PyPDFLoader
```

## Example

```python
loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()
```

---

## Workflow

```text
PDF File
    ↓
PyPDFLoader
    ↓
pypdf
    ↓
Parse PDF
    ↓
Extract Page Text
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Important Observation

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

The page-oriented loading behavior created one Document for each page.

---

## PDF Metadata

Metadata can contain:

```text
source
page
page_label
total_pages
producer
creator
creationdate
```

Example:

```python
{
    "source": "data/employee_handbook.pdf",
    "total_pages": 3,
    "page": 0,
    "page_label": "1"
}
```

---

## Important Production Point

Not every PDF contains directly extractable text.

### Text-based PDF

```text
PDF
 ↓
Selectable Text
 ↓
PyPDFLoader
 ↓
Text Extraction
```

### Scanned PDF

```text
Scanned PDF
    ↓
Page contains images
    ↓
Normal text extraction may fail
    ↓
OCR / Vision Processing may be required
```

---

# 13. CSVLoader

## Purpose

`CSVLoader` is used to load structured CSV data.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import CSVLoader
```

## Example

```python
loader = CSVLoader(
    file_path="data/employees.csv"
)

documents = loader.load()
```

---

## Workflow

```text
CSV File
    ↓
CSVLoader
    ↓
Read CSV Rows
    ↓
Process Each Row
    ↓
Create Document
    ↓
List[Document]
```

---

## Practice Observation

The practice CSV contained:

```text
8 Employee Rows
       ↓
8 Document Objects
```

A row such as:

```text
101,Rahul Sharma,Engineering,Software Engineer,Hyderabad
```

was converted into textual content similar to:

```text
employee_id: 101
name: Rahul Sharma
department: Engineering
role: Software Engineer
location: Hyderabad
```

---

## CSV Metadata

Metadata can contain:

```python
{
    "source": "data/employees.csv",
    "row": 0
}
```

---

# 14. Docx2txtLoader

## Purpose

`Docx2txtLoader` is used to extract text from Microsoft Word `.docx` files.

## Packages

```bash
uv add langchain-community
uv add docx2txt
```

## Import

```python
from langchain_community.document_loaders import Docx2txtLoader
```

## Example

```python
loader = Docx2txtLoader(
    "data/company_policy.docx"
)

documents = loader.load()
```

---

## Workflow

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
 ↓
page_content + metadata
```

---

## Dependency Learning

During practice, the following error occurred:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

The solution was:

```bash
uv add docx2txt
```

This demonstrated the difference between a LangChain loader and its underlying extraction dependency.

---

# 15. JSONLoader

## Purpose

`JSONLoader` is used to load structured JSON data and select required content from the JSON structure.

## Packages

```bash
uv add langchain-community
uv add jq
```

## Import

```python
from langchain_community.document_loaders import JSONLoader
```

## Example

```python
loader = JSONLoader(
    file_path="data/employees.json",
    jq_schema=".[]",
    text_content=False
)

documents = loader.load()
```

---

## jq_schema

JSON can contain nested structures.

Therefore, `JSONLoader` needs to know which part of the JSON should be selected.

Example:

```python
jq_schema=".[]"
```

This selects each element from a JSON array.

---

## Workflow

```text
JSON File
    ↓
JSONLoader
    ↓
Apply jq_schema
    ↓
Select Required JSON Elements
    ↓
Create Document Objects
    ↓
List[Document]
```

---

# 16. WebBaseLoader

## Purpose

`WebBaseLoader` is used to retrieve content from web pages and convert the extracted textual content into LangChain Documents.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add requests
```

## Import

```python
from langchain_community.document_loaders import WebBaseLoader
```

## Example

```python
loader = WebBaseLoader(
    "https://example.com/"
)

documents = loader.load()
```

---

## Workflow

```text
URL
 ↓
WebBaseLoader
 ↓
HTTP Request
 ↓
Receive HTML
 ↓
Parse HTML
 ↓
Extract Text
 ↓
Create Document
 ↓
page_content + metadata
```

---

## Practice Output

The example webpage produced metadata such as:

```python
{
    "source": "https://example.com/",
    "title": "Example Domain",
    "language": "en"
}
```

---

## Production Considerations

A basic webpage loader may not be enough for:

- JavaScript-heavy websites
- Authenticated websites
- Protected pages
- Anti-bot systems
- Dynamically rendered content
- Complex HTML structures

Different ingestion strategies may be required for these scenarios.

---

# 17. BSHTMLLoader

## Purpose

`BSHTMLLoader` is used to load **local HTML files**.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add lxml
```

## Import

```python
from langchain_community.document_loaders import BSHTMLLoader
```

## Example

```python
loader = BSHTMLLoader(
    "data/company_website.html"
)

documents = loader.load()
```

---

## Workflow

```text
Local HTML File
       ↓
BSHTMLLoader
       ↓
BeautifulSoup
       ↓
HTML Parser
       ↓
Parse HTML
       ↓
Extract Text
       ↓
Document
```

---

## WebBaseLoader vs BSHTMLLoader

```text
Web URL
    ↓
WebBaseLoader
```

```text
Local .html File
       ↓
BSHTMLLoader
```

---

## lxml Dependency

During practice, the following error occurred:

```text
BSHTMLLoader uses the 'lxml' package
```

The dependency was installed using:

```bash
uv add lxml
```

---

# 18. UnstructuredLoader

## Purpose

`UnstructuredLoader` uses the Unstructured ecosystem for richer document ingestion and partitioning.

It can be useful when working with heterogeneous or more complex document formats.

## Packages

```bash
uv add langchain-unstructured
uv add unstructured
```

## Import

```python
from langchain_unstructured import UnstructuredLoader
```

## Example

```python
loader = UnstructuredLoader(
    file_path="data/company_policy.txt"
)

documents = loader.load()
```

---

## Workflow

```text
Document
    ↓
UnstructuredLoader
    ↓
Parse
    ↓
Partition
    ↓
Extract Content
    ↓
Document Elements
    ↓
LangChain Documents
```

---

# 19. What Does Parse Mean?

**Parsing means reading data, understanding its structure, and extracting useful information from it.**

Simple memory formula:

```text
Parse
  =
Read
  +
Understand Structure
```

Example:

```html
<h1>Employee Policy</h1>
<p>Employees should work 8 hours.</p>
```

An HTML parser understands:

```text
<h1> → Heading

<p> → Paragraph
```

and can extract the useful textual information.

---

# 20. What Does Partition Mean?

Partitioning means breaking a document into meaningful elements.

For example:

```text
ABC Technologies
```

may be identified as:

```text
Title
```

and:

```text
Employees should work 8 hours.
```

may be identified as:

```text
Narrative Text / Paragraph
```

Conceptually:

```text
Document
   ↓
Partition
   ↓
Title
Paragraph
List
Table
Other Elements
```

---

# 21. UnstructuredLoader Environment Issue

During local Windows practice, Unstructured reached native NLP dependencies such as spaCy.

Windows Application Control blocked native compiled components.

The error was related to:

```text
Application Control policy has blocked this file.
```

This was an environment/security-policy issue rather than an error in the loader logic.

It demonstrated an important production engineering lesson:

> More sophisticated document-processing frameworks can introduce additional dependencies and deployment complexity.

---

# 22. Dedicated Loader vs Unstructured

For a simple text file:

```text
TXT
 ↓
TextLoader
```

is usually simpler.

For heterogeneous or more complex enterprise documents:

```text
PDF
DOCX
HTML
PPTX
Other Documents
       ↓
Unstructured-based Processing
       ↓
Partition / Extract
       ↓
Documents
```

may be useful.

Do not automatically use a complex document-processing framework when a simple dedicated loader is sufficient.

---

# 23. Loader Comparison

| Data Source                       | Loader             | Additional Dependency        |
| --------------------------------- | ------------------ | ---------------------------- |
| TXT                               | TextLoader         | None beyond loader package   |
| Directory                         | DirectoryLoader    | Depends on underlying loader |
| PDF                               | PyPDFLoader        | pypdf                        |
| CSV                               | CSVLoader          | None beyond loader package   |
| DOCX                              | Docx2txtLoader     | docx2txt                     |
| JSON                              | JSONLoader         | jq                           |
| Web URL                           | WebBaseLoader      | beautifulsoup4 / requests    |
| Local HTML                        | BSHTMLLoader       | beautifulsoup4 / lxml        |
| Complex / Heterogeneous Documents | UnstructuredLoader | unstructured                 |

---

# 24. Packages Practiced

The following packages/dependencies were used during Document Loader practice:

```text
langchain-community

pypdf

docx2txt

jq

beautifulsoup4

requests

lxml

langchain-unstructured

unstructured
```

---

# 25. Package vs Class

An important Python dependency concept learned during this practice is the difference between a **package** and a **class**.

For example:

```text
langchain-community
        ↓
document_loaders
        ↓
TextLoader
```

Here:

```text
langchain-community → Package

document_loaders → Module

TextLoader → Class
```

Therefore, we do NOT install:

```bash
uv add TextLoader
```

because `TextLoader` is not a standalone package.

Instead:

```bash
uv add langchain-community
```

Then:

```python
from langchain_community.document_loaders import TextLoader
```

---

## Memory Formula

```text
uv add
   ↓
Install Package / Dependency
```

```text
import
   ↓
Use Class / Function / Module
```

---

# 26. Important Interview Concept — One File Does Not Always Mean One Document

A common incorrect assumption is:

```text
1 File = 1 Document
```

This is not always true.

The number and granularity of Document objects depend on the loader and its loading strategy.

---

## Example 1 — PDF

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

---

## Example 2 — CSV

During practice:

```text
1 CSV
 ↓
8 Data Rows
 ↓
8 Document Objects
```

Therefore:

> The number and granularity of LangChain Document objects depend on the source format, loader, and loading strategy.

---

# 27. Complete Document Loader Workflow

```text
                    RAW DATA
                       │
        ┌──────────────┼──────────────┐
        │              │              │
       TXT            PDF            CSV
        │              │              │
   TextLoader     PyPDFLoader     CSVLoader
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                Document Objects
                       │
              ┌────────┴────────┐
              │                 │
        page_content         metadata
              │                 │
              └────────┬────────┘
                       │
                       ▼
                  Text Splitter
                       │
                       ▼
                     Chunks
                       │
                       ▼
                  Embeddings
                       │
                       ▼
                Vector Database
```

---

# 28. Document Loader Interview Answer

## What is a Document Loader?

A professional interview answer:

> A Document Loader is a component responsible for reading data from different sources such as text files, PDFs, Word documents, CSV files, JSON files, HTML pages, or websites and converting the extracted content into standardized LangChain Document objects. These Document objects typically contain `page_content` for textual content and `metadata` for source-related information. The resulting Documents can then be passed to downstream RAG components such as text splitters, embedding models, and vector databases.

---

# 29. Why Are Document Loaders Important in RAG?

RAG systems may receive knowledge from many different data sources.

Each source has a different format.

For example:

```text
PDF
CSV
DOCX
JSON
HTML
TXT
```

The downstream RAG pipeline should not need completely different representations for every source.

Document loaders help normalize these sources into:

```text
LangChain Document Objects
```

which can then be processed by the rest of the pipeline.

```text
Different Data Sources
        ↓
Different Loaders
        ↓
Standardized Documents
        ↓
Text Splitters
        ↓
Embeddings
        ↓
Vector Database
```

---

# 30. Document Loader Best Practices

## 1. Select the Appropriate Loader

Choose a loader based on the source format and requirements.

Example:

```text
PDF → PyPDFLoader

CSV → CSVLoader
```

---

## 2. Preserve Metadata

Metadata is important for:

- Source tracking
- Citations
- Filtering
- Debugging
- Retrieval analysis

---

## 3. Validate Extracted Content

Never assume successful loading means good extraction.

Check:

```python
document.page_content
```

and:

```python
document.metadata
```

---

## 4. Handle Scanned Documents Properly

A scanned PDF may require OCR rather than standard PDF text extraction.

---

## 5. Avoid Unnecessary Complexity

Use a simple loader when the document is simple.

Do not introduce a complex processing framework unless the use case requires it.

---

# 31. Document Loader Debugging Lessons

Several dependency problems were intentionally encountered and resolved during practice.

## DOCX

Error:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

Solution:

```bash
uv add docx2txt
```

---

## HTML

Error:

```text
BSHTMLLoader uses the 'lxml' package
```

Solution:

```bash
uv add lxml
```

---

## Unstructured

Native dependencies were blocked by Windows Application Control.

Lesson:

```text
Application Code
      ↓
Framework
      ↓
Dependencies
      ↓
Native Libraries
      ↓
Operating System / Security Policy
```

Production debugging requires understanding the entire dependency chain rather than assuming every error comes from application code.

---

# 32. Current Progress

## RAG Fundamentals

- [X] RAG Workflow
- [X] Why RAG
- [X] Indexing / Retrieval / Generation Overview

## Document Loading

- [X] Document Loader Concept
- [X] Document Object Basics
- [X] page_content
- [X] metadata
- [X] TextLoader
- [X] DirectoryLoader
- [X] glob
- [X] loader_cls
- [X] PyPDFLoader
- [X] CSVLoader
- [X] Docx2txtLoader
- [X] JSONLoader
- [X] jq_schema
- [X] WebBaseLoader
- [X] BSHTMLLoader
- [X] UnstructuredLoader Concept
- [X] Parsing Concept
- [X] Partitioning Concept
- [X] Package vs Class
- [X] Dependency Debugging

---

# 33. Next Learning Topics

---

# 34. Future Topics

This repository will continue with:

## Text Splitting

- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- Token-based splitting
- Semantic splitting
- Chunk size
- Chunk overlap
- Separators
- Production chunking strategies

## Embeddings

- What are embeddings?
- Embedding models
- Vector dimensions
- Similarity
- Query embeddings
- Document embeddings
- Batch embedding

## Vector Databases

- Chroma
- Vector storage
- Collections
- Metadata
- Persistence
- Similarity search

## Indexing Pipeline

```text
Documents
 ↓
Load
 ↓
Split
 ↓
Embed
 ↓
Store
```

## Retrieval Pipeline

```text
Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Top-K Documents
 ↓
Context
```

## Basic RAG

```text
Documents
 ↓
Indexing
 ↓
Vector Database

User Question
 ↓
Retrieval
 ↓
Context
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

## Advanced RAG

Future practice will include:

- Multi-Query Retrieval
- Hybrid Search
- Metadata Filtering
- Maximum Marginal Relevance
- Re-ranking
- Contextual Compression
- Parent Document Retrieval
- Query Transformation
- Conversational RAG
- Agentic RAG
- Graph RAG

## Production RAG

Future production topics will include:

- Ingestion pipelines
- Incremental indexing
- Document versioning
- Metadata strategy
- Retrieval evaluation
- RAG evaluation
- Observability
- Caching
- Security
- Access control
- Scalability
- Cost optimization
- Latency optimization
- Production deployment

---

# 35. Repository Goal

The final goal of this repository is to develop a strong understanding of RAG from:

```text
Fundamentals
     ↓
Hands-On Coding
     ↓
Internal Working
     ↓
Interview Preparation
     ↓
Scenario-Based Understanding
     ↓
Production Engineering
```

The focus is not on memorizing LangChain code.

The focus is on understanding:

> **What the component does, why it exists, how it works, when to use it, what can fail, and how it fits into a production RAG architecture.**

---

# 36. Final Document Loader Revision

```text
TXT
 ↓
TextLoader

Directory
 ↓
DirectoryLoader

PDF
 ↓
PyPDFLoader

CSV
 ↓
CSVLoader

DOCX
 ↓
Docx2txtLoader

JSON
 ↓
JSONLoader

Web URL
 ↓
WebBaseLoader

Local HTML
 ↓
BSHTMLLoader

Complex / Heterogeneous Documents
 ↓
UnstructuredLoader
```

All loaders ultimately contribute to the same broader goal:

```text
Raw Knowledge
      ↓
Document Loading
      ↓
LangChain Documents
      ↓
Text Splitting
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
      ↓
Final Answer
```

---

## Author

RAG Interview Practice Repository

Focused on:

- Generative AI
- Retrieval-Augmented Generation
- LangChain
- Vector Databases
- LLM Applications
- Production RAG Engineering
- Technical Interview Preparati

# RAG Interview Practice

## Retrieval-Augmented Generation — Hands-On & Interview Preparation

This repository contains my structured hands-on practice for **Retrieval-Augmented Generation (RAG)**.

The purpose of this repository is not only to write LangChain code, but also to understand:

- Why each RAG component is required
- How each component works internally
- How different components are connected
- What packages and dependencies are required
- How to debug common implementation problems
- How to explain RAG concepts professionally in interviews
- How to make design decisions for real-world RAG applications
- How to move from basic RAG concepts toward production-level RAG systems

---

# 1. What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

RAG is an architecture that improves Large Language Model (LLM) responses by retrieving relevant information from an external knowledge source and providing that information as context to the LLM before generating the final answer.

Instead of depending only on the knowledge learned during model training, RAG allows the application to retrieve relevant information from external sources such as:

- PDF documents
- Text files
- Word documents
- CSV files
- JSON files
- Websites
- Databases
- Vector databases
- Enterprise knowledge bases

---

# 2. Why RAG?

Large Language Models have several limitations when used without external knowledge retrieval.

## Problems

### 1. Knowledge Cutoff

An LLM may not know information created or updated after its training period.

### 2. Private Data

An LLM does not automatically know private organizational information such as:

- Company policies
- Internal documents
- Customer information
- Product documentation
- Enterprise knowledge

### 3. Hallucination

An LLM may generate incorrect or unsupported information when it does not have sufficient context.

### 4. Domain-Specific Knowledge

General-purpose LLMs may not contain enough detailed knowledge about a company's internal or specialized domain.

---

# 3. How RAG Solves These Problems

RAG retrieves relevant information from an external knowledge source and provides that information to the LLM as context.

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Build Context
      ↓
Question + Context
      ↓
LLM
      ↓
Grounded Final Answer
```

This allows the LLM to generate answers based on retrieved information rather than relying only on its internal knowledge.

---

# 4. Three Main Stages of RAG

A RAG system can be understood through three major stages:

```text
1. Indexing
2. Retrieval
3. Generation
```

---

## Stage 1 — Indexing

During indexing, source documents are processed and stored in a searchable representation.

```text
Documents
    ↓
Document Loaders
    ↓
Document Objects
    ↓
Text Splitting
    ↓
Chunks
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Database
```

---

## Stage 2 — Retrieval

When a user asks a question, the system searches for relevant information.

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Vector Database
      ↓
Top-K Relevant Chunks
```

---

## Stage 3 — Generation

The retrieved information is provided to the LLM.

```text
Retrieved Chunks
       +
User Question
       ↓
Build Prompt
       ↓
LLM
       ↓
Final Answer
```

---

# 5. Complete RAG Workflow

```text
Documents
    ↓
Load Documents
    ↓
Document Objects
    ↓
Split Documents into Chunks
    ↓
Generate Embeddings
    ↓
Store Vectors in Vector Database
    ↓
User Asks a Question
    ↓
Generate Query Embedding
    ↓
Similarity Search
    ↓
Retrieve Top-K Relevant Chunks
    ↓
Merge / Prepare Retrieved Context
    ↓
Build Prompt
    ↓
Context + User Question
    ↓
Send to LLM
    ↓
Generate Final Answer
```

---

# 6. Repository Learning Roadmap

```text
RAG Interview Practice
│
├── 01. Document Loaders
├── 02. Document Objects
├── 03. Text Splitters
├── 04. Chunking Strategies
├── 05. Embeddings
├── 06. Vector Databases
├── 07. Indexing Pipeline
├── 08. Retrieval Pipeline
├── 09. Prompt Construction
├── 10. Basic RAG
├── 11. Advanced Retrieval
└── 12. Production RAG
```

---

# 7. Document Loaders

## What is a Document Loader?

A **Document Loader** is a component responsible for reading data from different sources and converting the extracted information into standardized LangChain `Document` objects.

Data can come from:

- TXT files
- PDFs
- CSV files
- Word documents
- JSON files
- HTML files
- Websites
- Other document sources

---

## General Document Loading Workflow

```text
Data Source
    ↓
Document Loader
    ↓
Read / Parse / Extract Content
    ↓
LangChain Document Objects
    ↓
page_content + metadata
```

---

# 8. LangChain Document Object

After loading data, LangChain represents the extracted information using `Document` objects.

A Document mainly contains:

```text
Document
│
├── page_content
│
└── metadata
```

## page_content

Contains the actual extracted textual content.

Example:

```text
Employees should work from 9 AM to 6 PM.
```

## metadata

Contains additional information about the source.

Example:

```python
{
    "source": "data/company_policy.txt"
}
```

Metadata may also contain:

- Page number
- Page label
- Total pages
- Row number
- Source URL
- Document title
- Language
- Other source information

---

# 9. Document Loaders Practiced

The following document loaders were implemented and practiced.

```text
TXT            → TextLoader

Directory      → DirectoryLoader

PDF            → PyPDFLoader

CSV            → CSVLoader

DOCX           → Docx2txtLoader

JSON           → JSONLoader

Web URL        → WebBaseLoader

Local HTML     → BSHTMLLoader

Complex /
Multi-format   → UnstructuredLoader
```

---

# 10. TextLoader

## Purpose

`TextLoader` is used to load plain text (`.txt`) files.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import TextLoader
```

## Example

```python
loader = TextLoader("data/company_policy.txt")

documents = loader.load()
```

## Workflow

```text
TXT File
   ↓
TextLoader
   ↓
Read Text
   ↓
Create Document
   ↓
page_content + metadata
```

## Important Point

A basic text file is generally represented as a Document containing the extracted text and source metadata.

---

# 11. DirectoryLoader

## Purpose

`DirectoryLoader` is used to load multiple files from a directory.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
```

## Example

```python
loader = DirectoryLoader(
    path="data",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()
```

---

## Important Parameters

### path

Specifies where the files are located.

```python
path="data"
```

Means:

```text
Look inside the data directory.
```

---

### glob

Specifies which files should be selected.

```python
glob="*.txt"
```

`*` is a wildcard.

Therefore:

```text
*.txt
```

means:

> Select all files whose names end with `.txt`.

Example:

```text
company_policy.txt     ✓
leave_policy.txt       ✓
employee_handbook.txt  ✓

resume.pdf             ✗
employees.csv          ✗
```

---

### loader_cls

Specifies which loader should read each matching file.

```python
loader_cls=TextLoader
```

Means:

> Use `TextLoader` to read every selected text file.

---

## DirectoryLoader Workflow

```text
Directory
    ↓
DirectoryLoader
    ↓
Find Matching Files
    ↓
glob="*.txt"
    ↓
TextLoader
    ↓
Read Each File
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Interview Summary

`DirectoryLoader` loads multiple files from a directory. It uses a glob pattern to select files and a specified loader class to read each matching file.

---

# 12. PyPDFLoader

## Purpose

`PyPDFLoader` is used to load and extract text from PDF documents.

## Packages

```bash
uv add langchain-community
uv add pypdf
```

## Import

```python
from langchain_community.document_loaders import PyPDFLoader
```

## Example

```python
loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()
```

---

## Workflow

```text
PDF File
    ↓
PyPDFLoader
    ↓
pypdf
    ↓
Parse PDF
    ↓
Extract Page Text
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Important Observation

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

The page-oriented loading behavior created one Document for each page.

---

## PDF Metadata

Metadata can contain:

```text
source
page
page_label
total_pages
producer
creator
creationdate
```

Example:

```python
{
    "source": "data/employee_handbook.pdf",
    "total_pages": 3,
    "page": 0,
    "page_label": "1"
}
```

---

## Important Production Point

Not every PDF contains directly extractable text.

### Text-based PDF

```text
PDF
 ↓
Selectable Text
 ↓
PyPDFLoader
 ↓
Text Extraction
```

### Scanned PDF

```text
Scanned PDF
    ↓
Page contains images
    ↓
Normal text extraction may fail
    ↓
OCR / Vision Processing may be required
```

---

# 13. CSVLoader

## Purpose

`CSVLoader` is used to load structured CSV data.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import CSVLoader
```

## Example

```python
loader = CSVLoader(
    file_path="data/employees.csv"
)

documents = loader.load()
```

---

## Workflow

```text
CSV File
    ↓
CSVLoader
    ↓
Read CSV Rows
    ↓
Process Each Row
    ↓
Create Document
    ↓
List[Document]
```

---

## Practice Observation

The practice CSV contained:

```text
8 Employee Rows
       ↓
8 Document Objects
```

A row such as:

```text
101,Rahul Sharma,Engineering,Software Engineer,Hyderabad
```

was converted into textual content similar to:

```text
employee_id: 101
name: Rahul Sharma
department: Engineering
role: Software Engineer
location: Hyderabad
```

---

## CSV Metadata

Metadata can contain:

```python
{
    "source": "data/employees.csv",
    "row": 0
}
```

---

# 14. Docx2txtLoader

## Purpose

`Docx2txtLoader` is used to extract text from Microsoft Word `.docx` files.

## Packages

```bash
uv add langchain-community
uv add docx2txt
```

## Import

```python
from langchain_community.document_loaders import Docx2txtLoader
```

## Example

```python
loader = Docx2txtLoader(
    "data/company_policy.docx"
)

documents = loader.load()
```

---

## Workflow

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
 ↓
page_content + metadata
```

---

## Dependency Learning

During practice, the following error occurred:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

The solution was:

```bash
uv add docx2txt
```

This demonstrated the difference between a LangChain loader and its underlying extraction dependency.

---

# 15. JSONLoader

## Purpose

`JSONLoader` is used to load structured JSON data and select required content from the JSON structure.

## Packages

```bash
uv add langchain-community
uv add jq
```

## Import

```python
from langchain_community.document_loaders import JSONLoader
```

## Example

```python
loader = JSONLoader(
    file_path="data/employees.json",
    jq_schema=".[]",
    text_content=False
)

documents = loader.load()
```

---

## jq_schema

JSON can contain nested structures.

Therefore, `JSONLoader` needs to know which part of the JSON should be selected.

Example:

```python
jq_schema=".[]"
```

This selects each element from a JSON array.

---

## Workflow

```text
JSON File
    ↓
JSONLoader
    ↓
Apply jq_schema
    ↓
Select Required JSON Elements
    ↓
Create Document Objects
    ↓
List[Document]
```

---

# 16. WebBaseLoader

## Purpose

`WebBaseLoader` is used to retrieve content from web pages and convert the extracted textual content into LangChain Documents.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add requests
```

## Import

```python
from langchain_community.document_loaders import WebBaseLoader
```

## Example

```python
loader = WebBaseLoader(
    "https://example.com/"
)

documents = loader.load()
```

---

## Workflow

```text
URL
 ↓
WebBaseLoader
 ↓
HTTP Request
 ↓
Receive HTML
 ↓
Parse HTML
 ↓
Extract Text
 ↓
Create Document
 ↓
page_content + metadata
```

---

## Practice Output

The example webpage produced metadata such as:

```python
{
    "source": "https://example.com/",
    "title": "Example Domain",
    "language": "en"
}
```

---

## Production Considerations

A basic webpage loader may not be enough for:

- JavaScript-heavy websites
- Authenticated websites
- Protected pages
- Anti-bot systems
- Dynamically rendered content
- Complex HTML structures

Different ingestion strategies may be required for these scenarios.

---

# 17. BSHTMLLoader

## Purpose

`BSHTMLLoader` is used to load **local HTML files**.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add lxml
```

## Import

```python
from langchain_community.document_loaders import BSHTMLLoader
```

## Example

```python
loader = BSHTMLLoader(
    "data/company_website.html"
)

documents = loader.load()
```

---

## Workflow

```text
Local HTML File
       ↓
BSHTMLLoader
       ↓
BeautifulSoup
       ↓
HTML Parser
       ↓
Parse HTML
       ↓
Extract Text
       ↓
Document
```

---

## WebBaseLoader vs BSHTMLLoader

```text
Web URL
    ↓
WebBaseLoader
```

```text
Local .html File
       ↓
BSHTMLLoader
```

---

## lxml Dependency

During practice, the following error occurred:

```text
BSHTMLLoader uses the 'lxml' package
```

The dependency was installed using:

```bash
uv add lxml
```

---

# 18. UnstructuredLoader

## Purpose

`UnstructuredLoader` uses the Unstructured ecosystem for richer document ingestion and partitioning.

It can be useful when working with heterogeneous or more complex document formats.

## Packages

```bash
uv add langchain-unstructured
uv add unstructured
```

## Import

```python
from langchain_unstructured import UnstructuredLoader
```

## Example

```python
loader = UnstructuredLoader(
    file_path="data/company_policy.txt"
)

documents = loader.load()
```

---

## Workflow

```text
Document
    ↓
UnstructuredLoader
    ↓
Parse
    ↓
Partition
    ↓
Extract Content
    ↓
Document Elements
    ↓
LangChain Documents
```

---

# 19. What Does Parse Mean?

**Parsing means reading data, understanding its structure, and extracting useful information from it.**

Simple memory formula:

```text
Parse
  =
Read
  +
Understand Structure
```

Example:

```html
<h1>Employee Policy</h1>
<p>Employees should work 8 hours.</p>
```

An HTML parser understands:

```text
<h1> → Heading

<p> → Paragraph
```

and can extract the useful textual information.

---

# 20. What Does Partition Mean?

Partitioning means breaking a document into meaningful elements.

For example:

```text
ABC Technologies
```

may be identified as:

```text
Title
```

and:

```text
Employees should work 8 hours.
```

may be identified as:

```text
Narrative Text / Paragraph
```

Conceptually:

```text
Document
   ↓
Partition
   ↓
Title
Paragraph
List
Table
Other Elements
```

---

# 21. UnstructuredLoader Environment Issue

During local Windows practice, Unstructured reached native NLP dependencies such as spaCy.

Windows Application Control blocked native compiled components.

The error was related to:

```text
Application Control policy has blocked this file.
```

This was an environment/security-policy issue rather than an error in the loader logic.

It demonstrated an important production engineering lesson:

> More sophisticated document-processing frameworks can introduce additional dependencies and deployment complexity.

---

# 22. Dedicated Loader vs Unstructured

For a simple text file:

```text
TXT
 ↓
TextLoader
```

is usually simpler.

For heterogeneous or more complex enterprise documents:

```text
PDF
DOCX
HTML
PPTX
Other Documents
       ↓
Unstructured-based Processing
       ↓
Partition / Extract
       ↓
Documents
```

may be useful.

Do not automatically use a complex document-processing framework when a simple dedicated loader is sufficient.

---

# 23. Loader Comparison

| Data Source                       | Loader             | Additional Dependency        |
| --------------------------------- | ------------------ | ---------------------------- |
| TXT                               | TextLoader         | None beyond loader package   |
| Directory                         | DirectoryLoader    | Depends on underlying loader |
| PDF                               | PyPDFLoader        | pypdf                        |
| CSV                               | CSVLoader          | None beyond loader package   |
| DOCX                              | Docx2txtLoader     | docx2txt                     |
| JSON                              | JSONLoader         | jq                           |
| Web URL                           | WebBaseLoader      | beautifulsoup4 / requests    |
| Local HTML                        | BSHTMLLoader       | beautifulsoup4 / lxml        |
| Complex / Heterogeneous Documents | UnstructuredLoader | unstructured                 |

---

# 24. Packages Practiced

The following packages/dependencies were used during Document Loader practice:

```text
langchain-community

pypdf

docx2txt

jq

beautifulsoup4

requests

lxml

langchain-unstructured

unstructured
```

---

# 25. Package vs Class

An important Python dependency concept learned during this practice is the difference between a **package** and a **class**.

For example:

```text
langchain-community
        ↓
document_loaders
        ↓
TextLoader
```

Here:

```text
langchain-community → Package

document_loaders → Module

TextLoader → Class
```

Therefore, we do NOT install:

```bash
uv add TextLoader
```

because `TextLoader` is not a standalone package.

Instead:

```bash
uv add langchain-community
```

Then:

```python
from langchain_community.document_loaders import TextLoader
```

---

## Memory Formula

```text
uv add
   ↓
Install Package / Dependency
```

```text
import
   ↓
Use Class / Function / Module
```

---

# 26. Important Interview Concept — One File Does Not Always Mean One Document

A common incorrect assumption is:

```text
1 File = 1 Document
```

This is not always true.

The number and granularity of Document objects depend on the loader and its loading strategy.

---

## Example 1 — PDF

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

---

## Example 2 — CSV

During practice:

```text
1 CSV
 ↓
8 Data Rows
 ↓
8 Document Objects
```

Therefore:

> The number and granularity of LangChain Document objects depend on the source format, loader, and loading strategy.

---

# 27. Complete Document Loader Workflow

```text
                    RAW DATA
                       │
        ┌──────────────┼──────────────┐
        │              │              │
       TXT            PDF            CSV
        │              │              │
   TextLoader     PyPDFLoader     CSVLoader
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                Document Objects
                       │
              ┌────────┴────────┐
              │                 │
        page_content         metadata
              │                 │
              └────────┬────────┘
                       │
                       ▼
                  Text Splitter
                       │
                       ▼
                     Chunks
                       │
                       ▼
                  Embeddings
                       │
                       ▼
                Vector Database
```

---

# 28. Document Loader Interview Answer

## What is a Document Loader?

A professional interview answer:

> A Document Loader is a component responsible for reading data from different sources such as text files, PDFs, Word documents, CSV files, JSON files, HTML pages, or websites and converting the extracted content into standardized LangChain Document objects. These Document objects typically contain `page_content` for textual content and `metadata` for source-related information. The resulting Documents can then be passed to downstream RAG components such as text splitters, embedding models, and vector databases.

---

# 29. Why Are Document Loaders Important in RAG?

RAG systems may receive knowledge from many different data sources.

Each source has a different format.

For example:

```text
PDF
CSV
DOCX
JSON
HTML
TXT
```

The downstream RAG pipeline should not need completely different representations for every source.

Document loaders help normalize these sources into:

```text
LangChain Document Objects
```

which can then be processed by the rest of the pipeline.

```text
Different Data Sources
        ↓
Different Loaders
        ↓
Standardized Documents
        ↓
Text Splitters
        ↓
Embeddings
        ↓
Vector Database
```

---

# 30. Document Loader Best Practices

## 1. Select the Appropriate Loader

Choose a loader based on the source format and requirements.

Example:

```text
PDF → PyPDFLoader

CSV → CSVLoader
```

---

## 2. Preserve Metadata

Metadata is important for:

- Source tracking
- Citations
- Filtering
- Debugging
- Retrieval analysis

---

## 3. Validate Extracted Content

Never assume successful loading means good extraction.

Check:

```python
document.page_content
```

and:

```python
document.metadata
```

---

## 4. Handle Scanned Documents Properly

A scanned PDF may require OCR rather than standard PDF text extraction.

---

## 5. Avoid Unnecessary Complexity

Use a simple loader when the document is simple.

Do not introduce a complex processing framework unless the use case requires it.

---

# 31. Document Loader Debugging Lessons

Several dependency problems were intentionally encountered and resolved during practice.

## DOCX

Error:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

Solution:

```bash
uv add docx2txt
```

---

## HTML

Error:

```text
BSHTMLLoader uses the 'lxml' package
```

Solution:

```bash
uv add lxml
```

---

## Unstructured

Native dependencies were blocked by Windows Application Control.

Lesson:

```text
Application Code
      ↓
Framework
      ↓
Dependencies
      ↓
Native Libraries
      ↓
Operating System / Security Policy
```

Production debugging requires understanding the entire dependency chain rather than assuming every error comes from application code.

---

# 32. Current Progress

## RAG Fundamentals

- [X] RAG Workflow
- [X] Why RAG
- [X] Indexing / Retrieval / Generation Overview

## Document Loading

- [X] Document Loader Concept
- [X] Document Object Basics
- [X] page_content
- [X] metadata
- [X] TextLoader
- [X] DirectoryLoader
- [X] glob
- [X] loader_cls
- [X] PyPDFLoader
- [X] CSVLoader
- [X] Docx2txtLoader
- [X] JSONLoader
- [X] jq_schema
- [X] WebBaseLoader
- [X] BSHTMLLoader
- [X] UnstructuredLoader Concept
- [X] Parsing Concept
- [X] Partitioning Concept
- [X] Package vs Class
- [X] Dependency Debugging

---

# 33. Next Learning Topics

```text
✅ Document Loading
        ↓
⬜ Document Objects — Deep Dive
        ↓
⬜ Text Splitters
        ↓
⬜ Chunking Strategies
        ↓
⬜ Embeddings
        ↓
⬜ Vector Databases
        ↓
⬜ Indexing Pipeline
        ↓
⬜ Retrieval Pipeline
        ↓
⬜ Prompt Construction
        ↓
⬜ Basic RAG
        ↓
⬜ Advanced Retrieval
        ↓
⬜ Production RAG
```

---

# 34. Future Topics

This repository will continue with:

## Text Splitting

- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- Token-based splitting
- Semantic splitting
- Chunk size
- Chunk overlap
- Separators
- Production chunking strategies

## Embeddings

- What are embeddings?
- Embedding models
- Vector dimensions
- Similarity
- Query embeddings
- Document embeddings
- Batch embedding

## Vector Databases

- Chroma
- Vector storage
- Collections
- Metadata
- Persistence
- Similarity search

## Indexing Pipeline

```text
Documents
 ↓
Load
 ↓
Split
 ↓
Embed
 ↓
Store
```

## Retrieval Pipeline

```text
Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Top-K Documents
 ↓
Context
```

## Basic RAG

```text
Documents
 ↓
Indexing
 ↓
Vector Database

User Question
 ↓
Retrieval
 ↓
Context
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

## Advanced RAG

Future practice will include:

- Multi-Query Retrieval
- Hybrid Search
- Metadata Filtering
- Maximum Marginal Relevance
- Re-ranking
- Contextual Compression
- Parent Document Retrieval
- Query Transformation
- Conversational RAG
- Agentic RAG
- Graph RAG

## Production RAG

Future production topics will include:

- Ingestion pipelines
- Incremental indexing
- Document versioning
- Metadata strategy
- Retrieval evaluation
- RAG evaluation
- Observability
- Caching
- Security
- Access control
- Scalability
- Cost optimization
- Latency optimization
- Production deployment

---

# 35. Repository Goal

The final goal of this repository is to develop a strong understanding of RAG from:

```text
Fundamentals
     ↓
Hands-On Coding
     ↓
Internal Working
     ↓
Interview Preparation
     ↓
Scenario-Based Understanding
     ↓
Production Engineering
```

The focus is not on memorizing LangChain code.

The focus is on understanding:

> **What the component does, why it exists, how it works, when to use it, what can fail, and how it fits into a production RAG architecture.**

---

# 36. Final Document Loader Revision

```text
TXT
 ↓
TextLoader

Directory
 ↓
DirectoryLoader

PDF
 ↓
PyPDFLoader

CSV
 ↓
CSVLoader

DOCX
 ↓
Docx2txtLoader

JSON
 ↓
JSONLoader

Web URL
 ↓
WebBaseLoader

Local HTML
 ↓
BSHTMLLoader

Complex / Heterogeneous Documents
 ↓
UnstructuredLoader
```

All loaders ultimately contribute to the same broader goal:

```text
Raw Knowledge
      ↓
Document Loading
      ↓
LangChain Documents
      ↓
Text Splitting
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
      ↓
Final Answer
```

---

## Author

RAG Interview Practice Repository

Focused on:

- Generative AI
- Retrieval-Augmented Generation
- LangChain
- Vector Databases
- LLM Applications
- Production RAG Engineering
- Technical Interview Preparation

# RAG Interview Practice

## Retrieval-Augmented Generation — Hands-On & Interview Preparation

This repository contains my structured hands-on practice for **Retrieval-Augmented Generation (RAG)**.

The purpose of this repository is not only to write LangChain code, but also to understand:

- Why each RAG component is required
- How each component works internally
- How different components are connected
- What packages and dependencies are required
- How to debug common implementation problems
- How to explain RAG concepts professionally in interviews
- How to make design decisions for real-world RAG applications
- How to move from basic RAG concepts toward production-level RAG systems

---

# 1. What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

RAG is an architecture that improves Large Language Model (LLM) responses by retrieving relevant information from an external knowledge source and providing that information as context to the LLM before generating the final answer.

Instead of depending only on the knowledge learned during model training, RAG allows the application to retrieve relevant information from external sources such as:

- PDF documents
- Text files
- Word documents
- CSV files
- JSON files
- Websites
- Databases
- Vector databases
- Enterprise knowledge bases

---

# 2. Why RAG?

Large Language Models have several limitations when used without external knowledge retrieval.

## Problems

### 1. Knowledge Cutoff

An LLM may not know information created or updated after its training period.

### 2. Private Data

An LLM does not automatically know private organizational information such as:

- Company policies
- Internal documents
- Customer information
- Product documentation
- Enterprise knowledge

### 3. Hallucination

An LLM may generate incorrect or unsupported information when it does not have sufficient context.

### 4. Domain-Specific Knowledge

General-purpose LLMs may not contain enough detailed knowledge about a company's internal or specialized domain.

---

# 3. How RAG Solves These Problems

RAG retrieves relevant information from an external knowledge source and provides that information to the LLM as context.

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Build Context
      ↓
Question + Context
      ↓
LLM
      ↓
Grounded Final Answer
```

This allows the LLM to generate answers based on retrieved information rather than relying only on its internal knowledge.

---

# 4. Three Main Stages of RAG

A RAG system can be understood through three major stages:

```text
1. Indexing
2. Retrieval
3. Generation
```

---

## Stage 1 — Indexing

During indexing, source documents are processed and stored in a searchable representation.

```text
Documents
    ↓
Document Loaders
    ↓
Document Objects
    ↓
Text Splitting
    ↓
Chunks
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Database
```

---

## Stage 2 — Retrieval

When a user asks a question, the system searches for relevant information.

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Vector Database
      ↓
Top-K Relevant Chunks
```

---

## Stage 3 — Generation

The retrieved information is provided to the LLM.

```text
Retrieved Chunks
       +
User Question
       ↓
Build Prompt
       ↓
LLM
       ↓
Final Answer
```

---

# 5. Complete RAG Workflow

```text
Documents
    ↓
Load Documents
    ↓
Document Objects
    ↓
Split Documents into Chunks
    ↓
Generate Embeddings
    ↓
Store Vectors in Vector Database
    ↓
User Asks a Question
    ↓
Generate Query Embedding
    ↓
Similarity Search
    ↓
Retrieve Top-K Relevant Chunks
    ↓
Merge / Prepare Retrieved Context
    ↓
Build Prompt
    ↓
Context + User Question
    ↓
Send to LLM
    ↓
Generate Final Answer
```

---

# 6. Repository Learning Roadmap

```text
RAG Interview Practice
│
├── 01. Document Loaders
├── 02. Document Objects
├── 03. Text Splitters
├── 04. Chunking Strategies
├── 05. Embeddings
├── 06. Vector Databases
├── 07. Indexing Pipeline
├── 08. Retrieval Pipeline
├── 09. Prompt Construction
├── 10. Basic RAG
├── 11. Advanced Retrieval
└── 12. Production RAG
```

---

# 7. Document Loaders

## What is a Document Loader?

A **Document Loader** is a component responsible for reading data from different sources and converting the extracted information into standardized LangChain `Document` objects.

Data can come from:

- TXT files
- PDFs
- CSV files
- Word documents
- JSON files
- HTML files
- Websites
- Other document sources

---

## General Document Loading Workflow

```text
Data Source
    ↓
Document Loader
    ↓
Read / Parse / Extract Content
    ↓
LangChain Document Objects
    ↓
page_content + metadata
```

---

# 8. LangChain Document Object

After loading data, LangChain represents the extracted information using `Document` objects.

A Document mainly contains:

```text
Document
│
├── page_content
│
└── metadata
```

## page_content

Contains the actual extracted textual content.

Example:

```text
Employees should work from 9 AM to 6 PM.
```

## metadata

Contains additional information about the source.

Example:

```python
{
    "source": "data/company_policy.txt"
}
```

Metadata may also contain:

- Page number
- Page label
- Total pages
- Row number
- Source URL
- Document title
- Language
- Other source information

---

# 9. Document Loaders Practiced

The following document loaders were implemented and practiced.

```text
TXT            → TextLoader

Directory      → DirectoryLoader

PDF            → PyPDFLoader

CSV            → CSVLoader

DOCX           → Docx2txtLoader

JSON           → JSONLoader

Web URL        → WebBaseLoader

Local HTML     → BSHTMLLoader

Complex /
Multi-format   → UnstructuredLoader
```

---

# 10. TextLoader

## Purpose

`TextLoader` is used to load plain text (`.txt`) files.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import TextLoader
```

## Example

```python
loader = TextLoader("data/company_policy.txt")

documents = loader.load()
```

## Workflow

```text
TXT File
   ↓
TextLoader
   ↓
Read Text
   ↓
Create Document
   ↓
page_content + metadata
```

## Important Point

A basic text file is generally represented as a Document containing the extracted text and source metadata.

---

# 11. DirectoryLoader

## Purpose

`DirectoryLoader` is used to load multiple files from a directory.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
```

## Example

```python
loader = DirectoryLoader(
    path="data",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()
```

---

## Important Parameters

### path

Specifies where the files are located.

```python
path="data"
```

Means:

```text
Look inside the data directory.
```

---

### glob

Specifies which files should be selected.

```python
glob="*.txt"
```

`*` is a wildcard.

Therefore:

```text
*.txt
```

means:

> Select all files whose names end with `.txt`.

Example:

```text
company_policy.txt     ✓
leave_policy.txt       ✓
employee_handbook.txt  ✓

resume.pdf             ✗
employees.csv          ✗
```

---

### loader_cls

Specifies which loader should read each matching file.

```python
loader_cls=TextLoader
```

Means:

> Use `TextLoader` to read every selected text file.

---

## DirectoryLoader Workflow

```text
Directory
    ↓
DirectoryLoader
    ↓
Find Matching Files
    ↓
glob="*.txt"
    ↓
TextLoader
    ↓
Read Each File
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Interview Summary

`DirectoryLoader` loads multiple files from a directory. It uses a glob pattern to select files and a specified loader class to read each matching file.

---

# 12. PyPDFLoader

## Purpose

`PyPDFLoader` is used to load and extract text from PDF documents.

## Packages

```bash
uv add langchain-community
uv add pypdf
```

## Import

```python
from langchain_community.document_loaders import PyPDFLoader
```

## Example

```python
loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()
```

---

## Workflow

```text
PDF File
    ↓
PyPDFLoader
    ↓
pypdf
    ↓
Parse PDF
    ↓
Extract Page Text
    ↓
Create Document Objects
    ↓
List[Document]
```

---

## Important Observation

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

The page-oriented loading behavior created one Document for each page.

---

## PDF Metadata

Metadata can contain:

```text
source
page
page_label
total_pages
producer
creator
creationdate
```

Example:

```python
{
    "source": "data/employee_handbook.pdf",
    "total_pages": 3,
    "page": 0,
    "page_label": "1"
}
```

---

## Important Production Point

Not every PDF contains directly extractable text.

### Text-based PDF

```text
PDF
 ↓
Selectable Text
 ↓
PyPDFLoader
 ↓
Text Extraction
```

### Scanned PDF

```text
Scanned PDF
    ↓
Page contains images
    ↓
Normal text extraction may fail
    ↓
OCR / Vision Processing may be required
```

---

# 13. CSVLoader

## Purpose

`CSVLoader` is used to load structured CSV data.

## Package

```bash
uv add langchain-community
```

## Import

```python
from langchain_community.document_loaders import CSVLoader
```

## Example

```python
loader = CSVLoader(
    file_path="data/employees.csv"
)

documents = loader.load()
```

---

## Workflow

```text
CSV File
    ↓
CSVLoader
    ↓
Read CSV Rows
    ↓
Process Each Row
    ↓
Create Document
    ↓
List[Document]
```

---

## Practice Observation

The practice CSV contained:

```text
8 Employee Rows
       ↓
8 Document Objects
```

A row such as:

```text
101,Rahul Sharma,Engineering,Software Engineer,Hyderabad
```

was converted into textual content similar to:

```text
employee_id: 101
name: Rahul Sharma
department: Engineering
role: Software Engineer
location: Hyderabad
```

---

## CSV Metadata

Metadata can contain:

```python
{
    "source": "data/employees.csv",
    "row": 0
}
```

---

# 14. Docx2txtLoader

## Purpose

`Docx2txtLoader` is used to extract text from Microsoft Word `.docx` files.

## Packages

```bash
uv add langchain-community
uv add docx2txt
```

## Import

```python
from langchain_community.document_loaders import Docx2txtLoader
```

## Example

```python
loader = Docx2txtLoader(
    "data/company_policy.docx"
)

documents = loader.load()
```

---

## Workflow

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
 ↓
page_content + metadata
```

---

## Dependency Learning

During practice, the following error occurred:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

The solution was:

```bash
uv add docx2txt
```

This demonstrated the difference between a LangChain loader and its underlying extraction dependency.

---

# 15. JSONLoader

## Purpose

`JSONLoader` is used to load structured JSON data and select required content from the JSON structure.

## Packages

```bash
uv add langchain-community
uv add jq
```

## Import

```python
from langchain_community.document_loaders import JSONLoader
```

## Example

```python
loader = JSONLoader(
    file_path="data/employees.json",
    jq_schema=".[]",
    text_content=False
)

documents = loader.load()
```

---

## jq_schema

JSON can contain nested structures.

Therefore, `JSONLoader` needs to know which part of the JSON should be selected.

Example:

```python
jq_schema=".[]"
```

This selects each element from a JSON array.

---

## Workflow

```text
JSON File
    ↓
JSONLoader
    ↓
Apply jq_schema
    ↓
Select Required JSON Elements
    ↓
Create Document Objects
    ↓
List[Document]
```

---

# 16. WebBaseLoader

## Purpose

`WebBaseLoader` is used to retrieve content from web pages and convert the extracted textual content into LangChain Documents.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add requests
```

## Import

```python
from langchain_community.document_loaders import WebBaseLoader
```

## Example

```python
loader = WebBaseLoader(
    "https://example.com/"
)

documents = loader.load()
```

---

## Workflow

```text
URL
 ↓
WebBaseLoader
 ↓
HTTP Request
 ↓
Receive HTML
 ↓
Parse HTML
 ↓
Extract Text
 ↓
Create Document
 ↓
page_content + metadata
```

---

## Practice Output

The example webpage produced metadata such as:

```python
{
    "source": "https://example.com/",
    "title": "Example Domain",
    "language": "en"
}
```

---

## Production Considerations

A basic webpage loader may not be enough for:

- JavaScript-heavy websites
- Authenticated websites
- Protected pages
- Anti-bot systems
- Dynamically rendered content
- Complex HTML structures

Different ingestion strategies may be required for these scenarios.

---

# 17. BSHTMLLoader

## Purpose

`BSHTMLLoader` is used to load **local HTML files**.

## Packages

```bash
uv add langchain-community
uv add beautifulsoup4
uv add lxml
```

## Import

```python
from langchain_community.document_loaders import BSHTMLLoader
```

## Example

```python
loader = BSHTMLLoader(
    "data/company_website.html"
)

documents = loader.load()
```

---

## Workflow

```text
Local HTML File
       ↓
BSHTMLLoader
       ↓
BeautifulSoup
       ↓
HTML Parser
       ↓
Parse HTML
       ↓
Extract Text
       ↓
Document
```

---

## WebBaseLoader vs BSHTMLLoader

```text
Web URL
    ↓
WebBaseLoader
```

```text
Local .html File
       ↓
BSHTMLLoader
```

---

## lxml Dependency

During practice, the following error occurred:

```text
BSHTMLLoader uses the 'lxml' package
```

The dependency was installed using:

```bash
uv add lxml
```

---

# 18. UnstructuredLoader

## Purpose

`UnstructuredLoader` uses the Unstructured ecosystem for richer document ingestion and partitioning.

It can be useful when working with heterogeneous or more complex document formats.

## Packages

```bash
uv add langchain-unstructured
uv add unstructured
```

## Import

```python
from langchain_unstructured import UnstructuredLoader
```

## Example

```python
loader = UnstructuredLoader(
    file_path="data/company_policy.txt"
)

documents = loader.load()
```

---

## Workflow

```text
Document
    ↓
UnstructuredLoader
    ↓
Parse
    ↓
Partition
    ↓
Extract Content
    ↓
Document Elements
    ↓
LangChain Documents
```

---

# 19. What Does Parse Mean?

**Parsing means reading data, understanding its structure, and extracting useful information from it.**

Simple memory formula:

```text
Parse
  =
Read
  +
Understand Structure
```

Example:

```html
<h1>Employee Policy</h1>
<p>Employees should work 8 hours.</p>
```

An HTML parser understands:

```text
<h1> → Heading

<p> → Paragraph
```

and can extract the useful textual information.

---

# 20. What Does Partition Mean?

Partitioning means breaking a document into meaningful elements.

For example:

```text
ABC Technologies
```

may be identified as:

```text
Title
```

and:

```text
Employees should work 8 hours.
```

may be identified as:

```text
Narrative Text / Paragraph
```

Conceptually:

```text
Document
   ↓
Partition
   ↓
Title
Paragraph
List
Table
Other Elements
```

---

# 21. UnstructuredLoader Environment Issue

During local Windows practice, Unstructured reached native NLP dependencies such as spaCy.

Windows Application Control blocked native compiled components.

The error was related to:

```text
Application Control policy has blocked this file.
```

This was an environment/security-policy issue rather than an error in the loader logic.

It demonstrated an important production engineering lesson:

> More sophisticated document-processing frameworks can introduce additional dependencies and deployment complexity.

---

# 22. Dedicated Loader vs Unstructured

For a simple text file:

```text
TXT
 ↓
TextLoader
```

is usually simpler.

For heterogeneous or more complex enterprise documents:

```text
PDF
DOCX
HTML
PPTX
Other Documents
       ↓
Unstructured-based Processing
       ↓
Partition / Extract
       ↓
Documents
```

may be useful.

Do not automatically use a complex document-processing framework when a simple dedicated loader is sufficient.

---

# 23. Loader Comparison

| Data Source                       | Loader             | Additional Dependency        |
| --------------------------------- | ------------------ | ---------------------------- |
| TXT                               | TextLoader         | None beyond loader package   |
| Directory                         | DirectoryLoader    | Depends on underlying loader |
| PDF                               | PyPDFLoader        | pypdf                        |
| CSV                               | CSVLoader          | None beyond loader package   |
| DOCX                              | Docx2txtLoader     | docx2txt                     |
| JSON                              | JSONLoader         | jq                           |
| Web URL                           | WebBaseLoader      | beautifulsoup4 / requests    |
| Local HTML                        | BSHTMLLoader       | beautifulsoup4 / lxml        |
| Complex / Heterogeneous Documents | UnstructuredLoader | unstructured                 |

---

# 24. Packages Practiced

The following packages/dependencies were used during Document Loader practice:

```text
langchain-community

pypdf

docx2txt

jq

beautifulsoup4

requests

lxml

langchain-unstructured

unstructured
```

---

# 25. Package vs Class

An important Python dependency concept learned during this practice is the difference between a **package** and a **class**.

For example:

```text
langchain-community
        ↓
document_loaders
        ↓
TextLoader
```

Here:

```text
langchain-community → Package

document_loaders → Module

TextLoader → Class
```

Therefore, we do NOT install:

```bash
uv add TextLoader
```

because `TextLoader` is not a standalone package.

Instead:

```bash
uv add langchain-community
```

Then:

```python
from langchain_community.document_loaders import TextLoader
```

---

## Memory Formula

```text
uv add
   ↓
Install Package / Dependency
```

```text
import
   ↓
Use Class / Function / Module
```

---

# 26. Important Interview Concept — One File Does Not Always Mean One Document

A common incorrect assumption is:

```text
1 File = 1 Document
```

This is not always true.

The number and granularity of Document objects depend on the loader and its loading strategy.

---

## Example 1 — PDF

During practice:

```text
1 PDF
 ↓
3 Pages
 ↓
3 Document Objects
```

---

## Example 2 — CSV

During practice:

```text
1 CSV
 ↓
8 Data Rows
 ↓
8 Document Objects
```

Therefore:

> The number and granularity of LangChain Document objects depend on the source format, loader, and loading strategy.

---

# 27. Complete Document Loader Workflow

```text
                    RAW DATA
                       │
        ┌──────────────┼──────────────┐
        │              │              │
       TXT            PDF            CSV
        │              │              │
   TextLoader     PyPDFLoader     CSVLoader
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                Document Objects
                       │
              ┌────────┴────────┐
              │                 │
        page_content         metadata
              │                 │
              └────────┬────────┘
                       │
                       ▼
                  Text Splitter
                       │
                       ▼
                     Chunks
                       │
                       ▼
                  Embeddings
                       │
                       ▼
                Vector Database
```

---

# 28. Document Loader Interview Answer

## What is a Document Loader?

A professional interview answer:

> A Document Loader is a component responsible for reading data from different sources such as text files, PDFs, Word documents, CSV files, JSON files, HTML pages, or websites and converting the extracted content into standardized LangChain Document objects. These Document objects typically contain `page_content` for textual content and `metadata` for source-related information. The resulting Documents can then be passed to downstream RAG components such as text splitters, embedding models, and vector databases.

---

# 29. Why Are Document Loaders Important in RAG?

RAG systems may receive knowledge from many different data sources.

Each source has a different format.

For example:

```text
PDF
CSV
DOCX
JSON
HTML
TXT
```

The downstream RAG pipeline should not need completely different representations for every source.

Document loaders help normalize these sources into:

```text
LangChain Document Objects
```

which can then be processed by the rest of the pipeline.

```text
Different Data Sources
        ↓
Different Loaders
        ↓
Standardized Documents
        ↓
Text Splitters
        ↓
Embeddings
        ↓
Vector Database
```

---

# 30. Document Loader Best Practices

## 1. Select the Appropriate Loader

Choose a loader based on the source format and requirements.

Example:

```text
PDF → PyPDFLoader

CSV → CSVLoader
```

---

## 2. Preserve Metadata

Metadata is important for:

- Source tracking
- Citations
- Filtering
- Debugging
- Retrieval analysis

---

## 3. Validate Extracted Content

Never assume successful loading means good extraction.

Check:

```python
document.page_content
```

and:

```python
document.metadata
```

---

## 4. Handle Scanned Documents Properly

A scanned PDF may require OCR rather than standard PDF text extraction.

---

## 5. Avoid Unnecessary Complexity

Use a simple loader when the document is simple.

Do not introduce a complex processing framework unless the use case requires it.

---

# 31. Document Loader Debugging Lessons

Several dependency problems were intentionally encountered and resolved during practice.

## DOCX

Error:

```text
ModuleNotFoundError: No module named 'docx2txt'
```

Solution:

```bash
uv add docx2txt
```

---

## HTML

Error:

```text
BSHTMLLoader uses the 'lxml' package
```

Solution:

```bash
uv add lxml
```

---

## Unstructured

Native dependencies were blocked by Windows Application Control.

Lesson:

```text
Application Code
      ↓
Framework
      ↓
Dependencies
      ↓
Native Libraries
      ↓
Operating System / Security Policy
```

Production debugging requires understanding the entire dependency chain rather than assuming every error comes from application code.

---

# 32. Current Progress

## RAG Fundamentals

- [X] RAG Workflow
- [X] Why RAG
- [X] Indexing / Retrieval / Generation Overview

## Document Loading

- [X] Document Loader Concept
- [X] Document Object Basics
- [X] page_content
- [X] metadata
- [X] TextLoader
- [X] DirectoryLoader
- [X] glob
- [X] loader_cls
- [X] PyPDFLoader
- [X] CSVLoader
- [X] Docx2txtLoader
- [X] JSONLoader
- [X] jq_schema
- [X] WebBaseLoader
- [X] BSHTMLLoader
- [X] UnstructuredLoader Concept
- [X] Parsing Concept
- [X] Partitioning Concept
- [X] Package vs Class
- [X] Dependency Debugging

---

# 33. Next Learning Topics

```text
✅ Document Loading
        ↓
⬜ Document Objects — Deep Dive
        ↓
⬜ Text Splitters
        ↓
⬜ Chunking Strategies
        ↓
⬜ Embeddings
        ↓
⬜ Vector Databases
        ↓
⬜ Indexing Pipeline
        ↓
⬜ Retrieval Pipeline
        ↓
⬜ Prompt Construction
        ↓
⬜ Basic RAG
        ↓
⬜ Advanced Retrieval
        ↓
⬜ Production RAG
```

---

# 34. Future Topics

This repository will continue with:

## Text Splitting

- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- Token-based splitting
- Semantic splitting
- Chunk size
- Chunk overlap
- Separators
- Production chunking strategies

## Embeddings

- What are embeddings?
- Embedding models
- Vector dimensions
- Similarity
- Query embeddings
- Document embeddings
- Batch embedding

## Vector Databases

- Chroma
- Vector storage
- Collections
- Metadata
- Persistence
- Similarity search

## Indexing Pipeline

```text
Documents
 ↓
Load
 ↓
Split
 ↓
Embed
 ↓
Store
```

## Retrieval Pipeline

```text
Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Top-K Documents
 ↓
Context
```

## Basic RAG

```text
Documents
 ↓
Indexing
 ↓
Vector Database

User Question
 ↓
Retrieval
 ↓
Context
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

## Advanced RAG

Future practice will include:

- Multi-Query Retrieval
- Hybrid Search
- Metadata Filtering
- Maximum Marginal Relevance
- Re-ranking
- Contextual Compression
- Parent Document Retrieval
- Query Transformation
- Conversational RAG
- Agentic RAG
- Graph RAG

## Production RAG

Future production topics will include:

- Ingestion pipelines
- Incremental indexing
- Document versioning
- Metadata strategy
- Retrieval evaluation
- RAG evaluation
- Observability
- Caching
- Security
- Access control
- Scalability
- Cost optimization
- Latency optimization
- Production deployment

---

# 35. Repository Goal

The final goal of this repository is to develop a strong understanding of RAG from:

```text
Fundamentals
     ↓
Hands-On Coding
     ↓
Internal Working
     ↓
Interview Preparation
     ↓
Scenario-Based Understanding
     ↓
Production Engineering
```

The focus is not on memorizing LangChain code.

The focus is on understanding:

> **What the component does, why it exists, how it works, when to use it, what can fail, and how it fits into a production RAG architecture.**

---

# 36. Final Document Loader Revision

```text
TXT
 ↓
TextLoader

Directory
 ↓
DirectoryLoader

PDF
 ↓
PyPDFLoader

CSV
 ↓
CSVLoader

DOCX
 ↓
Docx2txtLoader

JSON
 ↓
JSONLoader

Web URL
 ↓
WebBaseLoader

Local HTML
 ↓
BSHTMLLoader

Complex / Heterogeneous Documents
 ↓
UnstructuredLoader
```

All loaders ultimately contribute to the same broader goal:

```text
Raw Knowledge
      ↓
Document Loading
      ↓
LangChain Documents
      ↓
Text Splitting
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
      ↓
Final Answer
```

---

## Author

RAG Interview Practice Repository

Focused on:

- Generative AI
- Retrieval-Augmented Generation
- LangChain
- Vector Databases
- LLM Applications
- Production RAG Engineering
