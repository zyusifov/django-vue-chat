<template>
  <div id="app" class="app">
    <div class="header">
      <h2>Real time chat</h2>
    </div>
    <div class="messages" id="messages">
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
      <p>I send this message</p>
    </div>
    <div class="toolBar">
      <input placeholder="Send message..."/>
      <button>Send</button>
    </div>
  </div>
</template>

<style>
  .app{
    position: absolute;
    top: 10%;
    left: 10%;
    width: 800px;
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
  }
  .toolBar{
    font-size: 20px;
  }
  .toolBar input{
    font-size: 20px;
    height: 30px;
    padding:5px;
    width:83%
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
</script>