import discord

async def ping(message, args):
    await message.channel.send('Pong!')
    return None
