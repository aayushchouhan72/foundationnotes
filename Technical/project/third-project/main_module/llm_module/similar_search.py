from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq


#  LOcal imports
 
from main_module.datas.searchrange import searchlist
load_dotenv()

api = os.getenv("GROQ_API_KEY")


def getmodel():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=api
    )

def get_key(query:str)->str:
         llm = getmodel()

         response = llm.invoke(F"""search most simailar element from the give element from the list
           this is the list {searchlist} and the next is user query  {query} only return most  match or related in terms of meaning  element from the list not any other text exact same  if key not prsent simple return "not found" only 
           one more condition if query related  to komal then query should ends with 0 if not end with zero then  return "not found" only

 """)    
         return response.content
