from colorama import Fore, Style
import streamlit as st
from langchain_core.messages import HumanMessage


class MessageManager:
    def create_chat(self, qa):
        ia_emoticon = "\U0001f916"
        humano_emoticon = "\U0001f604"

        print(
            f"{ia_emoticon} "
            + Style.BRIGHT
            + Fore.YELLOW
            + "IA: "
            + Style.RESET_ALL
            + "Pregunta algo al documento"
        )
        while True:
            input_usuario = input(
                Style.BRIGHT + Fore.BLUE +
                f"{humano_emoticon} You: " + Style.RESET_ALL
            )
            if input_usuario.lower() == "salir":
                break
            bot_response = qa.invoke(
                {"question": f"{input_usuario}"}, return_only_outputs=True
            )
            print(
                f"{ia_emoticon} "
                + Style.BRIGHT
                + Fore.YELLOW
                + "IA:"
                + Style.RESET_ALL
                + f'{bot_response["answer"]}'
            )

    def generate_citations(self, documents_source: list) -> str:
        text_source: str = ""

        for index, document in enumerate(documents_source):
            quote: str = document.page_content
            source: str = document.metadata["source"].replace(
                "documents/pdfs/", "")
            page: str = document.metadata["page"] + 1
            fuente: str = (
                f"**Fuente #{index +
                             1}:** \n '{quote}'\n(*{source}, P.{page})*"
            )

            text_source += fuente + "\n\n\n"

        return text_source


def create_store_conversation_history():
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hola, soy una IA que te ayuda a chatear con tu PDF. Haz una pregunta al documento que acabas de cargar.",
            }
        ]


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hola, soy una IA que te ayuda a chatear con tu PDF. Haz una pregunta al documento que acabas de cargar.",
        }
    ]


def create_chat_history():
    # chat_history: list = []
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = []


def run_chat():
    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.spinner("Thinking..."):
                # Creamos la cadena que integra Vectorstroe, el LLM para hacer consultas.

                input = "\n".join([msg["content"]
                                  for msg in st.session_state.messages])

                query = st.session_state.qa.invoke(
                    {"input": prompt, "chat_history": st.session_state.chat_history}
                )

                response_text = query["answer"]
                documents_source = query["context"]

                # Agregamos la pregunta y la respuesta al chat_history
                st.session_state.chat_history.extend(
                    [HumanMessage(content=prompt), response_text]
                )

                messageManager = MessageManager()

                citation: str = messageManager.generate_citations(
                    documents_source)
                # st.markdown(citation)

            with st.chat_message("assistant"):
                st.write(response_text)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response_text}
                )
                expander = st.expander("Fuentes")
                expander.markdown(citation)

    # def generate_response(response):
    #     response_text = response_index.response
    #     response_source = response_index.source_nodes[0].metadata["file_name"]
    #     pages = [doc.metadata["page_label"] for doc in response_index.source_nodes]
    #     pages_sort = sorted(map(int, pages))
    #     response = (
    #         f'"{response_text}"(*{response_source}, PP.{",".join(map(str, pages_sort))}*)'
    #     )
    #
    #     return response
