import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()  
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pa(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')


bot.run("MTE2MjA1NTg0MjYwMjk1NDc4Mg.G2mpFF.6Y65jgG4juFZfNt1MFtLqKq2bn28R2Dls2t-e4")
