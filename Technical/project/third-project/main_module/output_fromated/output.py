
from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown
from rich import print
import time
import os

try:
    import pyttsx3
except Exception:
    pyttsx3 = None


# Local import
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

def speak(text: str):
    """Converts text to speech using pyttsx3 with a Windows fallback."""
    text = str(text).strip()
    if not text:
        return

    try:
        if pyttsx3 is None:
            raise RuntimeError("pyttsx3 is not installed")

        engine = pyttsx3.init(driverName='sapi5' if os.name == 'nt' else None)
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.5)
        engine.say(text)
        engine.runAndWait()
        return
    except Exception as e:
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(text)
            return
        except Exception:
            print(f"[Voice Error]: Could not play audio - {e}")