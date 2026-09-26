from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich import print

from main_module.inputs.audio_input import audioinput
from main_module.output_fromated.output import speak
from main_module.llm_module.similar_search import getmodel

def beast_start_voice():
    """Interactive Beast Mode driven entirely by speech."""
    con = Console()
    llm = getmodel()
    
    print("[bold magenta]=== Voice Mode Activated ===[/bold magenta]")
    print("[bold yellow]Say 'exit' or 'stop' to return to main menu.[/bold yellow]")
    
    while True:
        query = audioinput()
        
        if not query:
            continue
        if query in ["exit", "stop", "back", "0"]:
            speak("Exiting voice mode.")
            return

        full_response = ""
        with Live(console=con, refresh_per_second=15) as live:
            for chunk in llm.stream(f"Give a concise spoken response to in very short text {query}"):
                for char in chunk.content:
                    full_response += char
                    live.update(Markdown(full_response))

        print()
        # Read the generated response back to the user
        speak(full_response)