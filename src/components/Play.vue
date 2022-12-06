<template>
    <div>
        <div v-if="!getGuess">
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
   
</template>
<script>
    import { mapActions, mapGetters } from 'vuex';
    export default{
        methods:{
            ...mapActions(['getResualt', 'okRes', 'getUser']),
            question(name, fullname, index){
                if(this.a < 3){
                    if (name == fullname){
                        console.log("Ответ правильный")
                        this.okRes(this.$route.params.id)
                    }else{
                        console.log("Попробуй еще, попыток осталось" + 3 - this.a)
                        this.no[index]='x'
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
                no:[],
            }
        },
        updated(){
            console.log("hello")
        }
    }

</script>
<style scoped>
@import url('../assets/style/play.css')
</style>