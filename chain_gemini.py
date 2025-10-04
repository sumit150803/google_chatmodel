from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
    template="Generate a creative story about {topic}.",
    input_variables=["topic"]

)

model=ChatGoogleGenerativeAI( model="gemini-2.5-pro")

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({"topic":"a dragon who loves to bake cakes"})

print(result)
