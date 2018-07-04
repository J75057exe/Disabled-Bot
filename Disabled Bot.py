# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
disableEnable = True
def spastify(string):
    first = ""
    spastified = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            first += string[i].upper()
        else:
            first += string[i]

    str = ""
    for x in first:
        if x == " ":
            spastified += " :wheelchair: "
        else:
            spastified += x

    return (spastified)


TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    global disableEnable
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!disableHelp'):
        msg = 'Use the command !disableDisable to disable the bot and use !disableEnable to enable it.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!disableEnable'):
        disableEnable = True
    elif message.content.startswith('!disableDisable'):
        disableEnable = False
    
    elif message.content.startswith('') and disableEnable == True:
        msg = spastify(message.content).format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
