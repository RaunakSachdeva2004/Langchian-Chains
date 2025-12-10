from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq.chat_models import ChatGroq
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")


prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic'])



parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({'topic':'stand up comedy'}))


chain.get_graph().print_ascii()