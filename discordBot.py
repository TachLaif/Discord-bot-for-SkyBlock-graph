# Copyright (C) 2022 - TechLife
#
# Discord bot for SkyBlock graph (https://github.com/TachLaif/Discord-bot-for-SkyBlock-graph)
# - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 19.11.2022
#
# This work is made available under the GNU Affero General Public License v3.0.
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

import discord
import os
from dotenv import load_dotenv, find_dotenv
from main import generateGraph

load_dotenv(find_dotenv())

command_prefix = '!'
dark_mode = False

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('Logged in as a bot {0.user}'.format(client))
    print('Logged in following servers: ')
    for guild in client.guilds:
        print(str(guild))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='your bank account'))

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == command_prefix + 'graph':
        try:
            generateGraph(os.environ.get('API_KEY'), os.environ.get('PLAYER_NAME'), dark_mode)
            with open('graph.png', 'rb') as f:
                file = discord.File(f, filename = 'graph.png')
                await message.channel.send(file = file)
        except:
            await message.channel.send('Program ran into a problem while generating graph...')

client.run(os.environ.get('DISCORD_TOKEN'))
