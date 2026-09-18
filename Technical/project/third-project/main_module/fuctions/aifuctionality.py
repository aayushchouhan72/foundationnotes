import time
from rich.console import Console
from rich.markdown import Markdown

#  Local import 
from main_module.llm_module.similar_search import getmodel



def city_weather():
    llm =  getmodel()
    time.sleep(0.7)
    city_name=  input("Enter the city weather ...")
    res=llm.invoke(f"""
Give city weather {city_name} report in on line 

""")
    print(res.content)

def news_genrator():
    llm=getmodel()
    time.sleep(0.7)
    con = Console()
    news_domain=  input("Enter the News domain ...")
    res=llm.invoke(f"""
return the 5 news this news  {news_domain} 

""")
    con.print(Markdown(res.content))   