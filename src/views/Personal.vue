<template>
    <div class="createRoom"  v-bind:class="[activeCreate ? 'activeCreate' : 'deactiveCreate']">
        <div class="formPop">
            <h4 style="margin-top: 0;">Иконки</h4>
            <div class="iconCreate">
                <img v-for="icon in getIcons" :src="icon['image']" alt="" v-bind:class="(icon['id'] == this.id_icon?'selectIcon':'iconRoomsSel')" v-on:click="selectIcon(icon['id'])">
            </div>
        </div>
        <div class="formPop">
            <h3 style="margin-top: 0;">Создание комнаты</h3>
            <input v-model="name" type="text" placeholder="Название">
            <input v-model="numHum" type="text" placeholder="Кол-во человек">
            <input v-model="maxPrice" type="text" placeholder="Макс. стоимость подарка">
            <p v-if="autoRes == false" style="margin: 0;">Дата результатов</p>
            <input v-if="autoRes == false" v-model="date" type="date">
            <!-- <div style="display: inline-flex;align-items: center;height: 20px;margin-bottom: 5px;">
                <input v-model="autoRes" type="checkbox" style="padding: 0;box-shadow: none;width: 5%;">
                <p style="margin: 0;">Без авто результата</p>
            </div> -->
            <div style="display: inline-flex;align-items: center;height: 20px;">
                <input v-model="private" type="checkbox" style="padding: 0;box-shadow: none;width: 5%;">
                <p style="margin: 0;">Приватная комната</p>
            </div>
            <div class="ctr_formPop">
                <button v-on:click="closeCreate()" style="width: 28%;margin: 1%;color: white;height: 40px;border: 0;border-radius: 7px;cursor: pointer;font-family: 'Didact Gothic', sans-serif ;background: linear-gradient(to bottom right, #ff0000a1, #ff2323);">Отмена</button>
                <button v-on:click="addRoom()" style="width: 68%;margin: 1%;color: white;height: 40px;border: 0;border-radius: 7px;cursor: pointer;font-family: 'Didact Gothic', sans-serif ;background: linear-gradient(to bottom right, #F2B441, #ffa887);">Создать</button>
            </div>
        </div>
    </div>
    <div>
        <hed />
    </div>
  <div class="ogr_rooms">
        <div class="myRooms">
            <div v-if="(getMyRooms.length != 0)">
                <div class="controll_panel">
                    <h2>Ваши комнаты</h2>
                    <button class="btn_create" v-on:click="openCreate">Создать комнату</button>
                </div>
                <div class="listRooms">
                        <swiper  class="swiper obj_ref nav"
                                :modules="modules"
                                :space-between="30"
                                :slides-per-view="6"
                                :slides-per-group="3"
                                :loop="false"
                                :loop-fill-group-with-blank="false"
                                :navigation="true"
                                :pagination="{ clickable: true }">
                            <swiper-slide v-for="room in getMyRooms">
                            <div class="room" style="padding: 3%;">
                                <div class="icon_room">
                                    <img :src="room['icon']" alt="">
                                </div>
                                <div class="information_room">
                                    <div class="cell_info">
                                        <div style="width: 100%;height: 20%;;display: inline-flex;align-items: center;justify-content: space-between;">
                                            <h2 class="name_room">{{
                                            (room['name'].length > 16)?room['name'].slice(0, 16)+'...':room['name']
                                            }}</h2>
                                            <h2 class="name_room" style="color:#ddd;">{{room['nowPlayer']}}/{{room['maxHum']}}</h2>
                                        </div>
                                        <div v-if="room['private'] == true" style="width: 100%;height: 30%;">
                                            <div  style="width: 100%;height: 100%;display: inline-flex;">
                                                <h3 style="margin: 0;font-size: 14px;color: #a7a7a7;">Закрыто</h3>
                                                <img style="height: 100%;margin-left: 5px;" src="../assets/lock_close_padlock_icon_145962.svg" alt="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="cell_btn">
                                        <a :href="('/room/'+room['id_room'])" style="color: white;"><button class="btn_create" style="width: 100%;height: 100%;">Открыть</button></a>
                                    </div>
                                </div>
                            </div>
                            </swiper-slide>
                        </swiper>

                    <div class="room cell_siper" style="padding: 3%;" v-for="room in getMyRooms">
                        <div class="icon_room">
                            <img :src="room['icon']" alt="">
                        </div>
                        <div class="information_room">
                            <div class="cell_info">
                                <div style="width: 100%;height: 20%;;display: inline-flex;align-items: center;justify-content: space-between;">
                                    <h2 class="name_room">{{
                                            (room['name'].length > 16)?room['name'].slice(0, 16)+'...':room['name']
                                            }}</h2>
                                    <h2 class="name_room" style="color:#ddd;">{{room['nowPlayer']}}/{{room['maxHum']}}</h2>
                                </div>
                                <div v-if="room['private'] == true" style="width: 100%;height: 30%;">
                                    <div  style="width: 100%;height: 100%;display: inline-flex;">
                                        <h3 style="margin: 0;font-size: 14px;color: #a7a7a7;">Закрыто</h3>
                                        <img style="height: 100%;margin-left: 5px;" src="../assets/lock_close_padlock_icon_145962.svg" alt="">
                                    </div>
                                </div>
                            </div>
                            <div class="cell_btn">
                                <a :href="('/room/'+room['id_room'])" style="color: white;"><button class="btn_create" style="width: 100%;height: 100%;">Открыть</button></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <div class="none_rooms">
                    <h2>У вас нет комнат</h2>
                    <button v-on:click="openCreate" class="btn_create">Создать комнату</button>
                </div>
            </div>
            <div v-if="(getPlay.length != 0)">
                <h2>Ваши игры</h2>
                <div class="listRooms">
                        <div class="room" v-for="room in getPlay">
                            <div class="icon_room">
                                <img :src="room['icon']" alt="">
                            </div>
                            <div class="information_room">
                                <div class="cell_info">
                                    <div style="width: 100%;height: 20%;;display: inline-flex;align-items: center;justify-content: space-between;">
                                        <h2 class="name_room">{{
                                            (room['name'].length > 16)?room['name'].slice(0, 16)+'...':room['name']
                                            }}</h2>
                                        <h2 class="name_room" style="color:#ddd;">{{room['nowPlayer']}}/{{room['maxHum']}}</h2>
                                    </div>
                                    <div v-if="room['private'] == true" style="width: 100%;height: 30%;">
                                        <div  style="width: 100%;height: 100%;display: inline-flex;">
                                            <h3 style="margin: 0;font-size: 14px;color: #a7a7a7;">Закрыто</h3>
                                            <img style="height: 100%;margin-left: 5px;" src="../assets/lock_close_padlock_icon_145962.svg" alt="">
                                        </div>
                                    </div>
                                </div>
                                <div class="cell_btn">
                                    <a :href="('/room/'+room['id_room'])" style="color: white;"><button class="btn_create" style="width: 100%;height: 100%;">Открыть</button></a>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
            <div v-if="(getRooms.length != 0)">
                <h2>Другие комнаты</h2>
                <div class="listRoomsNoMy">
                        <div class="room noMyRoom" v-for="room in getRooms">
                            <div class="icon_room">
                                <img :src="room['icon']" alt="">
                            </div>
                            <div class="information_room">
                                <div class="cell_info">
                                    <div style="width: 100%;height: 20%;;display: inline-flex;align-items: center;justify-content: space-between;">
                                        <h2 class="name_room">{{
                                            (room['name'].length > 16)?room['name'].slice(0, 16)+'...':room['name']
                                            }}</h2>
                                        <h2 class="name_room" style="color:#ddd;">{{room['nowPlayer']}}/{{room['maxHum']}}</h2>
                                    </div>
                                    <div v-if="room['private'] == true" style="width: 100%;height: 30%;">
                                        <div  style="width: 100%;height: 100%;display: inline-flex;">
                                            <h3 style="margin: 0;font-size: 14px;color: #a7a7a7;">Закрыто</h3>
                                            <img style="height: 100%;margin-left: 5px;" src="../assets/lock_close_padlock_icon_145962.svg" alt="">
                                        </div>
                                    </div>
                                </div>
                                <div class="cell_btn">
                                    <a :href="('/room/'+room['id_room'])" style="color: white;"><button class="btn_create" style="width: 100%;height: 100%;">Открыть</button></a>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
        </div>



  </div>
</template>
<script>
    import SwiperClass, { Pagination , Navigation } from 'swiper'
    import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
    import 'swiper/css'
    import 'swiper/css/pagination'
    import 'swiper/css/navigation'
    import { mapGetters, mapMutations, mapActions } from 'vuex';
    import hed from '../components/header.vue'


    import { useToast } from "vue-toastification";
import { timeouts } from 'retry'

    export default {
        data(){
            return{
                icon:[],
                activeCreate: false,
                ws: null,

                id_icon: 1,
                name: '',
                numHum:'',
                maxPrice:'',
                date:'',
                autoRes:true,
                private:false,
                interval:null,
            }
        },
        name: "lk",
        computed: mapGetters(['getMyRooms', 'getIcons', 'getToken', 'getRooms', 'getPlay']),
        methods:{
            ...mapMutations(['setImage']),
            ...mapActions(['getImages', 'myRooms', 'Rooms', 'Play']),
            openCreate(){
                this.activeCreate = true
            },
            closeCreate(){
                this.activeCreate = false
                this.closeForm()
            },
            selectIcon(id){
                this.id_icon = id
            },
            closeForm(){
                this.activeCreate = false
                this.id_icon = 1
                this.name = null
                this.numHum = null
                this.maxPrice = null
                this.date = null
                this.autoRes = true
                this.private = false
            }
            ,
            async addRoom(){
                console.log(this.private)
                let formData = new FormData();
                formData.append('token', localStorage.getItem('token'));
                formData.append('id_icon', this.id_icon);
                formData.append('name', this.name);
                formData.append('max', this.numHum);
                formData.append('max_price', this.maxPrice);
                if (this.autoRes == false) formData.append('date', this.date);
                if (this.private == true) formData.append('private', 1);
                else formData.append('private', 0);
                if (this.autoRes == true) formData.append('autoRes', this.autoRes);
                else formData.append('autoRes', this.autoRes);
                fetch('http://192.168.1.68:8000/api/v1/room/create',{
                    method: "POST",
                    body: formData,
                }).then(res=>res.json()).then(data=>{
                    const toast = useToast()
                    console.log(data['err'])
                   if(data['err'] == null){
                        toast.success(data['mas'])
                        this.myRooms()
                        this.closeForm()
                   }else{
                        toast.error(data['err'], {
                            timeout:1500,
                        })
                   }
                })
            },
            get(){
                this.Rooms()
                this.myRooms()
                this.Rooms()
                this.Play()
            }
        },
        mounted(){
            this.getImages()
            this.myRooms()
            this.Rooms()
            this.Play()

            this.interval = setInterval(this.get, 5000)
        }
        ,components: {
            Swiper,
            SwiperSlide,
            hed,
        },
        setup() {
            return {
                modules: [Pagination, Navigation ],
            }
        }
    }
</script>
<style scoped>
    @import url('../assets/style/stylePersonal.css')
</style>