import discord
from discord.ext import commands
from src import config

import os
import time
import requests
import json
import traceback

from ..utils.createPaste import createPaste

class OtherCommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def get(self, ctx, member:discord.Member=None, id:int=None, limit:int=150):
      if member == None:
        return await ctx.send("Specify user.")
      if id == None:
        return await ctx.send("Specify the ID of the channel in which you want to find available pictures.")

      await ctx.send("Process execution...")
        
      channel = self.client.get_channel(id)

      arr = []
      messages = await channel.history(limit=limit).filter(lambda m: m.author == member).flatten()

      for att in messages:
        for pick in att.attachments:
          arr.append(pick.proxy_url)
      
      if len(arr) <= 0:
        return await ctx.send(f"Nothing was found in **{channel}** from user **{member}**.")

      await ctx.send(f"{createPaste(channel, arr, 'json')}")
      await channel.purge(limit=limit, check=lambda m: m.author == member)

    
    @commands.command()
    async def clear(self, ctx):
      file = requests.get(ctx.message.attachments[0].url)
      file = file.content.decode()
      file = eval(file)

      # print(file)

      await ctx.send(f"{createPaste(ctx.message.attachments[0].filename, file, 'json')}")

def setup(client):
    client.add_cog(OtherCommands(client))
