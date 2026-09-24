from rich.console import Console
from rich.markdown import Markdown
from rich import print
#  Local imports 
from main_module.inputs.text_input import datainput
from main_module.llm_module.similar_search import getmodel

#  Beast mode full function 
def beast_start():
    history={
        "user":[],
        "AI":[]
    }
    con=Console()
    while True:
       query = datainput()
       if query==0 or query == "0":
           return
       history["user"].append(query)
       llm =  getmodel()
       res = llm.invoke(f"Give the answer of given user query {query} important answer accoring to history {history} in which key ai contain your response and key user contain user querys ")
       con.print(Markdown(res.content))
       history['AI'].append(res.content)
       