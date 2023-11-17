<template>

  <navigation class="nav-bar"
              :username="user.username"
              :status="'student'"
              :buttons="buttons"
  ></navigation>
  <div class="main-container">
    <div class="subject-picker">
      <div class="subject-title">
        Subject:
      </div>
      <div class="select-body">
        <select v-model="selectedSubject" class="custom-select">
          <option
              v-for="subject in registeredSubjects"
              :key="subject.id"
              :value="subject.id"
          >
            {{ subject.code }}
          </option>
        </select>
      </div>

    </div>
    <Calendar style="margin-top: 5px"
              :activities="activities"
              :key="calendarKey">
    </Calendar>
  </div>

</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import Calendar from "@/components/Calendar.vue";

export default {
  components: {Calendar, Navigation},
  data(){
    return{
      user: {},
      registeredSubjects: [],
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'not-selected', route:'/student'},
        {text:'Subjects', class:'not-selected', route:'/student/subjects'},
        {text:'Activities', class:'selected', route:'/student/activities'},
      ],
      selectedSubject: 0,
      activities: [],
      calendarKey: 0,

    }
  },
  methods: {
    async getScheduleActivities(subjectId){
      await axios.get(`http://127.0.0.1:8000/api/subject_activities/${subjectId}`)
          .then(response=>{
            this.activities = response.data.data;
            this.updateCalendarKey();
          })
          .catch(e=>{
            console.log(e);
          })
    },
    updateCalendarKey() {
      this.calendarKey += 1;
    },
    getUserAndSubjects(){
      try{
        const storedUser = localStorage.getItem('user');
        if(storedUser){
          this.user = JSON.parse(storedUser);
          try{
            axios.get(`http://127.0.0.1:8000/api/student_subjects/${this.user.id}`)
                .then(response => {
                  this.registeredSubjects = response.data.data;
                })
                .catch(error => {
                  console.error('Error response: ', error);
                });
          }catch (e) {
            console.log(e);
          }
        }
      } catch (error){
        console.log(error);
      }
    },
  },
  watch: {
    selectedSubject(newValue, oldValue) {
        this.getScheduleActivities(newValue);
    },
  },
  mounted() {
    this.getUserAndSubjects();
  }
}
</script>

<style scoped>
.nav-bar{
  margin-top: 5px;
  margin-bottom: 0;
}
.main-container{
  width: 100%;
  height: 90vh;
  display: flex;
  flex-direction: column;
}
.subject-picker{
  width: 190px;
  height: 60px;
  background: #81d4fa;
  margin-top: 20px;
  margin-left: 30px;
  display: flex;
  align-items: center;
  font-size: 22px;
  font-weight: bold;
  border: 3px solid black;
  border-radius: 10px;

}
.select-body{
  margin-left: 15px;
  height: 70%;
  display: flex;
  flex-grow: 1;
  align-items: center;

}
.custom-select{
  height: 70%;
  width: 80%;
  margin-left: 10px;
  font-size: 18px;
  border: 2px solid black;
}
.subject-title{
  margin-left: 10px;
}
</style>