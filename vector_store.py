from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def create_vectorstore(text: str, openai_api_key: str) -> FAISS:
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
