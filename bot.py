import discord
from discord.ext import commands
from ytdownloader import *
from ytsearch import  *
from songqueue import *
import asyncio
token = ''   #your token goes here
bot = commands.Bot(command_prefix='/') #Change prefix used to call bot in discord 

@bot.command()
async def play(ctx,*,mess): #play is the argument used after the user types the prefix
    if ctx.author.voice != None:
        music_queue(mess)
        channel = ctx.author.voice.channel #makes the channel varible = to the channel name that the person who used the command is in 
        vc = await channel.connect() #define vc for use in the next line
        while len(songs) != 0:
            new_song = songs.pop(0)
            yt_download(search(new_song))
            vc.play(discord.FFmpegPCMAudio("song.mp3"),after=lambda e: print('done', e)) #uses ffmpeg to play "song" aka test.mp3 
            await ctx.send("Now Playing"+ str(search(new_song)))
            await asyncio.sleep(int(time_search(new_song)) + 3)
        if len(songs) == 0:
            await leave(ctx)   
    else:
        await ctx.send("You are not in a voice channel or a voice channel I cannot access")
@bot.command()
async def queue(ctx, *, mess):
    music_queue(mess)
    print(len(songs))

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel #makes the channel varible = to the channel name that the person who used the command is in 
    vc = await channel.connect() #define vc for use in the next line
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect() 
    
bot.run(token)
