from fastapi import FastAPI,Depends,status
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import Chatnvidia
from langchain_nvidia import ChatNVIDIA
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv



load_dotenv()

os.environ['NVIDIA_API_KEY']=os.getenv("NVIDIA_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatNVIDIA(),
    path="/openai"
)
model=ChatNVIDIA()
##ollama llama2
llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"


)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
