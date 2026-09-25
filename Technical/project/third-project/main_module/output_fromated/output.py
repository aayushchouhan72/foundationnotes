
from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown
from rich import print
import time
from main_module.llm_module.similar_search import getmodel

def fromated_output(query,instruction):
     con=Console()
     full_response = ""
     llm=getmodel()
     with Live(console=con, refresh_per_second=15) as live:
                   for chunk in llm.stream(f"Give the answer of given user query {query} according to given instruction {instruction}"):
                          for char in chunk.content:
                                  full_response += char
                                  live.update(Markdown(full_response))
                                  time.sleep(0.01)
     return full_response 
     print()