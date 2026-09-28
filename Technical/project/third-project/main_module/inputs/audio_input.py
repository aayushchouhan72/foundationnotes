import speech_recognition as sr
from rich import print


def _get_best_microphone_index():
    try:
        devices = sr.Microphone.list_microphone_names()
        if not devices:
            return None

        preferred = [
            'microphone array',
            'microphone',
            'headset',
            'input',
            'realtek',
        ]

        for phrase in preferred:
            for index, device_name in enumerate(devices):
                name = (device_name or '').lower()
                if phrase in name and 'virtual' not in name and 'output' not in name and 'speaker' not in name:
                    return index

        # If nothing matches, fall back to the first non-virtual input device.
        for index, device_name in enumerate(devices):
            name = (device_name or '').lower()
            if 'virtual' not in name and 'output' not in name and 'speaker' not in name:
                return index

        return 0
    except Exception:
        return 0


def audioinput() -> str:
 
    try:
        mic_names = sr.Microphone.list_microphone_names()
        if not mic_names:
            print("[bold red]No microphone detected on this system.[/bold red]")
            return ""
    except Exception as e:
        print(f"[bold red]Microphone check failed: {e}[/bold red]")
        return ""

    mic_index = _get_best_microphone_index()
    print(f"[bold yellow]Using microphone index: {mic_index}[/bold yellow]")

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0
    recognizer.energy_threshold = 350
    recognizer.dynamic_energy_threshold = True

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("[bold green]Adjusting background noise...[/bold green]")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[bold cyan]Speak now...[/bold cyan]")

            audio = recognizer.listen(source, timeout=12, phrase_time_limit=8)
            print("[bold green]Recording complete! Processing...[/bold green]")
            text = recognizer.recognize_google(audio)
            print(f"[bold cyan]You said:[/bold cyan] {text}")
            return text.lower().strip()

    except sr.UnknownValueError:
        print("[bold red]Could not understand the audio. Please speak more clearly.[/bold red]")
        return ""
    except sr.RequestError as e:
        print(f"[bold red]Speech recognition service error: {e}[/bold red]")
        return ""
    except sr.WaitTimeoutError:
        print("[bold red]You didn't speak within 12 seconds.[/bold red]")
        return ""
    except Exception as e:
        print(f"[bold red]Microphone error: {e}[/bold red]")
        return ""