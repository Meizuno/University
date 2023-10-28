<template>
  <section>
    <div class="form-box">
      <div class="form-value">
        <form action="" @submit.prevent>
          <h2>Login</h2>
          <div class="inputbox">
            <input v-model="username" type="text" >
            <label for="">Username</label>
          </div>
          <div class="inputbox">
            <input v-model="password" type="password" >
            <label for="">Password</label>
          </div>
          <button @click="sendGetUser">Log in</button>
        </form>
      </div>
    </div>

  </section>

</template>

<script>
import axios from 'axios';
import store from "@/store";
import router from "@/router";
export default {
  data(){
    return{
      username: '',
      password: '',
    }
  },
  methods:{
    sendGetUser: function () {
      const postData = {
        username: this.username,
        password: this.password,
      };

      axios.post('http://127.0.0.1:8000/api/auth/token', postData)
          .then(response => {
            console.log('Ответ сервера: token - ', response.data.access);
            localStorage.setItem('token', response.data.access);
            localStorage.setItem('IsAuth', response.data.access);
            store.commit('setToken', response.data.access);
            store.commit('setIsAuth', true);
            router.push('/student');
          })
          .catch(error => {
            console.log("Wrong user or password");
            console.error('Ошибка при отправке запроса');
          });

    },
  },

}
</script>

<style  scoped>
*{
  margin: 0;
  padding: 0;
}
section{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  background: none;
}
.form-box{
  position: relative;
  width: 400px;
  height: 450px;
  background: none;
  border-radius: 20px;
  border: 2px solid royalblue;
  display: flex;
  justify-content: center;
  align-items: center;
}

h2{
  font-size: 2em;
  color: royalblue;
  text-align: center;
}
.inputbox{
  position: relative;
  margin: 30px 0;
  width: 310px;
  border-bottom: 2px solid royalblue;
}
.inputbox label{
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  color: royalblue;
  font-size: 1em;
  pointer-events: none;
  transition: .5s;
}


input:focus ~ label,
input:valid ~ label{
  top: -5px;
}
.inputbox input{
  width: 100%;
  height: 50px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1em;
  padding: 0 35px 0 5px;
  color: black;
}
button{
  width: 100%;
  height: 40px;
  border-radius: 40px;
  background: white;
  border: 2px solid royalblue;
  cursor: pointer;
  outline: none;
  font-size: 1em;
  font-weight: 600;
}
</style>