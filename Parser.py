from Commander import commands


class Parser:
    async def parse(self, txt, message):
        """ Pass command (string) and message (obj) to run the command """
        commandList = txt.split(' ')
        if await commands.find(commandList[0], message) is None:
            await message.channel.send('That isn\'t a command!')
            return None
        await commands.command(commandList[0], commandList[1:], message)
        return


parser = Parser()
