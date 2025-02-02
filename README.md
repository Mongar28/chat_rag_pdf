# PDF Chatbot con Langchain y Streamlit

Este proyecto implementa un sistema de Recuperación de Respuestas Generadas (RAG) utilizando Langchain para crear un chatbot que puede interactuar con documentos PDF. La aplicación está desplegada en Streamlit, proporcionando una interfaz de usuario intuitiva y fácil de usar.

![Aplicacion desplegada](/assets/chat_rag_pdf.png)

## Características

- **Langchain**: Una potente biblioteca que facilita la construcción de aplicaciones basadas en modelos de lenguaje. En este proyecto, Langchain se utiliza para la recuperación de respuestas generadas (RAG), lo que permite al chatbot buscar y generar respuestas precisas basadas en el contenido de los documentos PDF.
- **Streamlit**: Despliegue de la aplicación con una interfaz de usuario intuitiva y fácil de usar.
- **Interacción con PDF**: Permite al chatbot extraer y proporcionar información de documentos PDF.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Mongar28/chat_rag_pdf
    cd chat_rag_pdf
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Crea un archivo `.env` en el directorio raíz del proyecto y agrega tu API token de OpenAI:

    ```plaintext
    OPENAI_API_KEY="tu_api_token_de_openai"
    ```

    Este archivo `.env` es crucial para configurar el modelo de lenguaje que se utilizará en la aplicación. La clave `OPENAI_API_KEY` debe contener tu token de API de OpenAI, que permite a la aplicación acceder y utilizar los modelos de lenguaje de OpenAI.

## Uso 

1. Ejecuta la aplicación:

    ```bash
    streamlit run app.py
    ```

2. Abre tu navegador web y ve a `http://localhost:8501` para interactuar con el chatbot.

## Estructura del Proyecto

```plaintext
├── app.py                 # Archivo principal de la aplicación Streamlit
├── assets                 
├── chat                   # Modulos que definen parte del comportamiento del chat
│   ├── chat_behavior.py
│   └── streamlit_tools.py
├── documents              
│   └── pdfs               # Directorio donde se guardaran los archivos PDF
├── embeddings             # Directorio donde se guardaran las bases de datos vectoriales
├── langchain_tools        # Directorio donde estarán los módulos encargados del comportamiento del RAG
│   ├── embeddings.py
│   ├── __init__.py
│   ├── llm.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── split_docs.py
│   └── vectorstore.py
├── .env                   # Archivo donde se guarda el OPENAI_API_KEY para poder mover el LLM 
├── LICENSE
├── README.md
├── requirements.txt       # Lista de dependencias del proyecto 
└── streamlit_components   # Directorio donde se encuentra el módulo con parte de los componentes de Streamlit 
    ├── components.py

