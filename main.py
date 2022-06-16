import random
import asyncio
import discord
from discord.ext import commands
import youtube_dl, os, downloadMp3
TOKEN = "OTE0MjM1NzgzNjAxMzMyMjU1.YaKGbA.RdzOyjd88phmiQgx5_C994mVAps"

#TODO find a way to increase video download speeds

bot = commands.Bot(command_prefix='mici ')
players = {}
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@commands.has_permissions(kick_members=True)
@bot.command(name="kick", breif="  kick member from server")
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@commands.has_permissions(ban_members=True)
@bot.command(name="ban", brief="  ban user from server")
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.ban(reason=reason)
    ban = discord.Embed(title=f":boot: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)

#made by vonor22#7289
#C:\ffmpeg\bin

@bot.command(name="earrape")
async def earrape(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./baseSongs/mundian.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    await ctx.message.delete()

@bot.command(name="baga-o-manea", brief="  baga o manea s u s p e c t a")
async def manea(ctx):
    manele = ["./baseSongs/TunakTunakTun.mp3", "./baseSongs/aragaz cu butelie.mp3", "./baseSongs/zarzavat.mp3", "./baseSongs/sms.mp3", "./baseSongs/mundian.mp3"]

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(random.choice(manele))
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@bot.command(name="hooo-baaa")
async def stop(ctx):
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients)
    voice_client.pause()
    await ctx.send("👍")

@bot.command(name="mai-tare-baaa")
async def resume(ctx):
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients)
    voice_client.resume()
    await ctx.send("👍")

@bot.command(description="Mutes a specrified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.add_roles(mutedRole)
    await ctx.send(f"Muted {member}")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

   await ctx.send("👍")

@bot.command(name="intra")
async def intra(ctx):
    channel = ctx.author.voice.channel

    await channel.connect()
    await ctx.send("👍")

@bot.command(name="pleaca")
async def pleaca(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("👍")

@bot.command(name="baga", brief="  baga muzik de pe iutub lel")
async def baga(ctx, url_ : str):
    await ctx.send("👍")
    downloadMp3.process(url=url_)
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio("song.mp3")
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

bot.run(TOKEN)
