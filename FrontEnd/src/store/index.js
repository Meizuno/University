import {createStore} from "vuex";

export default createStore({

    state: {
        token: '',
        isAuth: false,
    },

    // computed свойства
    // getters: {
    //
    // },


    //store.commit('func name', param)
    mutations: {
        setToken(state,token){
            state.token = token;
        },
        setIsAuth(state, bool){
            state.isAuth = bool;
        },
        incLikes(state){
            state.likes += 1;
        }
    },

    // функции которые юзают мутации
    // action: {
    //
    // },

})