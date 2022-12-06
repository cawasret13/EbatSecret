<template>
    <div class="createRoom activeCreate">
        <div class="form_mobile form" style="position: relative;overflow: scroll;height: 90%;min-height: 200px;">
            <button v-on:click="(setActiveIK(false))" class="exit"><img width="24" src="../assets/cross-black-circular-button_icon-icons.com_73054.svg" alt=""></button>
            <h1 style="margin-top: 0;">Список одобрении</h1>
            <div v-if="(getlistOK.length != 0)" class="listPlayerAdd">
                <div v-for="(player, index) in getlistOK" class="cell_player">
                    <h1 class="namePlayer">{{player['fullname']}}</h1>
                    <div class="btn_add">
                        <button v-on:click="ok(false, index)" class="no">Отмена</button>
                        <button v-on:click="ok(true, index)" class="yes">Добавить</button>
                    </div>
                </div>
            </div>
            <div v-else>
                <h3 style="font-size: 16px;text-align: center;color: #ddd;">Список пустой, подождите немного</h3>
            </div>
        </div>
    </div>
</template>
<script>
    import { mapGetters, mapMutations, mapActions } from 'vuex';
    export default{
        computed:mapGetters(['getActiveOk', 'getlistOK']),
        methods:{
            ...mapMutations(['setActiveIK']),
            ...mapActions(['listOK', 'yesOK']),
            ok(status, index){
                let arr = [
                    this.$route.params.id,
                    status, 
                    index
                ]
                this.yesOK(arr)
            }
        },
        mounted(){
            this.listOK(this.$route.params.id)
        }
    }
</script>