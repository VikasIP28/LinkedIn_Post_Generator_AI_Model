from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GRO_API_KEY"), model_name = "llama-3.1-70b-versatile")

if __name__ == "__main__":
    response = llm.invoke("What are the base colours to be used to get orange color")
    print(response.content)