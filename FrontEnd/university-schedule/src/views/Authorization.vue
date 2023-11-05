<template>
  <section>

    <div class="form-box">
      <div class="form-value">
        <form action="" @submit.prevent>
          <h2 class="login_name">Login</h2>
          <div class="inputbox">
            <input v-model="username" type="text" >
            <label for="">Username</label>
          </div>
          <div class="inputbox">
            <input v-model="password" type="password" >
            <label for="">Password</label>
          </div>
          <div class="bttns">
            <button class="login_bttn" @click="sendGetUser">Log in</button>
            <button class="home_bttn"> Home</button>
          </div>

        </form>
      </div>
    </div>

  </section>
</template>

<script>
import axios from "axios";

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
            //store.commit('setToken', response.data.access);
            //store.commit('setIsAuth', true);
            //router.push('/student');
          })
          .catch(error => {
            console.log("Wrong user or password");
            console.error('Ошибка при отправке запроса');
          });
      this.username = '';
      this.password = '';
    },
  },
}
</script>

<style scoped>
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
  background: white;
  border-radius: 20px;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
}

h2{
  font-size: 2em;
  color: black;
  text-align: center;
}
.inputbox{
  position: relative;
  margin-top: 40px;
  margin-bottom: 20px;
  width: 310px;
  border-radius: 10px;
  background: rgba(0, 0, 0, 0.1);
}
.inputbox label {
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-40%);
  color: rgba(0, 0, 0, 0.6);
  font-size: 1em;
  font-weight: bold;
  pointer-events: none;
  transition: .5s;
  height: 40px; /* Выравнивание высоты label с высотой input */

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
  font-size: 20px;
  padding: 0 35px 0 5px;
  color: black;
}
.bttns{
  display: flex;
  justify-content: center;
}
button{
  width: 30%;
  height: 40px;
  border-radius: 10px;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  font-size: 1em;
  font-weight: 600;
}
.home_bttn{
  background-color: #45BFFF;
  margin-left: 10px;
}
.login_bttn{
  background-color: #84D296;
  margin-right: 10px;
}

</style>