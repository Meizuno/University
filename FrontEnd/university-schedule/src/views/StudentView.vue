<template>
  <navigation
      class="nav-bar"
      :username="user.username"
      :status="'student'"
      :buttons="buttons"
  >

  </navigation>
  <div class="main-container">
    <div class="schedule">
      <div class="time-div">
        <div>8 am</div>
        <div>9 am</div>
        <div>10 am</div>
        <div>11 am</div>
        <div>12 am</div>
        <div>13 am</div>
        <div>14 am</div>
        <div>15 am</div>
        <div>16 am</div>
      </div>
      <div class="days-div">
        <div class="day-cell">
          <div>Monday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div >Tuesday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Wednesday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Thursday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Friday</div>
          <div>dd.mm</div>
        </div>
      </div>

      <div class="Monday">

        <div class="lecture_two_hours" style="grid-column-start: 2;">
          <schedule-cell></schedule-cell>
        </div>
        <div class="lecture_two_hours" style="grid-column-start: 4;">
          <schedule-cell :type="'Lecture'"></schedule-cell>
        </div>

        <div class="lecture_two_hours" style="grid-column-start: 3;">
          <schedule-cell></schedule-cell>
        </div>




        <div class="lecture_two_hours" style="grid-column-start: 6;">
          IMS Lecture
        </div>
      </div>
      <div class="Tuesday">
        <div class="lecture_two_hours" style="grid-column-start: 3; background: #FFB13B">
          IMP Exercise
        </div>
      </div>
      <div class="Wednesday"> </div>
      <div class="Thursday">
        <div class="lecture_two_hours" style="grid-column-start: 2; background: #FFB13B">
          IZP Exercise
        </div></div>
      <div class="Friday"> </div>

    </div>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import ScheduleCell from "@/components/ScheduleCell.vue";

export default {
  components: {ScheduleCell, Navigation},
  data(){
    return{
      user: {},
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'selected', route:'/student'},
        {text:'Subjects', class:'not-selected', route:'/student/subjects'},
        {text:'Activities', class:'not-selected', route:'/student/activities'},
      ]
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
  },
  mounted() {
    this.getUser();
  }

}
</script>

<style scoped>
.nav-bar{
  margin-top: 5px;
  margin-bottom: 0;
}
.main-container{
  justify-content: center;
  display: flex;
  width: 100%;
  height: 85vh;
}
.schedule{
  margin-top: 10px;
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  grid-auto-rows: minmax(100px, auto);
  width: 95%;
  min-height: 90%;
  height: fit-content;
  border: 4px solid #151832;
  background: white;
  border-radius: 10px;
  padding-bottom: 10px;
}
.time-div{
  font-weight: bold;
  display: grid;
  grid-template-columns: repeat(9,1fr);
  align-items: center;
  justify-items: center;
  grid-column-start: 2;
  grid-column-end: 11;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
}
.days-div{
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  grid-column-start: 1;
  grid-row-start: 2;
  grid-row-end: 7;
}
.day-cell{
  display: flex;
  flex-direction: column;
  font-weight: bold;
  justify-content: center;
  align-items: center;
}
.Thursday,
.Friday,
.Wednesday,
.Tuesday,
.Monday{
  display: grid;
  grid-template-columns: repeat(9,1fr);

  grid-column-start: 2;
  grid-column-end: 11;

  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
  align-items: center;

}

.lecture_two_hours{
  display: flex;
  justify-content: center;
  min-height: 90px;
  align-items: center;
  background: #84D296;
  border-radius: 20px;
  grid-column-end: span 2;
}

</style>