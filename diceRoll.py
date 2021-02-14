import random

random.seed()


async def rollDice(message, args):
    diceinfo = args[0]
    if 'd' not in diceinfo:
        await message.channel.send('Incorrect formatting!')
        return None

    diceinfo = diceinfo.split('d')


    try:
        if diceinfo[0] == '':
            diceinfo[0] = '1'
        numDice = int(diceinfo[0])
        numSides = int(diceinfo[1])
    except ValueError:
        await message.channel.send('Incorrect formatting!')
        return None

    add = 0

    randNum = random.randrange(numSides) + 1
    rollinfo = []
    for i in range(numDice):
        num = random.randrange(numSides) + 1
        rollinfo.append(num)
        add += num

    if len(args) > 1:
        for i in range(1, len(args)):
            try:
                add += int(args[i])
                rollinfo.append(args[i])
            except ValueError:
                await message.channel.send('Incorrect formatting!')
                return None

    await message.channel.send('{} = {}'.format(rollinfo, add))
