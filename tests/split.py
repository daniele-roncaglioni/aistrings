from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-4-0125-preview", temperature=0)

text = "I have never seen Saturn through a telescope, but I would really love to see it once."
criterion = "Split the text using names of planets of the solar system as separators."
response = astr.split(text, criterion)
astr.log_history()
print(response)
