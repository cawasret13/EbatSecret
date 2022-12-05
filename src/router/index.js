import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Personal from '../views/Personal.vue'
import room from '../views/room.vue'


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
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
