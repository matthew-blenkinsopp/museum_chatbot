import Vue from 'vue'
import vuetify from './vuetify'

// let routes = require("./routes");
//import App from './App.vue'
Vue.component('navbar', require('./components/Navbar.vue').default);
Vue.component('chat-bot', require('./components/ChatBot.vue').default);
Vue.component('app-footer', require('./components/AppFooter.vue').default);

window.vuetify = vuetify

const app = new Vue({
  vuetify,
  el: '#app',
});


export default app;