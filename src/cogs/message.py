import discord
from discord.ext import commands
from src import config

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client


    # @commands.Cog.listener()
    # async def on_message(self, message):


def setup(client):
    client.add_cog(Message(client))