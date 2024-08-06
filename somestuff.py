from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureOpenAI
from langchain_core.output_parsers import StrOutputParser

animal = """
elephant
"""

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        given information about an animal {animal} I want you to write:
        1. a short summary
        2. give one interesting fact about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables="animal", template=summary_template
    )
    llm = AzureOpenAI(
        deployment_name=os.environ["MY_DEPLOYMENT_NAME"],
        azure_endpoint=os.environ["MY_OPENAI_API_BASE"],
        openai_api_version=os.environ["MY_OPENAI_API_VERSION"],
        openai_api_key=os.environ["MY_OPENAI_API_KEY"],
    )
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"animal": animal})
    print(res)


def printEnvVars():
    load_dotenv()
    print("Hello world")
    print(os.environ["MY_SPECIAL_KEY"])
    print(os.environ["MY_SECOND_KEY"])
