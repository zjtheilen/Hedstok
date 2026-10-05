import json

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

client = genai.Client(http_options=types.HttpOptions(timeout=30000))


def main():
    with open("experiment-1/discover-prompt.md", encoding="utf-8") as file:
        prompt = file.read()

    with open("experiment-1/discovery-input.json", encoding="utf-8") as file:
        evidence = file.read()

    prompt = prompt.replace(
        "[INSERT SIGNAL DATA HERE]",
        evidence,
    )

    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt,
    )

    with open(
        "experiment-1/discovery-output.md",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(interaction.output_text)


if __name__ == "__main__":
    main()
