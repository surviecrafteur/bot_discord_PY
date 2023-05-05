import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = ",",description= "video tuto de surviecrafteur", intents = discord.Intents.all(),allowed_mentions = discord.AllowedMentions (everyone = True),)

@bot.event
async def on_ready():#un evenement lorseque le bot est conecter
	print("\x1b[42;5;226mconecté:\x1b[0m" + str(bot.user))

@bot.command()
async def chanellesend(ctx):#envoyer un message dans le channel actuelle
    await ctx.send("votre message")#renplacrer "votre message" par le message de votre choix

@bot.command()
async def reponserandome(ctx):#envoyer un message aleatoire dans le channel actuelle
    variable = ["reponce1","reponce2","reponce3"]#remplacer les "reponce" par ce que vous vouller 
    await ctx.send(random.choice(variable))

@bot.command()
async def channele(ctx):#envoyer un message dans le channel actuelle et un channel predefinie
    channel = bot.get_channel(1074351644059381800)
    await channel.send("votre message1")
    await ctx.send("votre message2")

bot.run(token = "insérez votre token ici")#renplacrer "insérez votre token ici" par votre token a ne pas partager
