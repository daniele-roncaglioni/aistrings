from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-4-0125-preview", temperature=0)

text = "I would have never though that i would one day love dogs as much as cats."
test_text = "Love for dogs."
response = astr.match(text, test_text)
astr.log_history()
print(response)

test_text = "Love for parrots."
response = astr.match(text, test_text)
astr.log_history()
print(response)
