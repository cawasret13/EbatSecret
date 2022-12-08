export default{
    state: {
        listMyRoom:[],
        listRooms:[],
        icons:null,
    },
    getters: {
        getIcons(state){
            return state.icons
        },
       getMyRooms(state){
        return state.listMyRoom
       },
       getRooms(state){
            return state.listRooms
        }
    },
    mutations: {
        setImage(state, data){
            state.icons = data
        }
    },
    actions: {
        async getImages(ctx){
<<<<<<< HEAD
            fetch('http://192.168.1.68:8000/api/v1/room/images').then(res=>res.json()).then(data => {
=======
            fetch('http://45.9.24.240:8000/api/v1/room/images').then(res=>res.json()).then(data => {
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
                let images = JSON.parse(data)
                ctx.state.icons = images
            })
        },
        async myRooms(ctx){
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
<<<<<<< HEAD
            fetch('http://192.168.1.68:8000/api/v1/room/my',{
=======
            fetch('http://45.9.24.240:8000/api/v1/room/my',{
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.listMyRoom = JSON.parse(data)
                })
        },
        async Rooms(ctx){
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
<<<<<<< HEAD
            fetch('http://192.168.1.68:8000/api/v1/room/',{
=======
            fetch('http://45.9.24.240:8000/api/v1/room/',{
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.listRooms = JSON.parse(data)
                })
        }
    },
}