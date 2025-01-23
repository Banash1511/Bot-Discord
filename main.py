import discord, os, audioop, logic as l, commandapi as ca, ambiente as am
from dotenv import load_dotenv
from logic import *
from discord.ext import commands

load_dotenv ()
Token = os.getenv ("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name = "psw")
async def password(ctx, lenght=25):
    a = l.contra(lenght)
    await ctx.send(f"🔐Su contraseña se ha generado: {a}")

@bot.command(name = "moneda")
async def luck(ctx):
    await ctx.send(l.moneda())

@bot.command(name = "meme")
async def momo(ctx):
    a = l.meme()
    await ctx.send(file=a)

@bot.command(name = "momasos")
async def momaso(ctx):
    a = l.momasos()
    await ctx.send(file=a)

@bot.command(name = "pato")
async def patos(ctx):
    a = ca.get_duck_image_url()
    await ctx.send(a)

@bot.command(name="eco")
async def ecologia(ctx, opc:int):
    if opc == 1:
        await ctx.send(embed=am.bolsas_biod())
    elif opc ==2:
        await ctx.send(embed=am.bolsas_biod2())
    elif opc == 3:
        await ctx.send(embed=am.bolsas_biod3())
    
    else:
        await ctx.send("esta opcion no existe")


bot.run(Token)