import { createApp } from 'vue'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import App from './App.vue'
import router from './router'
import store from './store'
import VueMeta from 'vue-meta'

<<<<<<< HEAD
createApp(App).use(Toast).use(store).use(router).mount('#app')
=======
createApp(App).use(store).use(router).mount('#app')
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
