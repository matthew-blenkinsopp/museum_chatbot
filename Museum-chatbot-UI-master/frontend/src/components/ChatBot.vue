<template>
<div class="background">
  <div class="container mt-4 c">
      <div class="bg-gray-800 text-white chat">
          <div class="chat-title flex space-between">
              <h1 class="w-9/12">Museum bot</h1>
              <v-switch
              class="w-3/12"
                dark
                v-model="sk"
                :label="`current mode: ${sk ? 'ML Model' : 'Manual'}`"
                ></v-switch>
          </div>
          
          <div class="chat-content">

              <div v-for="(text,index) in chatTexts" :key="index" 
                :class="text.generated_by_bot ? 'flex px-5 my-2':'flex flex-row-reverse px-5 my-2'">
                <div :class="text.generated_by_bot? 'bot-text-card':'person-text-card'">
                    <div v-if="text.generated_by_bot" v-html="text.text"></div>
                    <div v-else>{{text.text}}</div>
                </div>
              </div>
          </div>
          <div class="chat-input p-2">
              <div class="flex justify-between">
                <input v-on:keyup.enter='sendText' type="text" placeholder="Type your question..."  v-model="inputText" class="w-10/12 mx-2">
                <button class="send-btn lg:w-1/12 w-2/12 mx-4 hover:bg-green-600 bg-green-500" :disabled="botTyping || inputText==''" @click="sendText">send</button>
              </div>
          </div>
      </div>
  </div>
</div>
      
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return{
            sk:false,
            csrftoken:"",
            inputText:"",
            botTyping:false,
            chatTexts:[
                {text:"Hello",generated_by_bot:false},
                {text:"Hello, How may I assist you ?",generated_by_bot:true},
            ]
        }
    },
    methods:{
        sendText(){
            if (this.inputText == ""){
                return;
            }
            this.botTyping = true;
            let bodyFormData = new FormData();
            bodyFormData.append('text', this.inputText);
            if(this.sk){
                bodyFormData.append('sk','1');
            }else{
                bodyFormData.append('sk','0');
            }
            
            this.chatTexts.push({text:this.inputText,generated_by_bot:false});
            axios(
                {   headers: {
                        'X-CSRFToken': this.csrftoken,
                    },
                    method:'post',
                    url:'chat-bot',
                    data:bodyFormData,
                }
            )
            .then((response)=>{
                let text = response.data.text;
                this.chatTexts.push({text:text,generated_by_bot:true});
                this.botTyping=false;
                this.inputText = "";
            }).catch(()=>{
                this.chatTexts.push({text:"An error has accored",generated_by_bot:true});
            }).then(function(){

            });
            this.botTyping = false;
        },getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    },mounted(){
        this.csrftoken = this.getCookie('csrftoken');
    }
}
</script>

<style>


@media only screen and (max-width: 786px){
    .c{
        padding-top: 70px;
        min-height: 75vh;
    }   
}
@media only screen and (min-width: 786px){
    .c{
        padding-top: 160px;
        min-height: 75vh;
    }   
}

.chat{
    border-radius: 5px;

}
.send-btn:disabled{
    background: gray;
}
.send-btn{
    padding: 5px;
    border-radius: 10px;
}

.chat-input  input{
    padding: 5px;
}

.background{
    background: transparent;
    background-size: cover;
    overflow: hidden;
}
.chat-title{
    padding: 10px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    background: rgba(0, 0, 0, 0.2);
}
.chat-content{
    background: rgba(0, 0, 0, 0.5);
    padding: 10px;
}


.person-text-card{
    position: relative;
    background: white;
    max-width: 500px;
    color: black;
    border-radius: 10px;
    padding: 10px;
}
.person-text-card:after{
    content: '';
	position: absolute;
	right: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 10px solid transparent;
	border-left-color: white;
	border-right: 0;
	border-top: 0;
	margin-top: -10px;
	margin-right: -10px;
}

.bot-text-card{
    position: relative;
    background: #333333;
    max-width: 500px;
    color: white;
    border-radius: 10px;
    padding: 10px;
}
.bot-text-card:after{
    content: '';
	position: absolute;
	left: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 10px solid transparent;
	border-right-color: #333333;
	border-left: 0;
	border-top: 0;
	margin-top: -10px;
	margin-left: -10px;
}
.chat-input{
    padding: 10px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    background: rgba(0, 0, 0, 0.2);
}
</style>