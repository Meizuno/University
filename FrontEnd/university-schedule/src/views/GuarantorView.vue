<template>
  <navigation
      class="nav-bar"
      :username="'test username'"
      :status="`guarantor ${guarantorSubject.code}`"
      :buttons="buttons"
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
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'selected', route:'/guarantor'},
        {text:'Instructors', class:'not-selected', route: '/guarantor/instructors'},
        {text:'Activities', class:'not-selected', route: '/guarantor/activities'},
      ],
      user : {

      },
      guarantorSubject : {},
      activities: [],
      calendarKey: 0,
    }
  },

  methods: {
    async getGuarantorSubjectAndActivities(){
      try {
        // change to user.id
        axios.get("http://127.0.0.1:8000/api/subject?guarantor_id=2")
            .then(response => {
              this.guarantorSubject = response.data.data[0];
              localStorage.setItem('subject', JSON.stringify(this.guarantorSubject));
              axios.get(`http://127.0.0.1:8000/api/subject_activities/${this.guarantorSubject.id}`)
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
  mounted() {
    this.getGuarantorSubjectAndActivities();
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