import discord
import diceRoll
import ping
import say

commandsList = {}


class Commands:
    async def command(self, command, args, message):
        await commandsList[command](message, args)
        return

    async def find(self, command, message):
        try:
            ret = commandsList[command]
        except Exception:
            print('No such command {}'.format(command))
            print('Commands: {}'.format(commandsList))
            return None
        return ret

    def addCommand(self, command, func):
        """  Pass Command (string), func (function) """
        commandsList[command] = func
        return

commands = Commands()

commands.addCommand('roll', diceRoll.rollDice)
commands.addCommand('ping', ping.ping)
commands.addCommand('say', say.say)
