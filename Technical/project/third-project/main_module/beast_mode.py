from rich.console import Console
from rich.markdown import Markdown
from rich import print
import time
from rich.live import Live

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
    llm =  getmodel()
    while True:
       query = datainput()
       if query==0 or query == "0":
           return
       history["user"].append(query)
       full_response = ""
       with Live(console=con, refresh_per_second=15) as live:
               for chunk in llm.stream(f"Give the answer of given user query {query} important answer "):
                      for char in chunk.content:
                              full_response += char
                              live.update(Markdown(full_response))
                              time.sleep(0.01) 
       print()
       history['AI'].append(chunk.content)
    