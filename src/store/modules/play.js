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
<<<<<<< HEAD
            fetch('http://192.168.1.68:8000/api/v1/room/resualt',{
=======
            fetch('http://45.9.24.240:8000/api/v1/room/resualt',{
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.info = JSON.parse(data)[0]
                })
       },
       async okRes(ctx, id){
<<<<<<< HEAD
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            formData.append('id_room', id);
            fetch('http://192.168.1.68:8000/api/v1/room/res',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                ctx.state.info = JSON.parse(data)[0]
                })
=======
            fetch(`http://45.9.24.240/api/v1/room/resualt?id_room=${id}&token=${localStorage.getItem('token')}`, ).then(res=>res.json()).then(data=>{
                   ctx.state.info = JSON.parse(data)[0]
            })
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
       },
    },
}