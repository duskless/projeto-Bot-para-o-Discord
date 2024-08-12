import discord # importar a biblioteca
from discord.ext import commands # importando as ferramentas para utilizar os comandos
from math import sqrt
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('MEU_TOKEN')
permissoes = discord.Intents.default() # definindo as permissões
permissoes.message_content = True # permitindo que o bot leia as mensagens
permissoes.members = True # permitindo que o bot leia os membros
bot = commands.Bot(command_prefix="!", intents=permissoes) # definindo o prefixo e as permissões

@bot.command() # indica que a função abaixo vai ser um comando do discord
async def ola(ctx:commands.Context): # async condiz em rodar as funções quantas vezes forem necessárias
    # ctx é uma abreviação de Context que representa a chamada do comando
    usuario = ctx.author
    canal = ctx.channel
    await ctx.reply(f"Olá, {usuario.display_name}!\n Você está no canal: {canal.name}")

# Calculadora
@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    res = num1 + num2
    await ctx.reply(f"A soma de {num1} com {num2} é: {num1} + {num2} = {res}")

@bot.command()
async def subtrair(ctx:commands.Context, num1:float, num2:float):
    res = num1 - num2
    await ctx.reply(f"A subtração de {num1} com {num2} é: {num1} - {num2} = {res}")

@bot.command()
async def multiplicar(ctx:commands.Context, num1:float, num2:float):
    res = num1 * num2
    await ctx.reply(f"O produto da multiplicação é: {num1} x {num2} = {res}")

@bot.command()
async def dividir(ctx:commands.Context, num1:float, num2:float):
    res = num1 / num2
    await ctx.reply(f"O produto da divisão é: {num1} / {num2} = {res}")

@bot.command()
async def potenciar(ctx:commands.Context, num1:float, num2:float):
    res = num1 ** num2
    await ctx.reply(f"O produto da potenciação é: {num1} ^ {num2} = {res}")

@bot.command()
async def raiz_quadrada(ctx:commands.Context, num1:float):
    res = sqrt(num1)
    await ctx.reply(f"A raiz quadrada de {num1} é: {num1} = {res}")

@bot.command()
async def falar(ctx:commands.Context, *,frase): # *, identifica a frase como um argumento inteiro
    await ctx.send(frase)








@bot.event # criando um evento
async def on_ready(): # quando ele estiver on
    print("Estou pronto!")

bot.run(TOKEN) # rodando o bot