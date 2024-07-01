from langchain_chroma import Chroma
import streamlit as st
import os


def create_verctorstore(docs_split: list, embeddings, file_name: str):

    if "db_name" not in st.session_state.keys():
        st.session_state.db_name = (
            file_name.replace(".pdf", "").replace(" ", "_").lower()
        )
    if "persist_director" not in st.session_state.keys():
        st.session_state.persist_directory = (
            f"embeddings/{st.session_state.db_name}"
        )
    if not os.path.exists(st.session_state.persist_directory):
        vectordb = Chroma.from_documents(
            persist_directory=st.session_state.persist_directory,
            documents=docs_split,
            embedding=embeddings,
        )
