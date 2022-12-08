import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Personal from '../views/Personal.vue'
import room from '../views/room.vue'
<<<<<<< HEAD
import history from '../views/History.vue'
import settings from '../views/settings.vue'
=======
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93


const isAuth = localStorage.getItem('token') !== null? true: false;


const authGuard = function(to, from, next){
  if(isAuth) {
    next ({
      name:'lk',
    });
  }
  else next()
}
const exitGuard = function(to, from, next){
  if(!isAuth) next ({name: "main"});
  else next()
}

const routes = [
  {
    path: '',
    name: 'main',
    component: Home,
    beforeEnter:authGuard,
  },
  {
    path: '/personal',
    name: 'lk',
    component: Personal,
    beforeEnter:exitGuard,
  },
  {
    path: '/room/:id',
    name: 'room',
    component: room,
<<<<<<< HEAD
    beforeEnter:exitGuard,
  },
  {
    path: '/history',
    name: 'history',
    component: history,
    beforeEnter:exitGuard,
  },
  {
    path: '/settings',
    name: 'settings',
    component: settings,
    beforeEnter:exitGuard,
=======
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
