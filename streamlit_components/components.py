import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


def load_app_title():
    # App title
    st.set_page_config(page_title="DocumentAssist")


# Sidebar
def load_sidebar():
    with st.sidebar:
        # logo_path = "documents/logo_1-removebg-preview.png"
        # st.sidebar.image(logo_path, width=200)

        # Ajusta el ancho según sea necesario
        add_vertical_space(45)
        # pdf_name = import_file()
        st.markdown(
            "Built by [Cristian MG](https://www.linkedin.com/in/cristianmontoyagarces/).")


# Titulo y logo
def load_title_logo():
    col1, col2 = st.columns([1.1, 1])
    with col1:
        st.title(
            "DocumentAssist",
        )
    # with col2:
    #     st.image(
    #         "documents/pdfs/logo_1-removebg-preview.png", width=110
    #     )
