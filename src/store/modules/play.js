export default{
    state: {
        info:[],
    },
    getters: {
        getInfoTO(state){
            return state.info
        },
        getGuess(state){
            return state.info['guess']
        }
    },
    mutations: {
      
    },
    actions: {
       async getResualt(ctx, id){
        let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            formData.append('id_room', id);
            fetch('http://45.9.24.240:8000/api/v1/room/resualt',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.info = JSON.parse(data)[0]
                })
       },
       async okRes(ctx, id){
            fetch(`http://45.9.24.240/api/v1/room/resualt?id_room=${id}&token=${localStorage.getItem('token')}`, ).then(res=>res.json()).then(data=>{
                   ctx.state.info = JSON.parse(data)[0]
            })
       },
    },
}