<template>
    <div>
        <div v-if="!getGuess">
            <h1 style="text-align: center;">Игра началась</h1>
            <h2 style="text-align: center;">Угадайте кому дарите подарок</h2>
            <h2 style="text-align: center;">Попыток осталось {{(3- this.a)}}</h2>
            {{getGuess}}
            <div>
                <h1 style="text-align: center;cursor: pointer;" v-on:click="question(player['fullname'], getInfoTO['user'])" v-for="player in getPlayers">{{player['fullname']}}</h1>
            </div>
        </div>
        <div v-else>
            <h1>Результаты</h1>
            <h2>Вы дарите подарок {{getInfoTO['user']}}</h2>
        </div>
    </div>
</template>
<script>
    import { mapActions, mapGetters } from 'vuex';
    export default{
        methods:{
            ...mapActions(['getResualt', 'okRes']),
            question(name, fullname){
                if(this.a < 3){
                    if (name == fullname){
                        console.log("Ответ правильный")
                        this.okRes(this.$route.params.id)
                    }else{
                        console.log("Попробуй еще, попыток осталось" + 3 - this.a)
                        this.a++
                        if(this.a == 3){
                            this.okRes(this.$route.params.id)
                        }
                    }
                }else{
                    console.log('Это не важно, ты все равно попал в мое сердце')
                    this.okRes(this.$route.params.id)
                }
            }

        },
        computed: mapGetters(['getInfoTO', 'getPlayers', 'getGuess']),
        mounted(){
            this.getResualt(this.$route.params.id)
        },
        data(){
            return{
                a:0,
            }
        },
        updated(){
            console.log("hello")
        }
    }

</script>