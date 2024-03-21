from langchain_community.chat_models import ChatOpenA
from dotenv import load_dotenv
import os
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

#import requests
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


article_txt=open("article.txt","r")
article_str = article_txt.read() # string of the entire file



"""
loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()

    # Split and embed the text in the documents
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()

    # Store the embeddings in a database as local files
    db = FAISS.from_documents(texts, embeddings)
    db.save_local('vectorstore/db_faiss')
    retriever = db.as_retriever()
"""

