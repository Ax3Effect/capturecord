


<template>
    <div class="app">
    <link href="https://fonts.googleapis.com/css?family=Dosis" rel="stylesheet"/>   
        <div class="titleDiv"><h1>Discord Plays Capture the Flag!</h1>
        <h2> Invite link: discordflag.com/join or discord.gg/AWtZxsf</h2> </div>
        
        <div class="infoBox"><b>Info</b></br>
            Type !join to be assigned a team.<br/><br/>
            When the game starts, type movement keys (WASD) and hit enter to move.
            <br/><br/>Try to steal the enemy flag and drop it to the point.    
        </div>
        
        <div class="redChat">
        <span> Red points: {{ redPoints }}  <img src="http://discordflag.com/static/img/player_1.png"> </span>
        
        <div id="redChat">
        <div class="card-body">
            <div id="messages" >
                
                  <p v-for="(msg, index) in messages" :key="index" v-if="msg.team">{{ msg.user }}: {{ msg.message}} </p>
            </div>
        </div>
        
        </div></div>
        <div class="blueChat">
        <span> Blue points: {{ bluePoints }} <img src="http://discordflag.com/static/img/player_2.png"> </span>
        <div id="blueChat">
                <div class="card-body">
            <div id="messages" >
                
                  <p v-for="(msg, index) in messages" :key="index" v-if="!msg.team">{{ msg.user }}: {{ msg.message}} </p>
            </div>
        </div>
        
        </div></div>
  <div class="center-div">
    <table class="appGrid" cellpadding="0">
      <tbody>
        <tr v-for="(row, rowindex) in map" :key="rowindex">
          <td v-for="(col, colindex) in row" :key="colindex">
          
          <div v-if="col == 0">
          <img src="http://discordflag.com/static/img/blank_board.png">
          </div>
          <div v-if="col == 1">
          <img src="http://discordflag.com/static/img/player_1.png">
          </div>
          <div v-if="col == 2">
          <img src="http://discordflag.com/static/img/player_2.png">
          </div>
          <div v-if="col == 3">
          <img src="https://cdn.discordapp.com/attachments/516062197231910912/516063166510137377/unknown.png">
          </div>
          <div v-if="col == 4">
          <img src="http://discordflag.com/static/img/flag_1.png">
          </div>
          <div v-if="col == 5">
          <img src="http://discordflag.com/static/img/flag_2.png">
          </div>
          <div v-if="col == 6">
          <img src="https://cdn.discordapp.com/attachments/516062197231910912/516168738584788992/p1_holding_f2.png">
          </div>
          <div v-if="col == 7">
          <img src="https://cdn.discordapp.com/attachments/516062197231910912/516168753432494093/p2_holding_f1.png">
          </div>
          <div v-if="col == 8">
          <img src="https://cdn.discordapp.com/attachments/516062197231910912/516169283886252034/blue_stand.png">
          </div>
          <div v-if="col == 9">
          <img src="https://cdn.discordapp.com/attachments/516062197231910912/516169295244427279/red_stand.png">
          </div>
          </td>
            </tr>
        </tbody>
        </table>


      </div>
  </div>
</template>

<script>
import io from 'socket.io-client';
export default {
    data() {
        return {
            user: '',
            message: '',
            messages: [],
            map: [],
              rows: [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]
  ],
            redPoints: 0,
            bluePoints: 0,
            socket : io('localhost:4242')
        }
    },
    methods: {
        sendMessage(e) {
            e.preventDefault();
            
            this.socket.emit('SEND_MESSAGE', {
                user: this.user,
                message: this.message
            });
            this.message = ''
        },

          	scrollToEnd: function() {    	
        var container = this.$el.querySelector("#messages");
        container.scrollTop = container.scrollHeight;
        },

    },
    mounted() {
        this.socket.on('MESSAGE', (data) => {
            this.messages = [...this.messages, data.message];
            // you can also do this.messages.push(data)
            // eslint-disable-next-line
            console.log(data.map);
            this.scrollToEnd();

            this.map = JSON.parse(data.map);
            this.redPoints = data.redPoints;
            this.bluePoints = data.bluePoints;



        });
    }
}
</script>

<style>
</style>