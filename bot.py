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
        w = 16
        h = 16
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
                #msg += self.getResource(self.map[i][j])
                msg += self.getResource("blank")
            msg += "\n"
        
        return msg

    def sendMap(self):
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

        print(messages)

        edited_msg = []

        for msg in messages:
            tmp = await client.send_message(message.channel, msg)
            edited_msg.append(tmp)

        self.messages = edited_msg

        print(edited_msg)
        await client.edit_message(edited_msg[2], "succ")

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
        
        print(message.server.emojis)
        for i in message.server.emojis:
            
            print(str(i))
        '''
        print(message.server.emojis)
        print(message.server.id)
        for i in message.server.emojis:
            
            print("{}:{}".format(i.name, i.id))
        '''
        print(game.getPrettyMap())
        '''
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        embed.add_field(name="t", value=game.getPrettyMap(), inline=False)
        embed.add_field(name="t", value=game.getPrettyMap(), inline=False)

        await client.send_message(message.channel, embed=embed)
        '''
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

        print(messages)



        edited_msg = []

        for msg in messages:
            tmp = await client.send_message(message.channel, msg)
            edited_msg.append(tmp)

        print(edited_msg)
        await client.edit_message(edited_msg[2], "succ")

    if message.content.startswith("!new"):
        game.newgame()
        game.setChannel(message.channel)



    if message.content.startswith("succ"):
        await client.send_message(message.channel, "<:game_tile:515873857526300685>")












client.run("NTE1ODU1NDQ5NDk3Nzk2NjE5.DtrLzw.9uxiqIZZTO30aTJtBkDzaMWiWhY")




    