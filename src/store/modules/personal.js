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
            fetch('http://45.9.24.240:8000/api/v1/room/images').then(res=>res.json()).then(data => {
                let images = JSON.parse(data)
                ctx.state.icons = images
            })
        },
        async myRooms(ctx){
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            fetch('http://45.9.24.240:8000/api/v1/room/my',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.listMyRoom = JSON.parse(data)
                })
        },
        async Rooms(ctx){
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            fetch('http://45.9.24.240:8000/api/v1/room/',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.listRooms = JSON.parse(data)
                })
        }
    },
}