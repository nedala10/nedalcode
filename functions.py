from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage,SystemMessage,AIMessage


# CREATE LLM 
llm = ChatOpenAI(openai_api_key="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", temperature=0)


# CREATE EMBEDDING FUNCTION
STembadding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# CALL THE VECTOR DB FROM LOCAL USING CHROMA 
vector_db = Chroma(
    persist_directory="../VectorDB",
    embedding_function=STembadding
    )


# CREATE MEMORY
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)



# CREATE CHAIN 

con_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=memory,
    retriever=vector_db.as_retriever(score_threshold=0.7),
    chain_type="stuff"
    
)


def conRAG(inquiry:str) -> str :


    replay = con_chain({"question": inquiry})

    return replay.get("answer")