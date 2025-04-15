import discord


class Command():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def run(self, client: discord.Client, interaction: discord.Interaction):
        await interaction.response.send_message('🏓 Pong!')


command = Command(
    name='ping',
    description='Get ping of the bot.'
)
