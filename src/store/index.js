import { createStore } from 'vuex'
import user from './modules/user'
import personal from './modules/personal'
import room from './modules/room'
import play from './modules/play'
export default createStore({
  modules: {
    user,
    personal,
    room,
    play
  }
})
