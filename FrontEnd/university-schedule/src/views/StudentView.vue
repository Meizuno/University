<template>
  <navigation
      class="nav-bar"
      :username="user.username"
      :status="'student'"
      :buttons="buttons"
  >

  </navigation>
  <div class="main-container">

    <div class="range-picker">
      <div class="picker-data">
        <div class="date-range">
          {{ startDate }} - {{ endDate }}
        </div>
        <div class="arrow-buttons">
          <button @click="decreaseDate()" class="bttn">←</button>
          <button @click="increaseDate()" class="bttn">→</button>
        </div>
      </div>
    </div>

    <Calendar style="margin-top: 10px"></Calendar>

  </div>



</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import ScheduleCell from "@/components/ScheduleCell.vue";
import RegisterInstructorCard from "@/components/RegisterInstructorCard.vue";
import GuarantRequest from "@/components/GuarantRequest.vue";
import DaysSchedule from "@/components/DaysSchedule.vue";
import Calendar from "@/components/Calendar.vue";

export default {
  components: {Calendar, DaysSchedule, GuarantRequest, RegisterInstructorCard, ScheduleCell, Navigation},
  data(){
    return{
      user: {},
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'selected', route:'/student'},
        {text:'Subjects', class:'not-selected', route:'/student/subjects'},
        {text:'Activities', class:'not-selected', route:'/student/activities'},
      ],
      startDate: '18.09.2023',
      endDate: '24.09.2023',
    }
  },

  methods:{
    Authorization() {
      this.$router.push('/authorization');
    },
    async getUser(){
      try{
        const token = localStorage.getItem('token');

        const headers = {
          'Authorization': 'Bearer ' + token,
        };
        axios.get('http://127.0.0.1:8000/api/my-info', {headers:headers})
            .then(response => {
              console.log('Ответ сервера:', response.data);
              this.user = response.data;
              localStorage.setItem('user', JSON.stringify(this.user));

            })
            .catch(error => {
              console.error('Error send request');
            });
      }catch (error){
        console.log(error);
      }
    },
    formatDate(date) {
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();

      return `${day < 10 ? '0' : ''}${day}.${month < 10 ? '0' : ''}${month}.${year}`;
    },
    increaseDate() {
      const startDateArr = this.startDate.split('.').map(Number);
      const endDateArr = this.endDate.split('.').map(Number);

      const start = new Date(startDateArr[2], startDateArr[1] - 1, startDateArr[0]);
      const end = new Date(endDateArr[2], endDateArr[1] - 1, endDateArr[0]);

      start.setDate(start.getDate() + 7);
      end.setDate(end.getDate() + 7);

      this.startDate = this.formatDate(start);
      this.endDate = this.formatDate(end);
    },
    decreaseDate() {
      const startDateArr = this.startDate.split('.').map(Number);
      const endDateArr = this.endDate.split('.').map(Number);

      const start = new Date(startDateArr[2], startDateArr[1] - 1, startDateArr[0]);
      const end = new Date(endDateArr[2], endDateArr[1] - 1, endDateArr[0]);

      start.setDate(start.getDate() - 7);
      end.setDate(end.getDate() - 7);

      this.startDate = this.formatDate(start);
      this.endDate = this.formatDate(end);
    },
  },
  mounted() {
    this.getUser();
  },

}
</script>

<style scoped>
.nav-bar{
  margin-top: 5px;
  margin-bottom: 0;
}
.main-container{
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 90vh;
}
.range-picker{
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: end;
  align-items: center;
  margin-top: 30px;
}
.picker-data{
  display: flex;
  background: white;
  align-items: center;
  height: 100%;
  width: 300px;
  border: 3px solid black;
  border-radius: 10px;
  margin-right: 40px;
}
.date-range{
  margin-right: 15px;
  margin-left: 15px;
  font-size: 16px;
  font-weight: bold;
}
.arrow-buttons{
  margin-right: 5px;
  display: flex;
  justify-content: space-between;
  margin-left: auto;

}
.bttn{
  margin-right: 10px;
  border: 3px solid darkred;
  cursor: pointer;
  height: 25px;
  width: 32px;

}
</style>