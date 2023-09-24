# Discord bot for SkyBlock graph
<a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/python-3.11.0-success?style=for-the-badge&logo=python&logoColor=white"></img></a>
<img src="https://img.shields.io/badge/Last%20update-17.03.2023-blue?style=for-the-badge"></img>
<a href="https://github.com/TachLaif/Discord-bot-for-SkyBlock-graph/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TachLaif/Discord-bot-for-SkyBlock-graph?style=for-the-badge"></img></a>

## Description

Optional program which uses my Bank graph for Hypixel Skyblock program and connects it to a Discord bot which sends the graph to you when you type a command.

**This repository requires the <a href="https://github.com/TachLaif/Bank-graph-for-Hypixel-Skyblock">Bank graph for Hypixel SkyBlock</a> in order to work!** 

## Table of Contents
- <a href="#description">Description</a>
- <a href="#table-of-contents">Table of Contents</a>
- <a href="#how-to-install">How to install</a>
  - <a href="#installing-the-libraries">Installing the libraries</a>
  - <a href="#installing-the-required-repositories">Installing the required reopsitories</a>
  - <a href="#how-to-get-a-discord-bot-token">How to get a Discord bot Token</a>
  - <a href="#editing-the-env-file">Editing the .env file</a>
- <a href="#how-to-use">How to use</a>
- <a href="#how-it-works">How it works</a>
- <a href="#tests-and-results">Tests and results</a>
- <a href="#license-and-credits">License and credits</a>

## How to install
- <a href="https://www.python.org/downloads/release/python-3110/">Python 3.11.0</a>
- <a href="https://pypi.org/project/discord.py/">discord.py</a>
- <a href="https://pypi.org/project/python-dotenv/">dotenv</a>
- os
- <a href="https://github.com/TachLaif/Bank-graph-for-Hypixel-Skyblock">Bank graph for Hypixel SkyBlock</a>
- Discord Bot Token

### Installing the libraries

The libraries can be installed with pip by using this command:

```cmd
pip install discord.py python-dotenv
```

The library __os__ is preinstalled with Python 3.11.0.

You can also install them with __requirements.txt__.

### Installing the required repositories

**Download and install <a href="https://github.com/TachLaif/Bank-graph-for-Hypixel-Skyblock">Bank graph for Hypixel SkyBlock</a> (Installation instructions are in the linked repository).** 

Then download this repository as a .zip file and unzip it to a folder.

Copy and paste __discordBot.py__ and __.env__ in the folder you extracted while you installed <a href="https://github.com/TachLaif/Bank-graph-for-Hypixel-Skyblock">Bank graph for Hypixel SkyBlock</a>.

Your folder structure now should look like this:

```
\Bank-graph-for-Hypixel-Skyblock-main (or however you called your main directory)
  \data
    - readme.txt
  - main.py
  - discordBot.py
  - .env
  - (OPTIONAL LICENSE, README.md AND requirements.txt)
```

### How to get a Discord bot Token

In order to get a Bot Token you have to create a new Bot in the <a href="https://discordapp.com/developers/">Discord Developer Portal</a>.

To do that register there and then under the tab 'Applications' click on 'New Application'

![discord bot 1](https://user-images.githubusercontent.com/104715363/202405430-dc98ae79-c6c6-483c-8fca-6486aee3df1a.png)

Give your Application a name and create it.

![discord bot 2](https://user-images.githubusercontent.com/104715363/202405510-b4c8a19d-a623-4500-bac4-c813caf02688.png)

In the bot tab of your application you have to click 'Add bot' and confirm you choice in the pop-up window.

![discord bot 3](https://user-images.githubusercontent.com/104715363/202405538-096f6f35-3d36-4dd6-af64-d4d594056ed6.png)

After you did that click on 'Reset Token' to get a new Token.

![discord bot 4](https://user-images.githubusercontent.com/104715363/202405579-5789b2c7-6b3a-467f-a20f-8c41c9a71e2e.png)

When you scroll down in the bot tab, you will see a category named 'Privileged Gateway Intents' where you have to enable 'MESSAGE CONTENT INTENT' and save the changes you made.

![discord bot 5](https://user-images.githubusercontent.com/104715363/202405620-ed1c2978-124c-46a9-9a3d-48464f936d54.png)

To invite your bot to a server you have to generate a link. To do that go to 'OAuth2' and 'URL Generator'.

![discord bot 6](https://user-images.githubusercontent.com/104715363/202405656-76690f8c-c62f-47a5-9bfa-594a8d473378.png)

Under the 'Scopes' category you have to enable 'bot' and under the 'General permissions' enable 'Read Messages/View Channels' and 'Send Messages'. Then you can copy the Generated URL to your browser and invite the Bot to one of your servers. 

![discord bot 7](https://user-images.githubusercontent.com/104715363/202405770-7c970246-3147-44c2-8b47-22ade87a6bff.png)
![discord bot 8](https://user-images.githubusercontent.com/104715363/202405765-1a3b004e-0744-4f2f-875e-37939b06cec6.png)

### Editing the .env file

The __.env__ file is a safe way of storing your (secret) variables like the Bot Token or your Hypixel API Key for your program. 

When you open the __.env__ file you will see the following:

```.env
DISCORD_TOKEN="[YOUR DISCORD BOT TOKEN HERE]"
API_KEY="[YOUR HYPIXEL API KEY HERE]"
PLAYER_NAME="[YOUR MINECRAFT PLAYER NAME HERE]"
```

This is where you have to put your Discord Bot Token, Hypixel API key and your Minecraft Player NAME so that the program can use them later.

## How to use

After you installed the program and set everything up you can run the program. You should see that the previously offline bot is now online and you can start writing messages to it.

When you write '!graph' the program will generate a graph of your SkyBlock Bank Balance and send it to the channel you send the command to.

There are two ways you can customize the program. When you open __discordBot.py__ you will see these two lines:

```python
command_prefix = '!'
dark_mode = False
```

'command_prefix' is the prefix the bot uses to destinguish commands from messages. You can change it to something else (e.g. '$' or '?') which can be very useful when you have a server with many different bots. 

'dark_mode' specifies if the program should create and send the graph in dark or in light mode. It is set to light mode by default. Change False to True to generate dark mode graphs instead.

**Be aware that you have to terminate and rerun the program for changes to take affect.**

## How it works

```python
load_dotenv(find_dotenv())
```

In the beginning this program loads the contents in the .env file so that it can use them later. Then it defines some basic stuff like the command prefix used by the bot to recognize a command or if the generated graph should be in dark mode or not. 

```python
command_prefix = '!'
dark_mode = False
```

Afterwards it sets up the Discord Message intents so that the Bot can read and react to messages.

```python
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
```

The the two events the bot has are defined.

The first event is when the program connects to Discord to start up the bot. In this event the program prints out when the the connection is established and it prints out the names of the servers it is connected to. Here the Bot also changes its status to "Watching your bank account".

```python
@client.event
async def on_ready():
    print('Logged in as a bot {0.user}'.format(client))
    print('Logged in following servers: ')
    for guild in client.guilds:
        print(str(guild))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='your bank account'))
```

In the second event the bot gets the messages sent and processes them. It starts by checking if the message was sent by a bot and if it was sent by a bot it ignores the message.

```python
if message.author.bot:
    return
```

Then it checks if the message contains the command graph with the predetermined command prefix. To make sure that the command is not case-sensitive the program converts the message to lowercase, which means that it does not matter if you write __!graph__, __!GRAPH__ or something in between. When this command is recognized by the program it tries to generate a graph using the informations given by the .env file. When the graph was successfully built the Discord bot sends it to the channel it recieved the command from, however if generating the graph failed it sends an error message instead.

```python
if message.content.lower() == command_prefix + 'graph':
    try:
        generateGraph(os.environ.get('API_KEY'), os.environ.get('PLAYER_NAME'), dark_mode)
        with open('graph.png', 'rb') as f:
            file = discord.File(f, filename = 'graph.png')
            await message.channel.send(file = file)
    except:
        await message.channel.send('Program ran into a problem while generating graph...')
```

At the end it starts a Bot using your Discord bot Token.

```python
client.run(os.environ.get('DISCORD_TOKEN'))
```

## Tests and results 

Program tested with **Python 3.11.0**.

## License and credits

This work is made available under the <a href="https://github.com/TachLaif/Discord-bot-for-SkyBlock-graph/blob/main/LICENSE">**GNU Affero General Public License v3.0**</a>.

Project made by **<a href="https://github.com/TachLaif">TechLife</a>**.
<br><br><a href="https://discord.com"><img src="https://img.shields.io/badge/TechLife-@techlife-informational?style=for-the-badge&logo=discord&logoColor=white"></a><br><a href="https://twitter.com/_Tech4Life_"><img src="https://img.shields.io/badge/Twitter-@__Tech4Life__-informational?style=for-the-badge&logo=twitter&logoColor=white"></a><br><a href="https://www.buymeacoffee.com/TechLife"><img src="https://img.shields.io/badge/Buy%20me%20a-coffee-red?style=for-the-badge&logo=buymeacoffee&logoColor=white" title="I like coffee!"></a>
