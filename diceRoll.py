import random

random.seed()


async def rollDice(message, args):
    if args[0][0] == 'd':
        args[0] = '1' + args[0]
    if args[0][1] != 'd':
        await message.channel.send('No letter \'d\'!')
        return None
    
    diceInfo = []
    for i in range(len(args[0])):
        diceInfo.append(args[0][i].split('d'))
    
    try:
        numDice = int(diceInfo[0][0])
    except ValueError:
        await message.channel.send('{} is not a valid argument!'
                                   .format(diceInfo[0]))
        return None

    sides = diceInfo[2]

    add = 0
    output = []
    for i in range(numDice):
        output.append(random.randint(1, int(sides[0])))
        add += output[i]

    if len(args) > 1:
        for i in range(1, len(args)):
            output.append(args[i])
            try:
                add += int(args[i])
            except ValueError:
                await message.channel.send('{} is not a valid argument!'
                                           .format(args[i]))
                return None

    await message.channel.send('{0} = {1}'.format(output, add))

    return None
