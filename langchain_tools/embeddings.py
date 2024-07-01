from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


def load_embeddins():
    load_dotenv()
    # model = "text-embedding-ada-002"
    model = "text-embedding-3-small"

    return OpenAIEmbeddings(model=model)
