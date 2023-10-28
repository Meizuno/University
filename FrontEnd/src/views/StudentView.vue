<template>
  <body style="margin: 0;">
  <div class="header">
    <div class="user-logo">
      <img class="user-logo-png" src="/images/user.png" alt="loading">
    </div>
    <div class="username">{{ user.username }}</div>
    <div class="log-button">
      <button class="log-btn" @click="logOut">LOGOUT</button>
    </div>
  </div>
  <div class="main-content">
    <div class="side-bar">
      <div class="side-bar-bttn">
        <button class="sd-btn">Personal schedule</button>
      </div>
      <div class="side-bar-bttn">
        <button class="sd-btn">Subject register</button>
      </div>
      <div class="side-bar-bttn">
        <button class="sd-btn">Registration of classes</button>
      </div>
    </div>
    <div class="schedule">
      <div class="choosed-button">
        <button class="c-btn">Personal schedule</button>
      </div>
      <div class="choosed-data">
        <div class="data-picker">Data picker</div>
      </div>
      <div class="main-schedule">
        <div class="schedule-table">
          <div class="table-time">

          </div>
          <div class="table-monday cell">
            Monday
          </div>
          <div class="table-thusday cell">
            Thusday
          </div>
          <div class="table-wednesday cell">
            Wednesday
          </div>
          <div class="table-thursday cell">
            Thursday
          </div>
          <div class="table-friday cell">
            Friday
          </div>
          <div class="time-div">
            <div>7<sup>00</sup></div>
            <div>8<sup>00</sup></div>
            <div>9<sup>00</sup></div>
            <div>10<sup>00</sup></div>
            <div>11<sup>00</sup></div>
            <div>12<sup>00</sup></div>
            <div>13<sup>00</sup></div>
            <div>14<sup>00</sup></div>
            <div>15<sup>00</sup></div>
            <div>16<sup>00</sup></div>
            <div>17<sup>00</sup></div>
            <div>18<sup>00</sup></div>
            <div>19<sup>00</sup></div>
            <div>20<sup>00</sup></div>
          </div>
          <div class="lecture cell">
            IIS LECTURE
          </div>
          <div class="cell"></div>

          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>

        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
import axios from "axios";
import store from "@/store";
import router from "@/router";
import async from "async";

export default {
  data(){
    return{
      user : {}
    }
  },

  methods:{
    logOut(){
      localStorage.removeItem('token');
      localStorage.removeItem('isAuth');
      store.commit('setToken', '');
      store.commit('setIsAuth', false);
      router.push('/')
    },
    async getUser(){
      try{
        const token = localStorage.getItem('token');
        if (token) {
          store.commit('setToken', token);
          store.commit('setIsAuth', true);
        }

        const headers = {
          'Authorization': 'Bearer ' + store.state.token,
        };
        axios.get('http://127.0.0.1:8000/api/my-info', {headers:headers})
            .then(response => {
              console.log('Ответ сервера:', response.data);
              this.user = response.data;

            })
            .catch(error => {
              console.error('Ошибка при отправке запроса');
            });
      }catch (error){
        console.log(error);
      }
    },
  },

  mounted() {
      this.getUser();
  },

}
</script>

<style scoped>
html {
  overflow-y: hidden;
}
.header{
  background: none;
  border-bottom: 2px solid #151832;
  border-radius: 10px;
  min-height: 70px;
  display: flex;
  align-items: center;
}
.user-logo-png{
  margin-left: 40px;
  width: 35px;
}
.username{
  margin-left: 10px;
  font-size: 20px;
  font-weight: bold;
}
.log-button{
  margin-left: auto;
  margin-right: 20px
}
.log-btn{
  background: #151832;
  padding: 13px 35px;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 15px;
  font-size: 20px;
  cursor: pointer;

}
.main-content{
  display: grid;
  grid-template-columns: 1fr 4fr;

}
.side-bar{
  display: flex;
  background: none;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  min-height: 90vh;
  border-right: 2px solid #151832;
}
.schedule{
  background-color: none;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}
.side-bar-bttn{
  width: 90%;
}
.sd-btn{
  width: 100%;
  margin-top: 50px;
  background: #4369C6;
  color: white;
  border: none;
  border-radius: 15px;
  padding: 15px 40px;
  font-size: 17px;
  font-weight: bold;
}
.choosed-button{
  display: flex;
  width: 100%;
  height: 45px;
  justify-content: center;
  align-items: flex-start;
  background: none;
}
.c-btn{
  height: 100%;
  background: #4369C6;
  color: white;
  border: none;
  border-radius: 15px;
  margin-top: 6px;
  padding: 0 40px;
  font-size: 20px;
  font-weight: bold;
}
.main-schedule{
  display: flex;
  flex: 1;
  justify-content: center;
  align-items: center;
  background: none;
}
.choosed-data{
  display: flex;
  justify-content: flex-end;
  height: 40px;
}
.data-picker{
  margin-right: 30px;
  width: 20%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid black;
}
.schedule-table{
  display: grid;
  grid-template-columns: 30px repeat(5, 1fr);
  grid-template-rows: 50px repeat(14, 1fr);
  width: 90%;
  height: 90%;
  border: 4px solid #151832;
  border-radius: 10px;

}
.time-div{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  background: none;
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 2;
  grid-row-end: 16;
}
.cell{
  display: flex;
  border-left: 1px solid #151832;
  border-right: 1px solid #151832;
  border-top: 1px solid gray;
  border-bottom: 1px solid gray;
  justify-content: center;
  align-items: center;
  font-size: large;
  font-weight: bold;
}
.lecture{

  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 5;
  grid-row-end: 7;
  background: greenyellow;
  border-radius: 10px;
}
</style>