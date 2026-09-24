from rich import print
import time

#  User define modules
from main_module.starters import starter



while True:
        print("""[bold green]
Enter the 1 to start application text mode ..😎😎[/bold green]""")
        time.sleep(0.8)
        print("[bold green]Enter the 2 to access in the beast  mode ..😎😎[/bold green]""")
        time.sleep(0.8)
        print("""[bold green]Enter the 3 to close application..😓😓[/bold green]
""")
        time.sleep(0.8)
        choice=input("Enter the your choice ...")
        match choice:
                case "1":
                       starter()     # appplication  starter fuction call from here ... 
                case "2":
                     pass      # application start in the beast mode ...
                case "3":
                        time.sleep(2)
                        print("[bold red]Dost aap neee tooo  application band kar diyaaaa...😒😒😒[/bold red]")
                        break
                case _:
                        time.sleep(1)
                        print("[bold red]Enter the valid choice...[/bold red]")
                        time.sleep(2)