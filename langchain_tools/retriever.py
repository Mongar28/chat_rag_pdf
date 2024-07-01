from langchain_chroma import Chroma
import streamlit as st


def create_retriever(embeddings):
    # Cargamos la vectorstore
    # vectordb = Chroma.from_documents(
    #     persist_directory=st.session_state.persist_directory,  # Este es el directorio del la vs del docuemnto del usuario que se encuentra cargado en la session_state.
    #     embedding_function=embeddings,
    # )
    vectordb = Chroma(
        persist_directory=st.session_state.persist_directory,
        embedding_function=embeddings,
    )

    # Creamos el retriver para que retorne los fragmentos mas relevantes.
    return vectordb.as_retriever(search_kwargs={"k": 10})
