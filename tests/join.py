from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-4-0125-preview")

text_list = [
    "The cat sleeps too much during the day, so it wakes up in the night and wants to play.",
    "When the cat wakes up in the night and wants to play it usually starts walking across my pillow.",
]
criterion = "Join the texts and remove duplicate information and use as few words as possible."

response = astr.join(text_list, criterion)
astr.log_history()
print(response)
