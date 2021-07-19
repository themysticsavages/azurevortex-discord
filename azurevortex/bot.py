import os
import json
import discord
from datetime import datetime
from discord.ext.commands.errors import UserNotFound
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

import util.dog
import util.genemail
import util.highcont
import util.format
import util.youtube

os.chdir('\\'.join(__file__.split('\\')[0:-1]))
os.system('cls')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    print('Azure is ready!')

@slash.slash(name="ping", description="Send a ping", guild_ids=None)
async def _ping(ctx):
    await ctx.send(f":ping_pong: Pong! ({round(client.latency*1000)} ms)")

@slash.slash(name="help", description="Get help and commands", guild_ids=None)
async def _help(ctx):
    embedVar = discord.Embed(title="Help", color=0x00000, description='[**Invite me!**](https://discord.com/api/oauth2/authorize?client_id=865975119801221120&permissions=939600902&scope=applications.commands%20bot)', timestamp=datetime.utcnow())
    embedVar.add_field(name="😐 General", value="`help`, `ping`", inline=True)
    embedVar.add_field(name="🎉 Fun", value="`email`, `dog`, `highcont`, `text`, `youtube`", inline=True)
    await ctx.send(embed=embedVar)

@slash.slash(name="dog", description="Send a cute doggo", guild_ids=None)
async def _dog(ctx):
    await ctx.send(util.dog.getdog())

@slash.slash(name="email", description="Get a random email address (not secure)", guild_ids=None)
async def _email(ctx):
    await ctx.send(util.genemail.getrandemailaddr())

@slash.slash(name="highcont", description="Make an image high-contrast!", options=[create_option(name="url", description="Raw image URL", option_type=3, required=True)], guild_ids=None)
async def _highcont(ctx, url: str):
    await ctx.send(util.highcont.highcont(url))

@slash.slash(name="text", description="Get a ton of cool formats for text!", options=[create_option(name="format", description="Format", option_type=3, required=True), create_option(name="thing", description="Text to format", option_type=3, required=True)], guild_ids=None)
async def _format(ctx, format: str, thing: str):
    if format == 'toxify':
        await ctx.send(util.format.toxify(thing))
    elif format == 'memify':
        await ctx.send(util.format.memify(thing))
    elif format == 'blockify':
        await ctx.send(util.format.blockify(thing))
    else:
        embedVar = discord.Embed(title="Text help", description='**Current text formats:**\n(toxify) bBrRuUhH!!111!!1 :clap::clap::clap:\n(memify) :b:ruh :flushed::100:\n(blockify) ▅▆▇▉ :fire: bruh :fire: ▉▇▆▅', color=0x00000, timestamp=datetime.utcnow())
        await ctx.send(embed=embedVar)

@slash.slash(name="youtube", description="Return a YouTube video from a search query", options=[create_option(name="query", description="YouTube search query", option_type=3, required=True)], guild_ids=None)
async def _youtube(ctx, query: str):
    await ctx.send(util.youtube.returnvideofromsearch(query))

client.run(json.loads(open('./config.json', 'r').read())['token'])