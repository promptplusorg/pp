import os
from embedchain import App
from dotenv import load_dotenv
load_dotenv()
ok = os.getenv('openai')

os.environ["OPENAI_API_KEY"] = ok
elon_musk_bot = App()

# Embed Online Resources


def embbding():
    elon_musk_bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
    elon_musk_bot.add("https://www.tesla.com/elon-musk")


def chat(text):
    response = elon_musk_bot.query(text)
    print(response)
    return (response)

# Answer: 'Elon Musk runs four companies: Tesla, SpaceX, Neuralink, and The Boring Company.'
