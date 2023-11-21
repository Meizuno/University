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
    <CalendarTest style="margin-top: 5px"
                  :activities="activities"
                  :key="calendarKey"
                  :is-scheduler="false"
                  @register_activity="registerActivity"
                  @unregister_activity="unregisterActivity"
    >
    </CalendarTest>
  </div>

</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import Calendar from "@/components/Calendar.vue";
import CalendarTest from "@/components/CalendarTest.vue";

export default {
  components: {CalendarTest, Calendar, Navigation},
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
      registeredActivities: [],

    }
  },
  methods: {
    registerActivity(activity){
      axios.post(`http://127.0.0.1:8000/api/student_register_activity/${this.user.id}/${activity.id}`)
          .then(response=>{
            this.getStudentActivities();
          })
          .catch(e=>{
            console.log(e);
          })
    },
    unregisterActivity(activity){
      axios.delete(`http://127.0.0.1:8000/api/student_register_activity/${this.user.id}/${activity.id}`)
          .then(response=>{
            this.getStudentActivities();
          })
          .catch(e=>{
            console.log(e);
          })
    },
    async getScheduleActivities(subjectId){
      await axios.get(`http://127.0.0.1:8000/api/subject_activities/${subjectId}`)
          .then(response=>{
            this.activities = response.data.data;
            this.getStudentActivities();
          })
          .catch(e=>{
            console.log(e);
          })
    },
    updateCalendarKey() {
      this.calendarKey += 1;
    },
    activityTypes(){
      this.activities.forEach(activity => {
        const registeredActivity = this.registeredActivities.find(
            registered => registered.id === activity.id
        );
        activity.regtype = registeredActivity ? 'registered' : 'unregistered';
      });
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
    async getStudentActivities(){
      // http://127.0.0.1:8000/api/activity?students=10&subject=3
      await axios.get(`http://127.0.0.1:8000/api/student_activities_subject/${this.user.id}/${this.selectedSubject}`)
          .then(response=>{
            this.registeredActivities = response.data.data;
            this.activityTypes();
            this.updateCalendarKey();
          })
          .catch(e=>{
            console.log(e);
          })
    }
  },
  watch: {
    async selectedSubject(newValue, oldValue) {
        await this.getScheduleActivities(newValue);
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