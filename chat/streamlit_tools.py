import streamlit as st
import os


def import_file() -> str:
    List_of_files: list = []

    archivo = st.file_uploader(
        "Arrastra o ingresa tu archivo .pdf", type=[".pdf"])
    nombre_archivo: str = ""

    if archivo is not None:
        nombre_archivo = archivo.name

        List_of_files.append(nombre_archivo)

        with open(f"documents/pdfs/{nombre_archivo}", "wb") as new_file:
            new_file.write(archivo.read())
    if (
        "archivo_anterior" in st.session_state
        and st.session_state.archivo_anterior != nombre_archivo
    ):
        st.session_state.clear()
    st.session_state.archivo_anterior = nombre_archivo

    return nombre_archivo


# Define la función para borrar el caché
def clear_cache():
    cache_path = os.path.join(st.__path__[0], "static", "cache")
    for root, dirs, files in os.walk(cache_path):
        for file in files:
            os.remove(os.path.join(root, file))
