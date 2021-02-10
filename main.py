import logging
import discord
from Parser import parser

try:
    fp = open('token.txt', 'r')
    TOKEN = fp.read()
except FileNotFoundError:
    print('Couldn\'t open "token.txt", please create this file!')

client = discord.Client()

COMMAND_START = '$'


@client.event
async def on_ready():
    """ Runs when bot is ready """
    print('Logged on as {}'.format(client.user))


@client.event
async def on_message(message):
    """ Runs when a message is sent """
    if message.author == client.user:
        return
    if message.content.startswith(COMMAND_START):
        txt = message.content[len(COMMAND_START):]
        await parser.parse(txt, message)

logging.basicConfig(level=logging.INFO)
client.run(TOKEN)
