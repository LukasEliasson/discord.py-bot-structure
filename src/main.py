import discord
from discord.ext import commands
from utils.event_handler import handle_events
import json

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

handle_events(client)

with open('src/config.json') as config_data:
    data = json.load(config_data)
    config_data.close()

client.run(data['TOKEN'])
