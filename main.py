import discord
from discord.ext import commands
from src import config

import os
import requests
import json
import traceback

client = commands.Bot(command_prefix = config.prefix)
# client.remove_command("help")

@client.command()
async def load(ctx, extension):
    if not extension:
        return await ctx.send("Please indicate cog which you want to load")
    client.load_extension(f"src.cogs.{extension}")
    await ctx.send(f"Cog {extension} successfull load.")

@client.command()
async def unload(ctx, extension):
    if not extension:
        return await ctx.send("Please indicate cog which you want to unload")
    client.unload_extension(f"src.cogs.{extension}")
    await ctx.send(f"Cog {extension} successfull unload.")

for file in os.listdir("./src/cogs"):
    if file.endswith(".py"):
        client.load_extension(f"src.cogs.{file[:-3]}")
        print(f"Cog {file} success loaded.")

client.run(os.getenv("token"))