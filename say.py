import discord

# Problems: if the message has multiple spaces in a row, I don't think it will work.

async def say(message, args):
    await message.channel.last_message.delete()
    text = " ".join(args)
    await message.channel.send(text)
    return None
