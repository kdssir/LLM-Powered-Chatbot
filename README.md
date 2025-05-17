
#  LLM-Powered PDF Chatbot (RAG App)

A simple but powerful **local chatbot** that lets users upload a PDF document and ask natural language questions about its contents — all powered by **Retrieval-Augmented Generation (RAG)** and a **local language model (LLM)**.

---

##  Features

-  Upload and index PDF documents
-  Ask questions about uploaded content
-  Uses semantic search + LLM for intelligent answers
-  100% offline, no OpenAI API or cloud dependency
-  Easily switch between local models like `flan-t5`, `flan-alpaca`, or `mistral`

---

##  How It Works

1. **PDF Upload:** User uploads a document via a simple web UI.
2. **Chunking:** The document is split into smaller text chunks.
3. **Embedding:** Each chunk is converted to a vector using `sentence-transformers`.
4. **Indexing:** Embeddings are stored in a `FAISS` vector store for fast semantic retrieval.
5. **Querying:**
   - When a user asks a question, the app finds the most relevant chunks using similarity search.
   - Those chunks are passed to a local language model (LLM) like `flan-alpaca` or `flan-t5`.
   - The LLM generates a fluent answer in natural language.

---

##  Getting Started

###  Prerequisites

- Python 3.9+
- pip
- Virtual environment (recommended)

###  Installation

```bash
git clone https://github.com/your-username/llm-pdf-chatbot.git
cd llm-pdf-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

###  Run the App

```bash
uvicorn main:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

##  Example Use Case

Upload a file like `FAQ.pdf`, then ask:

> _"What is the return policy?"_

And the chatbot will return the most relevant answer based on the document's content.

---

##  Model Options

This app uses a local model through `transformers`. Recommended models:

| Model                      | Type      | RAM Needed | Notes                      |
|---------------------------|-----------|------------|----------------------------|
| `google/flan-t5-base`     | Tiny      | ~1GB       | Fastest, lowest quality    |
| `google/flan-t5-large`    | Medium    | ~4GB       | Good balance               |
| `declare-lab/flan-alpaca-base` | Medium | ~2GB       | Instruction tuned         |
| `mistralai/Mistral-7B`    | Large     | ~12GB+     | High quality, use with Ollama |

To switch models, change the Hugging Face model name in `rag_chain.py`.

---

##  Project Structure

```
llm-pdf-chatbot/
├── main.py               # FastAPI backend with endpoints
├── rag_chain.py          # Core RAG pipeline logic
├── utils.py              # PDF loader and preprocessor
├── templates/index.html  # Simple frontend
├── static/style.css      # UI styling
├── requirements.txt      # Python dependencies
```

---

##  Dependencies

```txt
fastapi
uvicorn
langchain
langchain-community
transformers
sentence-transformers
faiss-cpu
```

If using `mistral` or `llama2` locally, install `langchain-ollama` and run `ollama run mistral`.

---

##  License

MIT License — free to use, modify, and share.

---

##  Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Hugging Face Transformers](https://huggingface.co)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [FastAPI](https://fastapi.tiangolo.com/) — For building the modern Python web API backend
