# Build a smallLangChain app that sends prompts to OpenAI, switch tracing on, and watch the runs appear, with no code change.

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def main():
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    prompts = [
        "Explain what Python is in simple terms.",
        "What is the difference between AI and Generative AI?",
        "Explain LangChain in 3 simple points."
    ]

    for prompt in prompts:
        response = model.invoke(prompt)

        print("\n" + "=" * 60)
        print("PROMPT:")
        print(prompt)

        print("\nANSWER:")
        print(response.content)


if __name__ == "__main__":
    main()