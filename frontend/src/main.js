import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import store from "./store";
import 'bootstrap-icons/font/bootstrap-icons.css'

import header from './components/Header'
import footer from './components/Footer'
import router from './router/index'


const app = createApp(App)
app.config.globalProperties.$http = axios;
app
  .component('MyHeader', header)
  .component('MyFooter', footer)
  .use(router)
  .use(store)
  .mount('#app')
