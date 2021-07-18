import os
import json
import discord
from datetime import datetime
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

import util.dog
import util.genemail
import util.highcont

os.chdir('\\'.join(__file__.split('\\')[0:-1]))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    os.system('cls')
    print('Azure is ready!')

id = [835603476314587187]

@slash.slash(name="ping", guild_ids=id, description="Send a ping")
async def _ping(ctx):
    await ctx.send(f":ping_pong: Pong! ({round(client.latency*1000)} ms)")

@slash.slash(name="help", guild_ids=id, description="Get help and commands")
async def _help(ctx):
    embedVar = discord.Embed(title="Help", color=0x00000, description='[**Invite me!**](https://discord.com/api/oauth2/authorize?client_id=865975119801221120&permissions=939600902&scope=applications.commands%20bot)', timestamp=datetime.utcnow())
    embedVar.add_field(name="😐 General", value="`help`, `ping`", inline=True)
    embedVar.add_field(name="🎉 Fun", value="`email`, `dog`, `highcont`", inline=True)
    await ctx.send(embed=embedVar)

@slash.slash(name="dog", guild_ids=id, description="Send a cute doggo")
async def _dog(ctx):
    await ctx.send(util.dog.getdog())

@slash.slash(name="email", guild_ids=id, description="Get a random email address (not secure)")
async def _email(ctx):
    await ctx.send(util.genemail.getrandemailaddr())

@slash.slash(name="highcont", description="Make an image high-contrast!", options=[create_option(name="url", description="Raw image URL", option_type=3, required=True)])
async def _highcont(ctx, url: str):
    await ctx.send(util.highcont.highcont(url))

client.run(json.loads(open('./config.json', 'r').read())['token'])