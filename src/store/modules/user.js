export default{
    state: {
        token: localStorage.getItem("token") || null,
    },
    getters: {
        getToken(state){
            return state.token
        }
    },
    mutations: {
        addToken(state, data){
            state.token = data
            localStorage.setItem('token', data)
        }
    },
    actions: {
    },
}