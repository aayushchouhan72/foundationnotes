from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from rich import print
load_dotenv()


def create_model(provider):

    if provider == "groq":
        return init_chat_model(
            "openai/gpt-oss-20b",
            model_provider="groq"
        )
    elif provider == "google":
        return init_chat_model(
            "gemini-3-flash-preview",
            model_provider="google_genai"
        )

    elif provider == "openai":
        return init_chat_model(
            "gpt-6-luna",
            model_provider="openai"
        )

    else:
        return None


print("\n===== LLM MODEL SELECTOR =====")

print("""
1. Groq
2. Google Gemini
3. OpenAI
""")

choice = input("Choose a model provider (1-4): ")

providers = {
    "1": "groq",
    "2": "google",
    "3": "openai"
}

provider = providers.get(choice)

if provider is None:
    print("❌ Invalid choice")
    exit()


llm = create_model(provider)

query = input("\nEnter your query: ")

print(f"\n🤖 Using {provider.upper()}...\n")

try:
    response = llm.invoke(query)

    if provider == "google":
        print("AI Response:")
        print(response.content[0]['text'])
    else:
        print("AI Response:")
        print(response.content)

except Exception as e:
    print("\n❌ Error:")
    print(e)