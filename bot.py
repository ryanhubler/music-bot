import discord
from discord.ext import commands
from ytdownloader import *
from ytsearch import  *
token = ''   #your token goes here
bot = commands.Bot(command_prefix='/') #Change prefix used to call bot in discord 

@bot.command()
async def play(ctx, *, mess): #play is the argument used after the user types the prefix
    isconnected = str(ctx.voice_client)
    if ctx.author.voice != None:
        if isconnected == "None":
            channel = ctx.author.voice.channel #makes the channel varible = to the channel name that the person who used the command is in 
            yt_download(search(mess))
            vc = await channel.connect() #define vc for use in the next line
            vc.play(discord.FFmpegPCMAudio("song.mp3"),after=lambda e: print('done', e)) #uses ffmpeg to play "song" aka test.mp3 
            await ctx.send("Now Playing"+ str(search(mess)))
        else:
            await leave(ctx)
            channel = ctx.author.voice.channel #makes the channel varible = to the channel name that the person who used the command is in 
            yt_download(search(mess))
            vc = await channel.connect() #define vc for use in the next line
            vc.play(discord.FFmpegPCMAudio("song.mp3"),after=lambda e: print('done', e)) #uses ffmpeg to play "song" aka test.mp3 
            await ctx.send("Now Playing" + str(search(mess)))
    else:
        await ctx.send("You are not in a voice channel")
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()  

bot.run(token)
