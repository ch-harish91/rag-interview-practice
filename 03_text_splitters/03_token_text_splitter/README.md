
# TokenTextSplitter

## Objective

Learn how to split text based on **tokens** instead of **characters** using LangChain's `TokenTextSplitter`.

---

## What is TokenTextSplitter?

`TokenTextSplitter` divides text into smaller chunks based on **token count**. It is useful because Large Language Models (LLMs) and embedding models process **tokens**, not characters.

---

## Why Use TokenTextSplitter?

- Creates token-based chunks.
- Helps keep chunks within model token limits.
- Useful for embedding models and LLMs.
- Supports chunk overlap to preserve context.

---

## Installation

```bash
uv add langchain-text-splitters
uv add tiktoken
```
