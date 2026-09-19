import time
from rich.console import Console
from rich.markdown import Markdown

#  Local import 
from main_module.llm_module.similar_search import getmodel
from main_module.fuctions.utility.utility import get_level

#  Get City weater ....
def city_weather():
    llm =  getmodel()
    con = Console()
    time.sleep(0.7)
    city_name=  input("Enter the city weather ...")
    res=llm.invoke(f"""
Give city weather {city_name} report in on line 

""")
    con.print(Markdown(res.content))

#  News genrator....
def news_genrator():
    llm=getmodel()
    time.sleep(0.7)
    con = Console()
    news_domain=  input("Enter the News domain ...")
    res=llm.invoke(f"""
return the 5 news this news  {news_domain} 

""")
    con.print(Markdown(res.content))   

#  interview question genrator ....
def interview_question_genrator():

    con = Console()
    topics = con.input(
    "[bold green]Enter the topic name for which you want to generate questions: [/bold green]"
)
    number = con.input(
    "[bold green]Enter the number of questions for each topic: [/bold green]"
)
    level=get_level()
    llm = getmodel()
    res =  llm.invoke(f"""
    Gentenrate interview question on given topic {topics} on each topic and the number of question on each topic is {number} accodring to given diffcultiy level which is  {level} the output should be in proper one by on in line in markdown

""")
    con.print(Markdown(res.content))

#  Genrate impromptu topics ....
def impromtu_topic_genrator():
    con= Console()
    theam =  con.input("[bold green] Enter the theame genarate topics ..[/bold green]")
    number =  int(con.input("[bold green] Enter number of topics you wont .. [/bold green]"))
    llm = getmodel()
    res=llm.invoke(f"""
    Genrate {number} imprompt  speaking topic on {theam}  topic should be thatkind person can speak atleast for 1.5 minutes  return only topic name not additional text on topic 
""")
    con.print(Markdown(res.content))

#  Quiz Genrator ....
def quiz_genrator():
    con= Console()
    topics = con.input("[bold green] Enter the  topics ...[/bold green]")
    num = int(con.input("[bold green] Enter the number if question ... [/bold green]"))
    llm = getmodel()
    res=llm.invoke(f"""
        Genrate quiz  of the given topic {topics} and number of question should be {num} and the question should be in mcq fromate each question has 4 option  option in a,b,c,d this should be in proper markdown file 
         """)
    questions= res.content
    con.print(Markdown(res.content))
    answer= input("Enter the Answer 1-A ,2-B ...")
    res = llm.invoke(F"""
This are the question {questions} and this are the answer {answer} in fromate question number -  correct option return  report in proper fromate which question is correct 
for Example 
     question  ai stands for  ?
              A artificaial intelligence
              B automatic intelligence 
              C automatic industry
              D artifical industry
     status correct yes/no
     if no the correct option :- 
""")
    con.print(Markdown(res.content))


    













