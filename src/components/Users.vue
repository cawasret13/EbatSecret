<template>
    <div class="uMenu">
        <h3 class="title">Игроки</h3>
        <div class="list_players">
            <div v-for="player in getPlayers" class="player">
                <h4 v-if="getInfo['why']" class="name_player">{{player['fullname']}}</h4>
                <h4 v-else class="name_player">...Имя</h4>
                <button v-if="getInfo['why'] && getInfo['created']" class="lock">Убрать</button>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex';
    export default{
        computed: mapGetters(['getPlayers', 'getInfo']),
<<<<<<< HEAD
        data(){
            return{
                interval:null,
            }
        },
        methods:{
            ...mapActions(['listPlayers']),
            get(){
                this.listPlayers(this.$route.params.id)
            }
        },
        mounted(){
            this.listPlayers(this.$route.params.id)
            this.interval = setInterval(this.get, 5000)
=======
        methods:{
            ...mapActions(['listPlayers'])
        },
        mounted(){
            this.listPlayers(this.$route.params.id)
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
        }
    }
</script>

<style scoped>
    @import url('../assets/style/users.css')
</style>