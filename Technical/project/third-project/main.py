from rich import print
import time

#  User define modules
from main_module.starters import starter
from main_module.beast_mode import beast_start
from main_module.beast_voice_mode import beast_start_voice


while True:
        print("""[bold green]
Enter the 1 to start application text mode ..😎😎[/bold green]""")
        time.sleep(0.8)
        print("""[bold green]Enter the 2 to access in the beast mode ..😎😎[/bold green]""")
        time.sleep(0.8)
        print("""[bold green]Enter the 3 to access voice mode ..🎙️[/bold green]""")
        time.sleep(0.8)
        print("""[bold green]Enter the 4 to close application..😓😓[/bold green]
""")
        time.sleep(0.8)
        choice = input("Enter your choice ... ")
        match choice:
                case "1":
                       starter()     # application starter function call from here ...
                case "2":
                       beast_start()    # application start in beast mode ...
                case "3":
                       beast_start_voice()     # voice mode work
                case "4":
                        time.sleep(2)
                        print("[bold red]Aapne application band kar diya...😒😒😒[/bold red]")
                        break
                case _:
                        time.sleep(1)
                        print("[bold red]Enter a valid choice...[/bold red]")
                        time.sleep(2)