from rich import print
from main_module.llm_module.similar_search import getmodel
import time 
def aboutinfo():
    time.sleep(0.7)
    print("[bold green]I am Smart assistent which is developed by  Aayush[/bold green]")
    
def add():
    num1,num2= map(int,input("Enter the number").split())
    print(num1+num2)

def sub():
    num1,num2= map(int,input("Enter the number").split())
    print(num1+num2)

def div():
    num1,num2= map(int,input("Enter the number").split())
    print(num1+num2)

def multiplication():
    num1,num2= map(int,input("Enter the number").split())
    print(num1+num2)

def power():
    num1,num2= map(int,input("Enter the number").split())
    print(num1+num2)
    
    
def notfound():
    time.sleep(0.7)
    print("[bold red]This fuctionaltiy does not exist [/bold red]")