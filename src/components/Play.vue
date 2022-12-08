<template>
    <div>
        <div v-if="!getGuess">
<<<<<<< HEAD
            <h2 class="gametitle">Игра началась!!!</h2>
            <h3 class="newYear">Поздавляем вас с Новым годом!🎄🍾</h3>
            <div class="cardPlay">
                <div class="infoCard">
                    <h3 class="title">Попробуйте угадать кому вы будете дарить подарок</h3>
                    <h4 class="title">У вас осталось {{3 - this.a}} попытки</h4>
                    <div class="listCard">
                        <div class="listPlayerCard" v-on:click="question(player['fullname'], getInfoTO['user'], index)" v-for="(player, index) in getPlayers">
                            <h1 v-if="(getInfoTO['from']!=player['fullname'])" class="card_player" v-bind:class="this.no[index]=='x'?'noA':''">
                                {{player['fullname']}}
                            </h1>
                            <h1 v-else class="card_player" v-bind:class="this.no[index]=='x'?'noA':''">
                                Это вы
                            </h1>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="">
            <div class="cardPlay mt">
                <div class="infoCard">
                    <h3 class="title">А вот и конец!</h3>
                    <h4 class="title" style="margin-bottom: 0;">Пора дарить подарки🎅🎁</h4>
                    <hr>
                    <h2 class="nameTo">Вы дарите подарок: {{getInfoTO['user']}}</h2>
                    <h2 class="priceTo">Максимальная сумма подарка: {{getInfoTO['price']}}₽</h2>
                    <h2 class="wishTo">Человек хочет: </h2>
                    <h2 class="wishTo">{{getInfoTO['wish']}}</h2>
                </div>
            </div>
        </div>
    </div>
   
=======
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
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
</template>
<script>
    import { mapActions, mapGetters } from 'vuex';
    export default{
        methods:{
<<<<<<< HEAD
            ...mapActions(['getResualt', 'okRes', 'getUser']),
            question(name, fullname, index){
=======
            ...mapActions(['getResualt', 'okRes']),
            question(name, fullname){
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
                if(this.a < 3){
                    if (name == fullname){
                        console.log("Ответ правильный")
                        this.okRes(this.$route.params.id)
                    }else{
                        console.log("Попробуй еще, попыток осталось" + 3 - this.a)
<<<<<<< HEAD
                        this.no[index]='x'
=======
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
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
<<<<<<< HEAD
                no:[],
=======
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
            }
        },
        updated(){
            console.log("hello")
        }
    }

<<<<<<< HEAD
</script>
<style scoped>
@import url('../assets/style/play.css')
</style>
=======
</script>
>>>>>>> 4cacb583c08c5615e5c4fe6aa78a63b10d2dfe93
