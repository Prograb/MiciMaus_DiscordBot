# main.py
import os
import discord
import random

TOKEN = "OTE0MjM1NzgzNjAxMzMyMjU1.YaKGbA.RdzOyjd88phmiQgx5_C994mVAps"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if 'a' in message.content.lower():
        await message.channel.send('@everyone')

client.run(TOKEN)