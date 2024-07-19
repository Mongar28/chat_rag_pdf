from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def load_llm_openai():
    load_dotenv()
    # model = "gpt-3.5-turbo-0125"
    # model = "gpt-4o"
    model = "gpt-4o-mini"

    llm = ChatOpenAI(
        model=model,
        temperature=0.1,
        max_tokens=2000,
    )

    return llm
