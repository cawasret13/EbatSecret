<template>
    <div>
        <hed />
    </div>
    <div class="back">
        <div class="window">
            <h1>Настройки</h1>
            <div class="formSet">
                <input type="text" placeholder="Имя" v-model="name">
                <input type="text" placeholder="Фамилия" v-model="surname">
                <input type="email" placeholder="Почта" v-model="email">
                <button class="saveSet" v-on:click="setData">Сохранить</button>
                
                <button v-on:click="logout" class="exitSet">Выход</button>
            </div>
        </div>
    </div>
</template>
<script>
       import hed from '../components/header.vue'
       import { useToast } from "vue-toastification";
       export default{
        components:{
            hed
        },
        methods:{
            logout(){
                localStorage.clear()
                location.replace('/')
            },
            getData(){
                fetch('http://192.168.1.68:8000/api/v1/user/settings?token='+localStorage.getItem('token')).then(res=>res.json()).then(data => {
                    data = JSON.parse(data)
                    this.name=data['name']
                    this.surname=data['surname']
                    this.email=data['email']
            })
            },
            setData(){
                let formData = new FormData();
            formData.append('token', localStorage.getItem('token'));
            formData.append('name', this.name);
            formData.append('surname', this.surname);
            formData.append('email', this.email);
            fetch('http://192.168.1.68:8000/api/v1/room/my',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                    const toast = useToast()
                    if(data['err']==null){
                        toast.success(data['mas'])
                        this.getData
                    }else{
                        toast.error(data['err'])
                    }
                })
            }
        },
        data(){
            return{
                name:'',
                surname:'',
                email:','
            }
        },
        mounted(){
            this.getData()
        }
       }
</script>
<style>
    @import url('../assets/style/settings.css')
</style>