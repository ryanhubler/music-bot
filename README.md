# Music-Bot

Music bot is a discord bot written in python3.

## Installation and Dependency's 

Clone the music-bot repository 

```bash
https://github.com/ryanhubler/music-bot.git
```
Discord.py
```bash
pip3 install discord.py
```
Youtube_dl
```bash
pip3 install youtube_dl
```
Youtube-Search-Python
```bash
pip3 install youtube-search-python
```
FFMPEG
```bash
sudo apt install ffmpeg
```
## Usage
The bot uses / to be called in Discord, however it can be changed easily in this line
```python
bot = commands.Bot(command_prefix='/') #Change prefix used to call bot in discord 
``` 
1. To use the bot in discord you must create a bot in the discord developer portal and add its token to this line
```python
token = ''   #your token goes here
``` 
2. Once your bot is in discord run bot.py
3. Then in discord play a song by being in a voice channel and typing /play <songname> in a text channel
4. To make the bot leave your voice channel type /leave in a text channel


## License
[MIT](https://choosealicense.com/licenses/mit/)
