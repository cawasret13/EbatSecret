<template>
    <div style="position: relative;">
        <img src="../assets/decor/Елка.svg" alt="" class="decor" style="position: absolute;bottom: 0;z-index: -1;">
        <img src="../assets/decor/Снеговик.svg" alt="" class="decor" style="position: absolute;bottom: 0;right: 0;z-index: -1;">
        <div class="header">
            <div class="ogr_header"> 
                <a href="" style="color:black;text-decoration: none">
                    <div class="logo">
                            <img src="../assets/logo.png" alt="Лого">
                            <h1 class="logoH">Тайный санта</h1>
                    </div>
                </a>
            </div>
        </div>
        <div class="content">
            <div class="auth_back">
                <transition name="mode-fade" mode="out-in" class="mobile_form">
                <div v-if="this.active" class="f_w">
                    <div class="auth_form form">
                        <h2 class="title">Авторизация</h2>
                        <input v-model="this.aLogin" type="text" name="login" placeholder="Логин">
                        <div style="display: flex;    flex-direction: column;">
                            <input v-model="this.aPassword"  type="password" name="password" placeholder="Пароль" style="margin: 0;" v-on:keyup.enter="Auth()">
                            <p style="margin: 0;margin-bottom: 15px;cursor: pointer;">Восстановление пароля</p>
                        </div>
                        <button class="btn_form" v-on:click="Auth()">Войти</button>
                    </div>
                    <div class="info">
                        <h1 class="titlePlay">Что такое «Тайный Санта?»</h1><br>
                        <h2 class="desc_game">«Тайный Сантa» — популярная церемония анонимного обмена подарками. Это новогодняя игра с простыми правилами: каждый участник является Тайным Сантой для одного из остальных участников и втайне готовит для него подарок. В результате всем достаётся и радость подготовки сюрприза, и подарок.
                            Данный сайт — сервис, который помогает огранизовать эту игру онлайн.</h2>
                    </div>
                    <div style="width: 100%;height: 50%;padding-bottom: 5%;display: flex;justify-content: center;">
                        <button class="btn_reg_home" v-on:click="this.active = false">Регистрация</button>
                        <button class="btn_reg_home_mobile" v-on:click="this.active = false">Регистрация</button>
                    </div>
                </div>
                <div v-else>
                    <div class="form auth_form">
                        <h2 class="title">Регистрация</h2>
                        <input v-model="rName" type="text" name="login" placeholder="Имя">
                        <input v-model="rSurname" type="text" name="login" placeholder="Фамилия">
                        <input v-model="rEmail" type="email" name="login" placeholder="Почта">
                        <input v-model="rLogin" type="text" name="login" placeholder="Логин">
                        <input v-model="rPassword" type="password" name="password" placeholder="Пароль">
                        <input v-model="rClonePassword" type="password" name="password" placeholder="Пароль еще раз" v-on:keyup.enter="Register()">
                        <button class="btn_form" v-on:click="Register()">Зарегистрироваться</button>
                    </div>
                    <div style="width: 100%;height: 50%;padding-bottom: 2%;padding-top: 5%;display: flex;justify-content: center;">
                        <button class="btn_reg_home" v-on:click="(this.active = true)">Вход</button>
                        <button class="btn_reg_home_mobile" v-on:click="(this.active = true)">Вход</button>
                    </div>
                </div>
                </transition>
            </div>
            <div style="width: 80%;margin: auto;">
                <h3 style="margin: 0;text-align: center;font-size: 18px;">Немного о игре</h3>
                <div class="ls_instructions">
                    <div class="bloc_w">
                        <div class="bar_icon">
                            <h3 class="namber">1</h3>
                            <img style="float: right;" src="../assets/icon_rooms/icon1.png" alt="">
                        </div>
                        <div class="description">
                            <h4 class="text_desc">Создайте комнату для жеребьевки, указав её название, ограничение на стоимость подарков и другие опции по желанию.</h4>
                        </div>
                    </div>
                    <div class="bloc_w">
                        <div class="bar_icon">
                            <h3 class="namber  two">2</h3>
                            <img class="img_two" src="../assets/icon_rooms/icon3.png" alt="">
                        </div>
                        <div class="description">
                            <h4 class="text_desc">Участники могут добавить в карточку свои пожелания по подарку. Как только все игроки зарегистрировались, проведите тайную жеребьевку.</h4>
                        </div>
                    </div>
                    <div class="bloc_w">
                        <div class="bar_icon">
                            <h3 class="namber">3</h3>
                            <img style="float: right;" src="../assets/icon_rooms/icon6.png" alt="">
                        </div>
                        <div class="description">
                            <h4 class="text_desc">Сразу после проведения жеребьевки все узнают, кому нужно подготовить подарок.</h4>
                        </div>
                    </div>
                    <div class="bloc_w">
                        <div class="bar_icon">
                            <h3 class="namber">*</h3>
                            <img style="float: right;" src="../assets/icon_rooms/icon8.png" alt="">
                        </div>
                        <div class="description">
                            <h4 class="text_desc">Комнаты после игры лежат в архиве, чтоб в него попасть в шапке нужно нажать на свое имя.</h4>
                            <h4 class="text_desc">Приятной игры, и хорошего настроения!!!</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
import { useToast } from "vue-toastification";
    export default{
        data(){
            return{
                active: true,
                aLogin:'',
                aPassword:'',

                rName:'',
                rSurname:'',
                rEmail:'',
                rLogin:'',
                rPassword:'',
                rClonePassword:''

            }
        },
            computed: mapGetters(["getToken"])
        ,
        methods:{
            ...mapMutations(["addToken"]),
           async Auth(){
            const toast = useToast()
            let formData = new FormData();
                formData.append('login', this.aLogin);
                formData.append('password', this.aPassword);
                fetch('http://192.168.1.68:8000/api/v1/user/authorization',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                    if(data['err'] == null){
                        this.addToken(data);
                        toast.success("Добро пожаловать!")
                        if(localStorage.getItem('token')!=null) location.replace('/personal')
                    }else{
                        toast.error(data['err'])
                    }
                })
           },
           async Register(){
                const toast = useToast()
                if(this.rClonePassword == this.rPassword){
                    let formData = new FormData();
                    formData.append('name', this.rName);
                    formData.append('surname', this.rSurname);
                    formData.append('email', this.rEmail);
                    formData.append('login', this.rLogin);
                    formData.append('password', this.rPassword);
                    fetch('http://192.168.1.68:8000/api/v1/user/create',{
                        method: "POST",
                        body: formData,
                    }).then(res=>res.json()).then(data=>{
                        if(data['err'] == null){
                            this.addToken(data);
                            if(localStorage.getItem('token')!=null) location.replace('/personal')
                        }else{
                            toast.error(data['err'])
                        }
                    })
                }else{
                    toast.error("Пароли не совпадают")
                }
           }    
        }
    }
</script>

<style>
    @import url('../assets/style/style.css')
</style>