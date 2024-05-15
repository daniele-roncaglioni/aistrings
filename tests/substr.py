from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-4-0125-preview", temperature=0)

text = (
    "For a brief early period when air-to-air combat was just being invented, the exceptionally skilled pilot could shape the battle in the skies. "
    "For most of the war, however, the image of the ace had little to do with the reality of air warfare, "
    "in which fighters fought in formation and air superiority depended heavily on the relative availability of resources. "
    "The successes of such German ace pilots as Max Immelmann and Oswald Boelcke, and especially Manfred von Richthofen, the most victorious fighter "
    "pilot of the First World War, were very publicized, for the benefit of civilian morale, and the Pour le Mérite, Prussia's highest award for gallantry,"
    " became part of the uniform of a leading German ace")
criterion = "The part where it talks about awards."
response = astr.substr(text, criterion)
astr.log_history()
print(response)
