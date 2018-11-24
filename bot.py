import discord
import asyncio

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

#client.loop.create_task(my_background_task())


class Game:
    def __init__(self, server=None):
        #self.server = server
        #self.emojis = server.emojis

        #print(self.emojis)
       #for i in self.emojis:
        #    print(str(i))

        self.map = [[]]
        self.resources = {
            "blank":"<:a1:515873857526300685>",
            "team1_flag":"<:b1:515874378282565647>",
            "team2_flag":"<:b2:515874545517985793>"
        }

        self.messages = None
        self.channel = None

    def setChannel(self, channel):
        self.channel = channel

    def setEmojis(self, emojis):
        self.emojis = emojis

    def getResource(self, name):
        return self.resources.get(name)

    def newgame(self):
        w = 15
        h = 15
        self.map = [[0 for x in range(w)] for y in range(h)] 
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                #resource = self.getRes("blank")
                #print(resource)
                self.map[i][j] = "blank"

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
        await client.send_message(message.channel, "<:game_tile:515873857526300685>")


async def update_map(game):
    await client.wait_until_ready()
    counter = 0
    channel = game.channel
    tmp = game.getPrettyMap()
    while not client.is_closed:
        #print(game.getFormattedMap())
        print("editing")
        messages = game.getFormattedMap()
        #print(messages)
        await game.editMessages(messages)
        
        if tmp != game.getFormattedMap():
            print("OH SHIT SOMETHING CHANGED")

        tmp = game.getFormattedMap()
        '''            
        messages = game.getFormattedMap()
            game.editMessages(messages)
            tmp = game.getFormattedMap()
        '''
        await asyncio.sleep(2)
            
client.loop.create_task(update_map(game))










client.run("NTE1ODU1NDQ5NDk3Nzk2NjE5.DtrLzw.9uxiqIZZTO30aTJtBkDzaMWiWhY")




    