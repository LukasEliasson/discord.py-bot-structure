import discord
from discord import app_commands
from discord.ext import commands
from utils.command_loader import load_commands
import json

async def run(client: commands.Bot):
    print(f'✅ Logged in as {client.user}')

    try:
        # TESTING MODE:
        # False = Load commands globally
        # True = Load commands to testing guild only (set ID in config.json)
        TESTING_MODE = True

        load_commands(client, testing_mode=TESTING_MODE)

        if TESTING_MODE:
            with open('src/config.json') as config_file:
                config_data = json.load(config_file)
                config_file.close()

            guild_id = config_data['TESTING_GUILD_ID']
            guild = discord.Object(id=guild_id)
            synced = await client.tree.sync(guild=guild)

            guild_obj = client.get_guild(guild_id)

            print(f"✅ Synced {len(synced)} commands to guild '{guild_obj.name}'")
        
        else:
            synced = await client.tree.sync()

            print(f"✅ Synced {len(synced)} commands globally")

    except Exception as exception:
        print(f'⚠️ Failed to sync commands: {exception}')
