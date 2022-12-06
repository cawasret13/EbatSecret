import { useToast } from "vue-toastification";

export default{
    state: {
        info: [],
        info_settings: [],
        icons: [],
        list_player: [],
        listPlay:[],

        activeOk: false,
        play:[]
    },
    getters: {
      getInfo(state){
        return state.info
      },
      getInfoSettings(state){
        return state.info_settings
      },
      getIconsSet(state){
        return state.icons
      },
      getPlayers(state){
        return state.list_player
      },
      getPlay(state){
        return state.listPlay
      },
      getActiveOk(state){
        return state.activeOk
      },
      getlistOK(state){
        return state.play
      }
    },
    mutations: {
      setIcon(state, arr){
          state.info_settings['id_icon'] = arr[0]
          state.info_settings['icon'] = arr[1]
      },
      setPrivate(state, status){
        state.info_settings['private'] = status
      },
      setPlay(state, status){
        state.info_settings['autoPlay'] = status
      },
      setInfo(state, data){
        state.info = data
        state.info_settings = data
      },
      setActiveIK(state, status){
        state.activeOk =  status
      }
    },
    actions: {
        async Room(ctx, id){
            let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            formData.append('id', id);
            fetch('http://192.168.1.68:8000/api/v1/room/show',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                   ctx.state.info = JSON.parse(data)[0]
                   ctx.state.info_settings = JSON.parse(data)[0]
                })
        },
        async images(ctx){
              fetch('http://192.168.1.68:8000/api/v1/room/images',{
            }).then(res=>res.json()).then(data=>{
              ctx.state.icons = JSON.parse(data)
            })
        },
        async Save(ctx, id){
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id', id);
          formData.append('data', JSON.stringify(ctx.state.info_settings));
          fetch('http://192.168.1.68:8000/api/v1/room/settings',{
                  method: "POST",
                  body: formData,
              }).then(res=>res.json()).then(data=>{
                location.replace('/room/'+id)
              })
        },
        async Delete(ctx, id){
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id', id);
          fetch('http://192.168.1.68:8000/api/v1/room/delete',{
                  method: "POST",
                  body: formData,
              }).then(res=>res.json()).then(data=>{
                if(data == 'Good') location.replace('/personal')
              })
        },
        async listPlayers(ctx, id){
          let formData = new FormData();
          formData.append('id', id);
          fetch('http://192.168.1.68:8000/api/v1/room/players',{
                  method: "POST",
                  body: formData,
              }).then(res=>res.json()).then(data=>{
                  ctx.state.list_player = JSON.parse(data)
              })
        },
        async Play(ctx){
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          fetch('http://192.168.1.68:8000/api/v1/room/play',{
                  method: "POST",
                  body: formData,
              }).then(res=>res.json()).then(data=>{
                  ctx.state.listPlay = JSON.parse(data)
              })
        },
        async add(ctx, id){
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id_room', id);
          fetch('http://192.168.1.68:8000/api/v1/room/add',{
                  method: "POST",
                  body: formData,
              }).then(res=>res.json()).then(data=>{
                  const toast = useToast()
                  if(data['err'] == null){
                    toast.success(data['mas'])
                  }else{
                    toast.error(data['err'])
                  }
              })
        },
        async listOK(ctx, id_room){
            fetch('http://192.168.1.68:8000/api/v1/room/listOK?id_room='+ id_room).then(res=>res.json()).then(data=>{
              let a = JSON.parse(data)
              ctx.state.play = a
            }
            )
        },
        yesOK(ctx, data){
          console.log(data)
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id_room', data[0]);
          formData.append('status', data[1]);
          formData.append('id', data[2]);
          let st = 0
          fetch('http://192.168.1.68:8000/api/v1/room/listOK',{
                  method: "POST",
                  body: formData,
              }).then(res=>{
                st = res.status
                return res.json()
              }).then(response=>{
                  alert(response)
                  if(st == 200) location.replace('/room/'+ data[0])
              })
        },
        exit(ctx, id){
          console.log(id, localStorage.getItem('token'))
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id_room', id);
          let st = 0
          fetch('http://192.168.1.68:8000/api/v1/room/exit',{
                  method: "POST",
                  body: formData,
              }).then(res=>{
                st = res.status
                return res.json()
              }).then(response=>{
                  alert(response)
                  if(st == 200) location.replace('/personal')
              })
        },
        start(ctx, id){
          let formData = new FormData();
          formData.append('token', localStorage.getItem('token'));
          formData.append('id_room', id);
          let st = 0
          fetch('http://192.168.1.68:8000/api/v1/room/start',{
                  method: "POST",
                  body: formData,
              }).then(res=>{
                return res.json()
              }).then(response=>{
                  alert(response)
              })
        }
    },
}

                
                
                
                
                
                
                