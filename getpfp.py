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
        if member == None:
            member = ctx.author
            embed=discord.Embed()
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
        elif member:
            embed=discord.Embed()
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
            
client.run(token)