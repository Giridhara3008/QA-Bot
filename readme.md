# Resume Question-Answering Chatbot (RAG with Flask)
A Flask web application that allows users to upload their resume in PDF format, processes the resume using Retrieval-Augmented Generation (RAG) with OpenAI embeddings and FAISS vector store, and enables users to ask questions about their resume via a chat interface.

## Features

- Upload PDF resumes securely
- Extract text from resumes using PyMuPDF
- Create semantic vector embeddings with OpenAI embeddings
- Store embeddings in a FAISS vector store for fast similarity search
- Build a Retrieval-Augmented Generation (RAG) question-answering chain using LangChain
- Interactive chat interface to ask questions about the uploaded resume

## Tech Stack

- **Flask** — Web framework for Python
- **OpenAI API** — For generating embeddings and answering questions
- **PyMuPDF** — Extract text from PDF files
- **FAISS** — Vector similarity search engine
- **LangChain** — To build RAG chains and manage embeddings & retrieval
- **Werkzeug** — For secure file uploads

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get from [OpenAI platform](https://platform.openai.com/account/api-keys))
## Project structure
app.py                 # Main Flask app
requirements.txt       # Python dependencies
utils/
    1.pdf_reader.py      # PDF text extraction logic
    2.vector_store.py    # Vector store creation logic with FAISS
    3.rag_chain.py       # Build RAG QA chain with LangChain
templates/
    1.upload.html        # Resume upload page
    2.chat.html          # Chat interface page
 uploads/               # Folder to store uploaded PDFs
## Steps to do the project
Install all requirements.txt and set up python virtual environment using venv. Built all required codes in app.py and run in the localhost.

## For running use the link
http://127.0.0.1:5000

## Conclusion
This project successfully demonstrates how to build a Retrieval-Augmented Generation (RAG) question-answering system over user-uploaded resumes using modern AI and NLP tools. By combining PDF text extraction, vector similarity search with FAISS, and language model embeddings from OpenAI via LangChain, the system provides relevant, context-aware answers to user queries based solely on their resume content.
The Flask-based web interface makes it accessible and user-friendly, turning complex AI workflows into a seamless interactive experience.
## Knowlege Gained
1.Understanding RAG (Retrieval-Augmented Generation): Learned how to enhance language model responses by retrieving contextually relevant documents from a vector store, improving accuracy and relevance.

2.Working with Vector Embeddings: Gained hands-on experience creating, storing, and querying text embeddings using OpenAI’s embedding API and FAISS.

3.PDF Text Extraction: Practiced extracting and preprocessing text from PDFs using PyMuPDF to prepare data for NLP tasks.

4.Building a Full-Stack AI Application: Developed skills in integrating backend AI components with a Flask web app, handling file uploads, managing state, and serving dynamic responses.

5.API Integration & Error Handling: Managed third-party API integration (OpenAI) including API key management, error diagnosis, and retry logic.

6.Python Modularization & Code Organization: Improved structuring code into reusable modules (pdf_reader.py, vector_store.py, rag_chain.py), which enhances maintainability.

7.This project is a solid foundation for building more advanced AI-powered document QA systems applicable in recruiting, legal, healthcare, and many other domains.


