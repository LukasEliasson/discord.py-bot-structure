import discord
from discord.ext import commands
from discord import app_commands
from os import listdir
from os.path import isfile, join, dirname
from importlib.util import spec_from_file_location, module_from_spec
import json

def load_commands(client: commands.Bot, testing_mode=False):
    commands_dir = join(dirname(__file__), '..', 'commands')
    files = listdir(commands_dir)

    for filename in files:

        if not filename.endswith('.py'):
            continue

        command_name = filename.removesuffix('.py')

        try:

            command_path = join(commands_dir, filename)

            spec = spec_from_file_location(command_name, command_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'command') and all(hasattr(module.command, attr) for attr in ['name', 'description', 'run']):

                async def command_run(interaction: discord.Interaction):
                    await module.command.run(client, interaction)

                command_obj = app_commands.Command(
                    name=module.command.name,
                    description=module.command.description,
                    callback=command_run
                )

                if testing_mode:
                    with open('src/config.json') as config_file:
                        config_data = json.load(config_file)
                        config_file.close()

                    guild_id = config_data['TESTING_GUILD_ID']
                    guild = discord.Object(id=guild_id)
                    
                    client.tree.add_command(command_obj, guild=guild)

                    guild_obj = client.get_guild(guild_id)

                    print(f"✅ Loaded command '{command_name}' to guild '{guild_obj.name}'")
                    
                else:
                    client.tree.add_command(command_obj)
                    print(f"✅ Loaded command '{command_name}' globally")

        except Exception as exception:
            print(f"❌ Failed to load command '{command_name}': {exception}")