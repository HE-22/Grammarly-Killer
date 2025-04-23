import os
import sys
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Avialable 4.1 models: gpt-4.1, gpt-4.1-mini, gpt-4.1-nano
# see for all models: https://platform.openai.com/docs/models
MODEL = "gpt-4.1-nano"

SYSTEM_PROMPT = """
You are an advanced spell check AI. simply return your input with corrected spelling,
and grammar without changing the meaning of what i was trying to say.
if i input code output the logical completion of code or clean up fomratting without changing 
what it is. never change the meaning or add extra stuff. think step by step in your head logically what makes the most sense.
Note: the majority of the time the input will not have spaces between words and will be heaviliy misspelled or abreaviated you are an expert so you can figure it out. but always take a step back and think. 

# OUTPUT FORMAT: 
user input: "helloworldthisisdisatest" -> assistant output: "hello world this is a test"
user input: "print('hello world')" -> assistant output: "print('hello world')"

if the text wasn't orignaly surrounded with quotes or language indicator, DO NOT add quotes around it, leave as close to original formatting as possible including multiple consequtive new lines and tabs. 

if there is slang you can keep it in but correct the spelling of it.
"""


def process_string(input_string: str) -> str:

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": input_string},
        ],
    )

    chat_response = completion.choices[0].message.content

    if chat_response is None:
        return ""

    return chat_response


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py 'input string'")
        sys.exit(1)

    input_str = sys.argv[1]

    output_str = process_string(input_str)
    if output_str is not None:
        output_str = output_str.rstrip("\n")
    print(output_str)
