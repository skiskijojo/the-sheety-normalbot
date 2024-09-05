import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print("I WILL WIN!!!")


@bot.command()
async def hello(ctx):
    await ctx.reply('hyeoooo!')


@bot.command()
async def rps(ctx, message):
    answer = message.lower()
    choice = ["rock", "paper", "scissors"]
    computers_answer = random.choice(choice)
    if answer not in choice:
        await ctx.reply("SO INVALID!!!!, please choose anything, and lowercase, STUPID!!!!!!")
    else:
        if computers_answer == answer:
            await ctx.reply("Its tie.")
        if computers_answer == "rock":
            if answer == "paper":
                await ctx.reply(f"Unfainr!!!!! (i choosed {computers_answer} and you chose {answer})")
        if computers_answer == "rock":
            if answer == "scissors":
                await ctx.reply(f"You loose GHHAHAHA!!! (i choosed {computers_answer} and you chose {answer})")
        if computers_answer == "paper":
            if answer == "rock":
                await ctx.reply(f"YOU LOOSE!!!! (i choosed {computers_answer} and you chose {answer})")
        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.reply(f"Nooooo cheater!!!! (i choosed {computers_answer} and you chose {answer})")
        if computers_answer == "scissors":
            if answer == "rock":
                await ctx.reply(f"YOU ARE CHEATER!!!! (i choosed {computers_answer} and you chose {answer})")
        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.reply(f"YOU LOOSE!!!! HAHAHAHA! (i choosed {computers_answer} and you chose {answer})")

bot.run('go put your bot token here, you stoopid')
