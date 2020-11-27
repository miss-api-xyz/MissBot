import discord
from discord.ext import commands
from src import config

import os
import time
import requests
import json
import traceback
import random
import sys

from ..utils.createPaste import createPaste
from ..modules import pastebin 
from ..utils.createPaste import createPaste

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # compile command
    @commands.has_any_role(config.ownerRole)
    async def compile(self, ctx, *, code=None):
        if not code:
            return await ctx.send("```undefined```")
        cur_time = int(time.time())

        code = code.replace('```', '')
        code = code.replace('py', '')
        code = code.replace('```', '')

        po = { "cmd": 'python main.cpp', "src": code }
        r = requests.post('http://coliru.stacked-crooked.com/compile', data=json.dumps(po))
        tim = int(time.time())
        res = r.text
        if len(res) == 0:
            res = 'No output'
        else:
            res = r.text[:1000]

        await ctx.send("```fix\nOutput: {}s```\n".format(tim - cur_time) + f"```py\n{res}```")


    @commands.command(aliases=["evil", "e", "ebal"]) # eval command
    @commands.has_any_role(config.ownerRole) 
    async def eval(self, ctx, *, code=None):
        if not code:
            return await ctx.send("```undefined```")

        try:
            code = str(code)
            output = eval(code)
            await ctx.send(f"```py\n{output}```")
        except Exception as error:
            await ctx.send(f"```py\n{error}```")


def setup(client):
    client.add_cog(OwnerCommands(client))