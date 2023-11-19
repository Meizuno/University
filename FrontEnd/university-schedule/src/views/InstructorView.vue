<template>
  <navigation
      class="nav-bar"
      :username="'instructor username'"
      :status="`guarantor`"
      :buttons="buttons"
  ></navigation>
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

    <CalendarTest
        style="margin-top: 5px"
        :is-scheduler="false"
        :activities="activities"
        :key="calendarKey"
    ></CalendarTest>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import CalendarTest from "@/components/CalendarTest.vue";
import axios from "axios";

export default {
  components: {CalendarTest, Navigation},
  data() {
    return {
      buttons: [
        {text: 'Home', class: 'not-selected', route: '/'},
        {text: 'Schedule', class: 'selected', route: '/instructor'},
        {text: 'Activities', class: 'not-selected', route: '/instructor/activities'},
      ],
      startDate: '18.09.2023',
      endDate: '24.09.2023',
      activities: [],
      calendarKey: 0,
      user: {},
    }
  },
  methods:{
    // get activities /activity?instructor=id
    // get subject /subject?instructors=id
    getActivities(){
      const date_from = this.convertDate(this.startDate);
      const date_to = this.convertDate(this.endDate);
      // set to dynamic
      axios.get(`http://127.0.0.1:8000/api/instructor_activities/5?date_from=${date_from}&date_to=${date_to}`)
          .then(response=>{
            this.activities = response.data.data;
            this.updateKey();
          })
          .catch(e=>{
            console.log(e);
          })
    },

    updateKey(){
      this.calendarKey += 1;
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
      this.getActivities();
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
      this.getActivities();
    },
    convertDate(inputDate) {
      const [day, month, year] = inputDate.split('.');
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    },
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