<template>
     <div class="header">
            <div class="ogr_header"> 
                <div class="headerFlex">
                    <div class="logo">
                        <a href="/" class="a_header"  v-if="(this.active == false)">
                            <img src="../assets/logo.png" alt="Лого" class="icon">
                            <h1>Тайный санта</h1>
                        </a>
                    </div>
                    <div v-if="(this.active == false)" class="infoUser">
                        <div v-on:click="(this.active = true)" class="showUser">{{this.fullname}}</div>
                    </div>
                    <div v-if="(this.active == true)" class="ls_ctrl">
                        <div class="btn_ctrl"><a href="/history">История</a></div>
                        <div class="btn_ctrl"><a href="/settings">Настройки</a></div>
                        <div v-on:click="(this.active = false)" class="btn_ctrl">Закрыть</div>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
    import { mapGetters } from 'vuex';
    export default{
        computed:mapGetters(['getInfo']),
        data(){
            return{
                fullname:'name',
                active:false,
            }
        },
        methods:{
            getuser(){
                let formData = new FormData();
                formData.append('token', localStorage.getItem('token'));
                fetch('http://192.168.1.68:8000/api/v1/user/info',{
                        method: "POST",
                        body: formData,
                    }).then(res=>res.json()).then(data=>{
                        this.fullname = JSON.parse(data)['fullname']
                    })
            },
          
        },
        mounted(){
           this.getuser()
        },
    }
</script>
<style scoped>
    .infoUser{
        position: relative;
    }
    .headerFlex{
        width: 100%;
        display: inline-flex;
        align-items: center;
        justify-content: space-between;
        height: 100%;
    }
    .icon{
        height: 90%;
    }
    .a_header{
        width: 100%;
        height: 100%;
        display: inline-flex;
        align-items: center;
        text-decoration: none;
        color: black;
    }
    .showUser{
        cursor: pointer;
    }
    .ls_ctrl{
        display: inline-flex;
    }
    .btn_ctrl{
        margin-left: 25px;
        cursor: pointer;
    }
    .btn_ctrl a{
        color: black;
        text-decoration: none;
    }
    @media only screen and (max-width: 600px) {
        .headerFlex{
            width: 98%;
        }
        .a_header h1{
            font-size: 14px;
            margin-left: 0;
        }
    }
</style>