import streamlit as st
from chat.streamlit_tools import import_file
from langchain_tools.split_docs import load_split_docs
from langchain_tools.llm import load_llm_openai
from langchain_tools.embeddings import load_embeddins
from langchain_tools.retriever import create_retriever
from langchain_tools.vectorstore import create_verctorstore
from langchain_tools.rag_chain import create_rag_chain
from streamlit_components.components import (
    load_app_title,
    load_sidebar,
    load_title_logo)
from chat.chat_behavior import (
    create_store_conversation_history,
    display_chat_messages,
    clear_chat_history,
    create_chat_history,
    run_chat
)


def main():
    load_app_title()
    load_sidebar()
    load_title_logo()

    pdf_name = import_file()

    if pdf_name:
        with st.spinner("Processing the document..."):
            docs_split: list = load_split_docs(pdf_name)
            embeddings_model = load_embeddins()
            llm = load_llm_openai()
            create_verctorstore(
                docs_split,
                embeddings_model,
                pdf_name
            )
            retriever = create_retriever(
                embeddings_model
            )

            # Creamos el RAG chain y lo asignamos a una key de la session_state
            if "qa" not in st.session_state.keys():
                st.session_state.qa = create_rag_chain(
                    llm, retriever)

        create_store_conversation_history()
        display_chat_messages()
        clear_chat_history()

        st.sidebar.button("Clear chat history", on_click=clear_chat_history)

        @st.cache_resource
        def get_num_tokens(prompt):
            """Get the number of tokens in a given prompt"""
            return len(prompt.split())

        create_chat_history()
        run_chat()


if __name__ == "__main__":
    main()
