
# 05 - Embeddings

## Overview

This module covers the fundamentals of **Embeddings** in Generative AI and Retrieval-Augmented Generation (RAG).

Embeddings convert text into numerical vectors that preserve semantic meaning. These vectors enable semantic search, similarity comparison, document retrieval, and many other AI applications.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand what embeddings are.
- Generate embeddings using Google Gemini.
- Compare embeddings using cosine similarity.
- Perform similarity search.
- Store metadata with embeddings.
- Build a complete embedding pipeline.
- Prepare for embedding-related interview questions.

---

# Folder Structure

```text
05_embeddings/
│
├── 01_google_embeddings/
│   ├── 01_embed_query.py
│   ├── 02_embed_documents.py
│   ├── 03_vector_dimension.py
│   └── 04_return_types.py
│
├── 02_similarity_search/
│   ├── 01_generate_embeddings.py
│   ├── 02_compare_embeddings.py
│   └── 03_top_k_search.py
│
├── 03_metadata_with_embeddings/
│   ├── 01_metadata.py
│   ├── 02_store_metadata.py
│   ├── 03_filter_metadata.py
│   └── 04_metadata_pipeline.py
│
└── README.md
```

---

# Topics Covered

## 1. Google Embeddings

Learned:

- embed_query()
- embed_documents()
- Vector Dimensions
- Return Types

Concepts:

- Embedding Model
- Query Embeddings
- Document Embeddings
- Dense Vectors

---

## 2. Similarity Search

Learned:

- Generate document embeddings
- Generate query embedding
- Cosine Similarity
- Compare vectors
- Top-K Retrieval

Pipeline:

```
Documents
      │
      ▼
Embeddings
      │
      ▼
Query Embedding
      │
      ▼
Cosine Similarity
      │
      ▼
Top-K Results
```

---

## 3. Metadata with Embeddings

Learned:

- Metadata
- Store metadata
- Filter metadata
- Complete metadata pipeline

Metadata Example

```python
{
    "id": 1,
    "text": "...",
    "embedding": [...],
    "metadata": {
        "source": "python.pdf",
        "page": 10,
        "department": "Programming"
    }
}
```

---

# Complete Embedding Pipeline

```
Documents
      │
      ▼
Chunking
      │
      ▼
Embedding Model
      │
      ▼
Embedding Vectors
      │
      ▼
Metadata
      │
      ▼
Similarity Search
      │
      ▼
Top-K Results
```

---

# Concepts Learned

- Embeddings
- Embedding Models
- Dense Embeddings
- Vector Dimensions
- Cosine Similarity
- Similarity Search
- Top-K Retrieval
- Metadata
- Metadata Filtering
- Embedding Pipeline

---

# Technologies Used

- Python
- Google Gemini Embeddings
- LangChain
- NumPy
- python-dotenv
- UV Package Manager

---

# Packages

```bash
uv add langchain-google-genai
uv add python-dotenv
uv add numpy
```

---

# Run the Programs

Google Embeddings

```bash
uv run 01_embed_query.py
```

```bash
uv run 02_embed_documents.py
```

```bash
uv run 03_vector_dimension.py
```

```bash
uv run 04_return_types.py
```

Similarity Search

```bash
uv run 01_generate_embeddings.py
```

```bash
uv run 02_compare_embeddings.py
```

```bash
uv run 03_top_k_search.py
```

Metadata

```bash
uv run 01_metadata.py
```

```bash
uv run 02_store_metadata.py
```

```bash
uv run 03_filter_metadata.py
```

```bash
uv run 04_metadata_pipeline.py
```

---

# Interview Topics Covered

- What is an Embedding?
- What is an Embedding Model?
- Dense vs Sparse Embeddings
- Vector Dimensions
- Cosine Similarity
- Similarity Search
- Top-K Search
- Metadata
- Metadata Filtering
- Embedding Optimization
- Production Best Practices

---

# Key Takeaways

- Embeddings convert text into vectors while preserving semantic meaning.
- Similarity search compares vectors instead of exact words.
- Cosine similarity measures how close two embeddings are.
- Metadata provides context such as source, page, and department.
- Production RAG systems combine embeddings, metadata, and similarity search to retrieve relevant documents efficiently.

---


**Harish Chinthalapudi**

Generative AI Engineering Practice Repository
