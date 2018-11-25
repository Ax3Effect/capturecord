import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='515855255314104325')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(1) # task runs every 60 seconds

async def coolshit(game):
    while not client.is_closed:
        await asyncio.sleep(1)
        game.setRandomFlags()
            

#client.loop.create_task(my_background_task())


class Game:
    def __init__(self, server=None):
        self.on = False
        #self.server = server
        #self.emojis = server.emojis

        #print(self.emojis)
       #for i in self.emojis:
        #    print(str(i))

        self.map = [[]]
        self.resources = {
            "blank":"<:a1:515873857526300685>",
            "team1_flag":"<:b3:515926117719343133>",
            "team2_flag":"<:b2:515874545517985793>",
            "player1":"<:b3:515921895741325351>",
            "player2":"<:b4:515921895904772096>"
        }

        self.messages = None
        self.channel = None
        self.width = 15
        self.height = 15

    def setChannel(self, channel):
        self.channel = channel

    def setEmojis(self, emojis):
        self.emojis = emojis

    def getResource(self, name):
        return self.resources.get(name)

    def moveRedLeft(self):
        

    def newgame(self):

        w = 15
        h = 15
        self.map = [[0 for x in range(self.width)] for y in range(self.height)] 
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                #resource = self.getRes("blank")
                #print(resource)
                self.map[i][j] = "blank"

        self.on = True

    def getPrettyMap(self):
        #print(self.map)
        msg = ""
        x = self.map
        for i in range(len(x)):
            for j in range(len(x[i])):
                msg += self.getResource(self.map[i][j])
                #msg += self.getResource("blank")
            msg += "\n"
        
        return msg

    def getFormattedMap(self):
        msg_list = game.getPrettyMap().split("\n")

        messages = []
        count = 0
        smsg = ""
        for i in msg_list:
            smsg += i + "\n"
            #print(smsg)
            count += 1
            if count == 3:
                messages.append(smsg)
                count = 0
                smsg = ""

        return messages

    async def editMessages(self, messages):
        if self.messages != None:
            for counter, i in enumerate(messages):
                print("a editing {}".format(counter))
                await client.edit_message(self.messages[counter], i)

    async def sendMap(self, messages):
        edited_msg = []

        for msg in messages:
            tmp = await client.send_message(self.channel, msg)
            edited_msg.append(tmp)

        self.messages = edited_msg

        #print(edited_msg)
        #await client.edit_message(edited_msg[2], "succ")

    def change(self, x, y, t):
        self.map[x][y] = t

    def addFlag(self, x, y, flag):
        print("adding a flag")
        self.map[x][y] = "team1_flag"
        #self.change(x, y, "team1_flag")

    async def editOneMessage(self, id, message):
        await client.edit_message(self.messages[id], message)

    def setRandomFlags(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)

        self.map[x][y] = "player1"
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)

        self.map[x][y] = "player2"

    def isOn(self):
        return self.on

    
        

game = Game()
game.newgame()


@client.event
async def on_message(message):

    

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} {} messages.'.format(counter, message.channel))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    if message.content.startswith("!map"):
        game.setChannel(message.channel)
        await game.sendMap()

    if message.content.startswith("!new"):
        game.newgame()
        game.setChannel(message.channel)
        messages = game.getFormattedMap()
        await game.sendMap(messages)

    if message.content.startswith("!flag"):
        game.addFlag(5, 5, "")
        game.addFlag(1, 1, "")


    if message.content.startswith("succ"):
        client.loop.create_task(coolshit(game))

    if message.content.startswith("printemoji"):
        for i in message.server.emojis:
            print(str(i))
    


async def update_map(game):
    await client.wait_until_ready()
    counter = 0
    channel = game.channel
    tmp = game.getFormattedMap()
    while not client.is_closed:
        #print(game.getFormattedMap())
        print("editing")

        new_tmp = game.getFormattedMap()
        for counter, i in enumerate(new_tmp):

            if new_tmp[counter] != tmp[counter]:
                await game.editOneMessage(counter, new_tmp[counter])
                


        #messages = game.getFormattedMap()
        #print(messages)
        #await game.editMessages(messages)
        
        if tmp != game.getFormattedMap():
            print("OH SHIT SOMETHING CHANGED")

        tmp = game.getFormattedMap()
        '''            
        messages = game.getFormattedMap()
            game.editMessages(messages)
            tmp = game.getFormattedMap()
        '''

        #game.setRandomFlags()
        await asyncio.sleep(2)


client.loop.create_task(update_map(game))


client.run("NTE1ODU1NDQ5NDk3Nzk2NjE5.DtrLzw.9uxiqIZZTO30aTJtBkDzaMWiWhY")




    