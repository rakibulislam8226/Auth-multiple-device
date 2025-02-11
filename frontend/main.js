import { createApp } from 'vue'
import './style.css'
import App from './App.vue';
import router from './router';
import izitoast from './plugins/izitoast';

createApp(App).use(router).use(izitoast).mount('#app')
