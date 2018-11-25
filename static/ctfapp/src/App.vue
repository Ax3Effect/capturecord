<style>
body{
	background-color:#707070;
	background: url("http://discordflag.com/static/img/bg.png") no-repeat center center fixed;
 -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.center-div
{
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width:40vw;
  height:40vw;
  background-color: #ccc;
  border-radius: 3px;
}
.titleDiv{
  position: absolute;
  margin: auto;
  top: 0px;
  right: 0;
  text-align:center;
  left: 0;
  -webkit-text-size-adjust: none;
  width: 40vw;
  font-family: 'Dosis', sans-serif;
  color:white;
  font-size:150%;
}


table, td, th {
  border: 1px solid white;
}
.appGrid{
	width:100%;
	height:100%;
	border-radius:3px;
}

.appGrid td img, th img{
	width:100%;
	height:100%;
	user-drag: none; 
	user-select: none;
	-moz-user-select: none;
	-webkit-user-drag: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.redChat{
  position: absolute;
  margin: auto;
  bottom: 10%;
  left: 12%;
  width:15vw;
  height:20vw;
  border-radius: 10px;
  background-color: rgba(255, 0, 0, 0.3);
  padding:10px;
  padding-right:0px;
}

.blueChat{
  position: absolute;
  margin: auto;
  bottom: 10%;
  right: 12%;
  width:15vw;
  height:20vw;
  border-radius: 10px;
  background-color: rgba(0, 0, 255, 0.3);
  padding:10px;
  padding-right:0px;
}

#messages::-webkit-scrollbar {
    width: 4px;
    background-color: #F5F5F5;
} 
#messages::-webkit-scrollbar-thumb {
    background-color: #000000;
}

.blueChat div, .redChat div{
	font-size:100%; 
	color:white;
	text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;
	overflow-y:auto;
	height:100%;
	font-family: 'Dosis', sans-serif;
}

.blueChat span, .redChat span{
  color:white;
  font-size:150%; 
}

.infoBox{
  position: absolute;
  margin: auto;
  top: 10%;
  left: 12.1%;
  width:16vw;
  height:12vw;
  border-radius: 10px;
  background-color: rgba(0, 0, 0, 0.3);
  padding:10px;
  padding-right:0px;
  color:white;
}

</style>

<template>
  <div class="app" id="app">
    <div class="container">
      
         
          <Chat />
     
     
    </div>
  </div>
</template>


<script>
import Chat from './components/Chat.vue'

export default {
  name: 'app',
  components: {
    Chat
  }
}
</script>

