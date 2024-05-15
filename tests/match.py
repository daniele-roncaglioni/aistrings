from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-3.5-turbo-0125", temperature=1)

targets = [
    "The cat sleeps too much",
    "The dog jumps over the fence",
    "The cat jumps over the fence",
    "I am so happy"
]
query = "The cat is very agile!"

response, index = astr.match(query, targets)
astr.log_history()
print(f"Option at index {index} is the best: \"{response}\"")
