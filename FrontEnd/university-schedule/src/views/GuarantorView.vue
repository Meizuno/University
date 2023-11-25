<template>
  <navigation
      class="nav-bar"
  >
  </navigation>
  <div class="main-container">
    <CalendarTest
        style="margin-top: 5px"
        :activities="activities"
        :key="calendarKey"
        :is-scheduler="false"
    ></CalendarTest>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import DaysSchedule from "@/components/DaysSchedule.vue";
import axios from "axios";
import CalendarTest from "@/components/CalendarTest.vue";

export default {
  components: {CalendarTest, DaysSchedule, Navigation},
  data(){
    return{
      header: {
        "Authorization": localStorage.getItem("token"),
      },
      user: {},
      guarantorSubject: {},
      activities: [],
      calendarKey: 0,
    }
  },

  methods: {
    getUser(){
      const storedUser = localStorage.getItem('user');
      if(storedUser) {
        this.user = JSON.parse(storedUser);
      }
    },
    async getGuarantorSubjectAndActivities(){
      try {
        // change to user.id
        axios.get(`http://127.0.0.1:8000/api/subject?guarantor_id=${this.user.id}`, {headers: this.header})
            .then(response => {
              this.guarantorSubject = response.data.data[0];
              localStorage.setItem('subject', JSON.stringify(this.guarantorSubject));
              axios.get(`http://127.0.0.1:8000/api/subject_activities/${this.guarantorSubject.id}`, {headers: this.header})
                  .then(response=>{
                    this.activities = response.data.data;
                    this.updateKey();
                  })
            })
            .catch(error => {
              console.error('Error response: ', error);
            });
      }catch (e) {
        console.log(e);
      }
    },
    updateKey(){
      this.calendarKey += 1;
    }
  },
  async mounted() {
    this.getUser();
    await this.getGuarantorSubjectAndActivities();
  },
}
</script>

<style scoped>
.main-container{
  justify-content: start;
  flex-direction: column;
  display: flex;
  width: 100%;
  height: 90vh;
}
</style>