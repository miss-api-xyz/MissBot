import discord
from discord.ext import commands
from discord import TextChannel
from src import config

class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Client successfull connected to Discord.')
        await self.client.change_presence(activity=discord.Game(name="miss-api.xyz"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{ctx.author.mention}, Command not found.")

def setup(client):
    client.add_cog(Ready(client))