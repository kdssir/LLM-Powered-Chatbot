from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from utils import load_pdf

class RAGChatbot:
    def __init__(self, pdf_path: str):
        self.docs = load_pdf(pdf_path)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = FAISS.from_documents(self.docs, embeddings)

        # Use flan-t5-large instead of llama2/mistral
        qa_pipeline = pipeline(
                "text2text-generation",
                model="google/flan-t5-large",
                tokenizer="google/flan-t5-large",
                max_length=512,
                truncation=True
            )

        llm = HuggingFacePipeline(pipeline=qa_pipeline)

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=self.vectorstore.as_retriever()
        )



    def ask(self, query: str) -> str:
        try:
            print(f"Query: {query}")
            result = self.qa_chain.invoke({"query": query})
            print(f"Result: {result}")
            return result['result']
        except Exception as e:
            print(f"Error during LLaMA2 QA: {e}")
            return "Sorry, something went wrong while generating the answer."

