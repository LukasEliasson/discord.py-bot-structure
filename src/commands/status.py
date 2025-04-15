import discord


class Command():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def run(self, client: discord.Client, interaction: discord.Interaction):
        pass  # Code goes here


command = Command(
    name='status',
    description='Get status information of the bot'
)
