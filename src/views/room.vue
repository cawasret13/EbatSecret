<template>
     <div>
        <hed />
    </div>
    <div v-if="(getInfo['play'] && getInfo['why'])">
        <Play />
    </div>
    <div v-else-if="!getInfo['play']">
        <listOK v-if="getActiveOk" />
        <div v-if="activeSettings" class="createRoom activeCreate" style="display:display: flex;justify-content: center;align-items: center;">
                <div v-if="getInfo['created']" class="settings">
                    <div v-if="ch_del" class="del">
                        <div class="window">
                            <h2>Вы уверены, что хотите удалить комнату?</h2>
                            <h3>Восстановить комнату будет невозможно</h3>
                            <div class="but_del">
                                <button v-on:click="(ch_del=false)" class="no">Нет</button>
                                <button v-on:click="Delete(this.$route.params.id)" class="yes">Да</button>
                            </div>
                        </div>
                    </div>
                    <h2>Настройки</h2>
                    <div class="sub_settings">
                        <div v-if="ch_icon" class="icons">
                            <button v-on:click="(ch_icon = !ch_icon)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                            <div class="ls_icon">
                                <h4 style="margin-top: 0;">Иконки</h4>
                                <div style="height: 450px;overflow: scroll;border-radius: 13px;">
                                    <img v-for="icon in getIconsSet" :src="icon['image']" alt="" v-bind:class="(icon['id'] == this.getInfoSettings['id_icon']?'selectIcon':'iconRoomsSel')" v-on:click="selectIcon(icon['id'], icon['image'])">
                                </div>
                            </div>
                        </div>
                        <div class="flex_line">
                            <p>Название:</p>
                            <input v-if="ch_name" type="text"  v-model="getInfoSettings['name']">
                            <h4 v-else-if="!ch_name">{{getInfoSettings["name"]}}</h4>
                            <button v-on:click="(ch_name = !ch_name)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                        </div>
                        <div class="flex_desc">
                            <p>Описание:</p>
                            <textarea v-if="ch_desc" type="text"  v-model="getInfoSettings['desc']"></textarea>
                            <h4 v-else-if="!ch_desc">{{getInfoSettings["desc"]}}</h4>
                            <button v-on:click="(ch_desc = !ch_desc)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                        </div>
                        <div class="flex_line">
                            <p>Cтоимость подарка:</p>
                            <input v-if="ch_maxPrice" type="text"  v-model="getInfoSettings['maxPrice']">
                            <h4 v-else-if="!ch_maxPrice">{{getInfoSettings["maxPrice"]}}</h4>
                            <button v-on:click="(ch_maxPrice = !ch_maxPrice)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                        </div>
                        <div class="flex_line">
                            <p>Иконка комнаты:</p>
                            <img :src="getInfoSettings['icon']" alt="">
                            <button v-on:click="(ch_icon = !ch_icon)"  class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                        </div>
                        <div class="flex_line">
                            <p>Максимальное число игроков:</p>
                            <input v-if="ch_maxHum" type="text"  v-model="getInfoSettings['maxHum']">
                            <h4 v-else-if="!ch_maxHum">{{getInfoSettings["maxHum"]}}</h4>
                            <button v-on:click="(ch_maxHum = !ch_maxHum)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button>
                        </div>
                        <div class="flex_line">
                            <p>Приватная комната:</p>
                            <input type="checkbox" v-model="getInfoSettings['private']" v-on:change="changePrivate(getInfoSettings['private'])">
                        </div>
                        <!-- <div class="flex_line">
                            <p>Авто игра:</p>
                            <input type="checkbox" v-model="getInfoSettings['autoPlay']" v-on:change="changePlay(getInfoSettings['autoPlay'])">
                        </div> -->
                    </div>
                    <button v-on:click="Save(this.$route.params.id)" class="save">Сохранить</button>
                    <button v-on:click="(ch_del = true)" class="delete">Удалить комнату</button>
                    <button v-on:click="(this.activeSettings = false)" class="exit"><img width="24" src="../assets/cross-black-circular-button_icon-icons.com_73054.svg" alt=""></button>
                </div>
                <div v-else class="settings">
                    <button v-on:click="exit(this.$route.params.id)" class="btn_exit">Выйти из комнаты</button>
                    <button v-on:click="(this.activeSettings = false)" class="exit"><img width="24" src="../assets/cross-black-circular-button_icon-icons.com_73054.svg" alt=""></button>
                </div>
        </div>
        <div class="ogr_width">
            <div class="flex">
                <div class="info_room">

                    <button v-if="getInfo['why']" v-on:click="(this.activeSettings = true)" class="settings_btn"><img src="../assets/cogwheel_icon-icons.com_70237.svg" alt=""></button>

                    <!-- <h3 class="name" style="margin-bottom: 0;">Информация</h3> -->
                    <h3 class="name">{{getInfo['name']}}</h3>
                    <div class="sIcon">
                        <img :src="getInfo['icon']" alt="" class="icon">
                    </div>
                    <div class="subInfo">
                        <p class="title_set">Описание:</p>
                        <h4 class="description" style="margin-bottom: 15px;">
                            {{getInfo['desc']}}
                        </h4>
                        <div class="flex_line">
                            <p class="title_set">Игроков:</p>
                            <h4 class="description">
                                {{getInfo['nowPlayer']}}/{{getInfo['maxHum']}}
                            </h4>
                        </div>
                        <div class="flex_line">
                            <p class="title_set">Максимальная сумма подарка:</p>
                            <h4 class="description">
                                {{getInfo['maxPrice']}}₽
                            </h4>
                        </div>
                    </div>
                    <div v-if="getInfo['why']">
                        <p class="title_set">Что бы вы хотели получить?<button v-on:click="(J = !J)" class="change"><img src="../assets/edit_square_FILL0_wght400_GRAD0_opsz48.svg" alt=""></button></p>
                        <div v-if="J" class="J">
                            <input class="inpJ" type="text" v-model="wish">
                            <button class="btnJ" v-on:click="wishSet">Это!</button>
                        </div>
                        <div v-else>
                           <p class="title_set">Кажется это:</p>
                           <p class="title_set">{{getInfo['wish']}}</p>
                        </div>
                    </div>
                    <button v-if="getInfo['why'] && getInfo['nowPlayer'] != getInfo['maxHum']" v-on:click="(share = !share)" class="share">Поделиться</button>
                    <button v-on:click="add(this.$route.params.id)" class="btn_v" v-if="!getInfo['private'] && !getInfo['why']">Войти</button>
                    <button v-on:click="add(this.$route.params.id)" class="btn_v" v-if="(getInfo['private'] && !getInfo['why'])">Подать заявку</button>
                    <div v-if="share" class="address">
                        <h4>localhost:8080/room/{{getInfo['id_room']}}</h4>
                    </div>
                    <div v-if="getInfo['nowPlayer'] != getInfo['maxHum']">
                        <button v-on:click="(setActiveIK(true))" class="share" v-if="(getInfo['created'] && getInfo['private'])">Список одобрения {{getInfo['oklen']>0?'( '+getInfo['oklen']+' )':''}}</button>
                    </div>
                    <div v-if="(getInfo['nowPlayer'] == getInfo['maxHum'] && getInfo['created'])">
                        <button v-on:click="start(this.$route.params.id)" class="start_play">Начать игру</button>
                    </div>
                    <div v-if="(getInfo['nowPlayer'] == getInfo['maxHum'] && !getInfo['created'])">
                        <h5>Все игроки на месте, скоро начало 🎅🎇🎉</h5>
                    </div>
                </div>
                <div class="users">
                    <users />
                </div>
            </div>
        </div>
    </div>

</template>
<script>
import { mapGetters, mapActions, mapMutations } from 'vuex';
import users from '../components/Users.vue'
import listOK from '../components/listOK.vue'
import Play from '../components/Play.vue'
import hed from '../components/header.vue'
import { useToast } from "vue-toastification";
    export default{
        data(){
            return{
                info:'',
                activeSettings:false,

                ch_name: false,
                ch_desc: false,
                ch_maxPrice: false,
                ch_maxHum:false,
                ch_icon:false,
                ch_del:false,
                share:false,
                J:false,
                id_icon: '',
                name: '',
                numHum: '',
                maxPrice: '',
                date: '',
                autoRes: '',
                private: '',
                desc: '',
                wish: '',
                interval: null,
            }
        },
        updated(){
        },
        computed:mapGetters(['getInfo', 'getInfoSettings', 'getIconsSet', 'getActiveOk']),
        methods:{
            ...mapActions(['Room', 'images', 'Save', 'Delete', 'add', 'exit', 'start']),
            ...mapMutations(['setIcon', 'setPrivate', 'setPlay', 'setActiveIK']),
            changePrivate(status){
                this.setPrivate(status)
            },
            changePlay(status){
                this.setPlay(status)
            },
            selectIcon(id,img){
                let arr = []
                arr.push(id)
                arr.push(img)
                this.setIcon(arr)
            },
            get(){
                if(this.activeSettings == false) this.Room(this.$route.params.id)
            },
            wishSet(){
                let formData = new FormData();
                formData.append('token', localStorage.getItem('token'));
                formData.append('id_room', this.$route.params.id);
                formData.append('wish', this.wish);
                fetch('http://192.168.1.68:8000/api/v1/room/wish',{
                        method: "POST",
                        body: formData,
                    }).then(res=>res.json()).then(data=>{
                        this.wish =''
                        this.J=false
                        const toast = useToast()
                        toast.success(data['mas'])
                    })
            }
        },
        mounted(){
            this.Room(this.$route.params.id)
            this.images()
            this.interval = setInterval(this.get, 5000)
        },
        components:{
            users,
            listOK,
            Play,
            hed
        }
    }
</script>
<style scoped>
    @import url('../assets/style/room.css')
</style>