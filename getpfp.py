import discord
import discord.ext
from discord.ext import commands
import json

client = commands.Bot(command_prefix = '$')

f = open("token.txt", "r")
token = f.read()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def getpfp(ctx, member: discord.Member = None):
    if member:
        pfp = member.avatar_url
        await ctx.send(pfp)
    elif not member:
        member = ctx.author
        pfp = member.avatar_url
        await ctx.send(pfp)

client.run(token)