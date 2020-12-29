import discord
import ffmpeg #used for playback dont know if its actully needs to be imported 
import os #used for deleting old test.mp3
import youtube_dl #downloads songs from youtube using link provided by youtubesearchpython
from youtubesearchpython import * #used to take user input and search youtube and returns url to be used by youtube_dl
from discord.ext import commands
ydl_opts = {
    'outtmpl': '/home/ryan/custommusic/test.mp3', #names downloaded file test.mp3 and places it in desired directory
    'format': 'bestaudio/best', #quality settings
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
token = 'yourTOKEN'   #your token goes here
bot = commands.Bot(command_prefix='/') #Change prefix used to call bot in discord 
@bot.command()
async def play(ctx, *, mess): #play is the argument used after the user types the prefix
    channel = ctx.author.voice.channel #makes the channel varible = to the channel name that the person who used the command is in 
    os.remove("test.mp3") #deletes old music file before new one is downloaded by youtube_dl
    videosSearch = VideosSearch(mess, limit = 1, language = 'en', region = 'US') #takes mess(user input from discord) and searched youtube and returns a messed up dictonary 
    results= videosSearch.result(mode = ResultMode.dict) #makes the output of the search a dict 
    unfinishedlink = str(results['result']).strip('[]') #remove the messed up parts of the returned dict form the search results
    link = eval(unfinishedlink) #makes the varible unfinisedlink back into a dict (could technicly be unsafe)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #youtube_dl stuff
        ydl.download([link['link']]) #the [link['link]] returns a url that is stored in the dict link (can be confusing needs updated)
    song = "test.mp3" #varible used to store the song name not needed as you could just put it directly into the vc.play... 
    vc = await channel.connect() #define vc for use in the next line
    vc.play(discord.FFmpegPCMAudio(song), after=lambda e: print('done', e)) #uses ffmpeg to play "song" aka test.mp3 
    
'''
#not working at the moment
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
'''
bot.run(token)

