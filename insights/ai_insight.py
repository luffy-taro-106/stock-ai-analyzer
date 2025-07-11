
from langchain.llms import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_insight(context):
    prompt = PromptTemplate.from_template(
        "Given this stock signal data: {context}, provide insights."
    )
    chain = LLMChain(llm=ChatGroq(model="llama3-70b"), prompt=prompt)
    return chain.run(context=context)

