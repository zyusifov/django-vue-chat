<template>
  <div id="app">
    <h2>Real-time chat</h2> 
    <button v-on:click="sendMessage('hello')">Send Message</button>
  </div>
</template>

<style>

</style>

<script>
    export default {
    name: 'App',
    data: function() {
        return {
        connection: null
        }
    },
    methods: {
      sendMessage: function(message) {
        console.log(message)
        this.connection.send('{"message": "hello dunya"}');
      }
    },
    created: function() {
        this.connection = new WebSocket("ws://127.0.0.1:8000/ws/chat/")
        this.connection.onmessage = function(event) {
          console.log(event);
        }

        this.connection.onopen = function(event) {
          console.log(event)
        }

    }
    }
</script>