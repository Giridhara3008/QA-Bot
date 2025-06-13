from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_qa_chain(vectorstore, openai_api_key: str):
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
