# Beap-API

A API which is has images ready to be used in code.

**Examples:**

```
import random

jpg = random.randint(1,50)

print(f"https://api.beapdev.net/api/cats/{jpg}.jpg") # CATS
print(f"https://api.beapdev.net/api/dogs/{jpg}.jpg") # DOGS

```

```
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

```
