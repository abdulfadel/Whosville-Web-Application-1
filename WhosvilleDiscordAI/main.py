import nextcord
import os
import nltk
from dotenv import load_dotenv
from neuralintents import GenericAssistant
# nltk.download()
chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("Whosville Bot is online!")

client = nextcord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-"):
        response = chatbot.request(message.content[0:])
        await message.channel.send(response)

client.run(TOKEN)