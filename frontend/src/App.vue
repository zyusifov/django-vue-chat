<template>
  <div id="app" class="app">
    <div class="header">
      <h2>Real time chat</h2>
    </div>
    <div class="messages" id="messages">
      <p v-for="message in messages" :key="message">
        {{ message }}
      </p>
    </div>
    <div class="toolBar">
      <input placeholder="Send message..." v-model="newMessage">
      <button v-on:click="sendMessage" >Send</button>
    </div>
  </div>
</template>

<style>
  .app{
    position: absolute;
    top: 10%;
    left: 10%;
    width: 40%;
    min-width:350px;
    border: 1px solid #cfcfcf;
    border-radius: 5px;
  }
  .header{
    display: flex;
    justify-content: space-between;
    padding-left: 30px;
    padding-right: 30px;
    text-align: center;
    background-color: #cfcfcf
  }
  .header h2{
    font-size: 28px;
    font-weight: bold;
  }
  .header p{
    font-size: 20px;
    font-weight: bold;
    color: #5d6878;
    display: inline-block;
  }
  .messages{
    padding:20px;
    font-size:18px;
    max-height:400px;
    overflow-y:scroll;
    min-height:400px;
  }
  .toolBar{
    font-size: 20px;
  }
  .toolBar input{
    font-size: 20px;
    height: 30px;
    padding:5px;
    width:80%
  }
  .toolBar button{
    font-size: 20px;
    height: 45px;
    width:15%
  }
</style>

<script>

  document.addEventListener('DOMContentLoaded', function(){
    function updateScroll(){
      var element = document.getElementById("messages");
      element.scrollTop = element.scrollHeight;
    }
    setInterval(updateScroll,500);

  });

  export default {
    name: 'App',
    data(){
      return {
        messages: [],
        newMessage: null,
        connection: null
      };
    },
    created: function() {
      let this_ = this;
      this.connection = new WebSocket("ws://127.0.0.1:8000/ws/chat/")

      this.connection.onmessage = function(event) {
        let receivedMessage = JSON.parse(event.data).message;
        this_.receiveMessage(receivedMessage)
      }
      this.connection.onopen = function(event) {
        return event
      }
    },
    methods: {
      sendMessage: function () {
        this.connection.send('{"message":"'+this.newMessage+'"}');
      },
      receiveMessage(message) {
        this.messages.push(message)
      }
    }
  }
  
</script>