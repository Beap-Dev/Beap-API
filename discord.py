import discord
import random
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import has_role
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import cooldown, BucketType

intents = discord.Intents.all()
commands = commands.Bot(command_prefix=f'c!', intents=intents)
jpg = random.randint(1,50)

@commands.command()
async def cat(ctx):
  await ctx.reply(f"https://api.beapdev.net/api/cats/{jpg}.jpg")
  
@commands.command()
async def dog(ctx):
  await ctx.reply(f"https://api.beapdev.net/api/dogs/{jpg}.jpg")

@commands.command()
async def tiger(ctx):
  await ctx.reply(f"https://api.beapdev.net/api/tigers/{jpg}.jpg")
  
commands.run('token')
