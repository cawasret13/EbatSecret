<template>
    <hed />
    <div>
        <h1 style="text-align: center;">История</h1>
        <div class="listRooms flexHis">
                <div class="room mt" v-for="room in this.list">
                    <div class="icon_room">
                        <img :src="room['icon']" alt="">
                    </div>
                    <div class="information_room">
                        <div class="cell_info">
                            <div style="width: 100%;height: 20%;;display: inline-flex;align-items: center;justify-content: space-between;">
                                <h2 class="name_room">{{
                                    (room['name'].length > 16)?room['name'].slice(0, 16)+'...':room['name']
                                    }}</h2>
                                <h2 class="name_room" style="color:#ddd;">{{room['nowPlayer']}}{{room['maxHum']}}</h2>
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
</template>
<script>
    import hed from '../components/header.vue'
    export default{
        data(){
            return{
                list:[]
            }
        },
        methods:{
            get(){
                let formData = new FormData();
                formData.append('token', localStorage.getItem('token'));
                fetch('http://192.168.1.68:8000/api/v1/history',{
                        method: "POST",
                        body: formData,
                    }).then(res=>res.json()).then(data=>{
                        this.list = JSON.parse(data)
                    })
                }
        },
        mounted(){
            this.get()
        },
        components:{
            hed
        }
    }
</script>
<style>
    .flexHis{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }
    .mt{
        margin-top: 10px;
    }
</style>