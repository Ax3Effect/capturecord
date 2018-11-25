from flask import Flask, render_template, send_from_directory, redirect
from flask_socketio import SocketIO
from flask_socketio import send, emit
import threading
app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

import discord
import asyncio
import random
import json

loop = asyncio.get_event_loop()

client = discord.Client()

class ServerGame:
    def __init__(self):
        self.map = [[]]
        self.width = 15
        self.height = 15

        self.generate_map()
        self.red_team = []
        self.blue_team = []
        self.red_x = 3
        self.red_y = 3
        self.blue_x = 9
        self.blue_y = 9
        self.players = []

        self.redflag_x = 4
        self.redflag_y = 4
        self.blueflag_x = 13
        self.blueflag_y = 13

        self.redCarrying = False
        self.blueCarrying = False

        self.dropred_x = 7
        self.dropred_y = 7

        self.dropblue_x = 8
        self.dropblue_y = 8

        self.redPoints = 0
        self.bluePoints = 0 

        self.started = False

    def add_player(self, player):
        if player in self.red_team or player in self.blue_team:
            return None

        if len(self.blue_team) >= len(self.red_team):
            self.red_team.append(player)
            return "red"
        else:
            self.blue_team.append(player)
            return "blue"

    def add_player_team(self, player, team):
        if team == "red":
            self.red_team.append(player)
        if team == "blue":
            self.blue_team.append(player)


    def generate_map(self):
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j] = 0


    def clear(self, x, y, team):
        print(x)
        print(y)
        if self.red_x == self.blue_x and self.red_y == self.blue_y:
            if team == "red":
                self.map[x][y] = 2
            elif team == "blue":
                self.map[x][y] = 1
        else:
            self.map[x][y] = 0

    def setPlayer(self, team):

        
        if team == "red":
            if self.redCarrying:
                self.map[self.red_x][self.red_y] = 6
            else:
                self.map[self.red_x][self.red_y] = 1
        if team == "blue":
            if self.blueCarrying:
                self.map[self.blue_x][self.blue_y] = 7
            else:
                self.map[self.blue_x][self.blue_y] = 2
        
    def move(self, direction, team, message=None):
        self.reset_map()
        if team == "red":
            #self.clear(self.red_x, self.red_y, "red")
            if direction == "right":
                if self.red_y < self.width-1:
                    self.red_y += 1
                    
            if direction == "left":
                if self.red_y > 0:
                    self.red_y -= 1
            if direction == "up":
                if self.red_x > 0:
                    self.red_x -= 1
            if direction == "down":
                if self.red_x < self.height-1:
                    self.red_x += 1


            
            #touching blue flag

            self.setPlayer("red")
                


        if team == "blue":
            #self.clear(self.blue_x, self.blue_y, "blue")
            if direction == "right":
                if self.blue_y < self.width-1:
                    self.blue_y += 1
                    
            if direction == "left":
                if self.blue_y > 0:
                    self.blue_y -= 1
            if direction == "up":
                if self.blue_x > 0:
                    self.blue_x -= 1
            if direction == "down":
                if self.blue_x < self.height-1:
                    self.blue_x += 1

            #touching red flag

            
            self.setPlayer("blue")
            


        
        self.gameplay_checks()
        self.set_everything()
        self.update(message, False)
        print("Red x: {} y: {} flag: {} | Blue x: {} y: {} flag: {}".format(self.red_x, self.red_y, self.redCarrying, self.blue_x, self.blue_y, self.blueCarrying))
        print("Red Flag: x: {} y: {} Blue flag: x: {} y: {}".format(self.redflag_x, self.redflag_y, self.blueflag_x, self.blueflag_y))


    def init_teams(self):
        self.map[self.red_x][self.red_y] = 1
        self.map[self.blue_x][self.blue_y] = 2

        self.map[self.redflag_x][self.redflag_y] = 4
        self.map[self.blueflag_x][self.blueflag_y] = 5

    def reset_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j] = 0

    def set_everything(self):
        self.reset_map()

        if self.red_x == self.blueflag_x and self.red_y == self.blueflag_y:
            self.redCarrying = True

        if self.blue_x == self.redflag_x and self.blue_y == self.redflag_y:
            self.blueCarrying = True

        # Set flags first
        self.stay_flag()

        # Set players and players carrying flags
        if self.redCarrying:
            self.map[self.red_x][self.red_y] = 6
        else:
            self.map[self.red_x][self.red_y] = 1

        if self.blueCarrying:
            self.map[self.blue_x][self.blue_y] = 7
        else:
            self.map[self.blue_x][self.blue_y] = 2

        if(self.blue_x==self.red_x and self.blue_y==self.red_y):
            self.map[self.red_x][self.red_y] = 3
            
            if self.redCarrying == True:
                self.reset_flag("red")
                self.redCarrying = False
            if self.blueCarrying == True:
                self.reset_flag("blue")
                self.blueCarrying = False

        # Set dropoffs
        self.dropoffs()





        




    def stay_flag(self):
        if self.blueCarrying == False:
            self.map[self.redflag_x][self.redflag_y] = 4
        if self.redCarrying == False:
            self.map[self.blueflag_x][self.blueflag_y] = 5
        
    def reset_flag(self, team):
        self.map[self.redflag_x][self.redflag_y] = 0
        self.map[self.blueflag_x][self.blueflag_y] = 0

        if team == "red":
            self.redflag_x = 1
            self.redflag_y = random.randint(1, 10)
        if team == "blue":
            self.blueflag_x = 13
            self.blueflag_y = random.randint(1, 10)

    def gameplay_checks(self):
        if self.red_x == self.dropred_x and self.red_y == self.dropred_y:
            self.redCarrying = False
            self.reset_flag("blue")
            self.redPoints += 1
        if self.blue_x == self.dropblue_x and self.blue_y == self.dropblue_y:
            self.blueCarrying = False
            self.reset_flag("red")
            self.bluePoints += 1

    def dropoffs(self):
        if self.redCarrying:
            # show dropoff for red
            self.map[self.dropred_x][self.dropred_y] = 8
        if self.blueCarrying:
            # show dropoff for blue
            self.map[self.dropblue_x][self.dropblue_y] = 9



    def to_json(self):
#
        return json.dumps(self.map)

    def update(self, message=None, ignore = True):
        
        if ignore == True:
            socketio.emit('MESSAGE', {'user': '', "message": {"user": "Discord", "message":"Game has started!"}, "map":game.to_json(),
            "redPoints":self.redPoints, "bluePoints":self.bluePoints})
        else:
            msg = "{}: {}".format(str(message.author), message.content)
            team = self.getPlayerTeam(message.author)
            if not team:
                team = True

            if team == "red":
                team = True
            if team == "blue":
                team = False
            
            print(msg)
            socketio.emit('MESSAGE', {'user': '', "message": {"user": str(message.author), "message":str(message.content), "team":team}, "map":game.to_json(),
            "redPoints":self.redPoints, "bluePoints":self.bluePoints})

    def start_game(self):
        if self.started == False:
            self.generate_map()
            self.init_teams()
            self.reset_flag("red")
            self.reset_flag("blue")
            self.update(None, ignore=True)
            self.started = True
            return True
        return False

    def getPlayerTeam(self, player):
        if player in self.red_team:
            return "red"
        elif player in self.blue_team:
            return "blue"
        else:
            return None





        
    


game = ServerGame()



@client.event
async def on_message(message):
    #print(message.content)
    #print(message.channel)
    #print(game.to_json())
    #socketio.emit('MESSAGE', {'user': '', 'message': '{}'.format(message.content), "map":game.to_json()})
    #{'user': 'asdasd', 'message': 'dfghdfghfdgh'}
    if message.content.startswith('!test'):
        #socketio.emit('some event', {'data': 42})
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} {} messages.'.format(counter, message.channel))

    if message.content.startswith("!join"):
        team = game.add_player(message.author)
        if team:
            await client.send_message(message.channel, "{}, You're on {} team!".format(message.author, team))

    if message.content.startswith("!start"):
        game.start_game()

    if message.content.startswith("d"):
        t = game.getPlayerTeam(message.author)
        if t:
            game.move("right", t, message)

    if message.content.startswith("s"):
        t = game.getPlayerTeam(message.author)
        if t:
            game.move("down", t, message)

    if message.content.startswith("a"):
        t = game.getPlayerTeam(message.author)
        if t:
            game.move("left", t, message)

    if message.content.startswith("w"):
        t = game.getPlayerTeam(message.author)
        if t:
            game.move("up", t, message)


    if message.content.startswith("assignRoles"):
        for i in message.server.members:
            for y in i.roles:
                if y in "Red Team":
                    game.add_player_team(i, "red")
                if y in "Blue Team":
                    game.add_player_team(i, "blue")


                    
@app.route('/dist/<path:path>')
def send_js(path):
    return send_from_directory('dist', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/join")
def redirectjoin():
    return redirect("https://discord.gg/AWtZxsf", code=302)



 
@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

token = "NTE1ODU1NDQ5NDk3Nzk2NjE5.DtrLzw.9uxiqIZZTO30aTJtBkDzaMWiWhY"

t = threading.Thread(target=client.run, args=(token,))
t.start()

if __name__ == '__main__':
    #t = threading.Thread(target=worker)
    #t.start()
    #client.run("NTE1ODU1NDQ5NDk3Nzk2NjE5.DtrLzw.9uxiqIZZTO30aTJtBkDzaMWiWhY")
    #loop.run_until_complete(worker())
    socketio.run(app, host='0.0.0.0', port=4242, debug=False)





