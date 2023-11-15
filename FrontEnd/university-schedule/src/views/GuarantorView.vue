<template>
  <navigation
      class="nav-bar"
      :username="'test username'"
      :status="'guarantor'"
      :buttons="buttons"
  >
  </navigation>
  <div class="main-container">
    <DaysSchedule></DaysSchedule>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import DaysSchedule from "@/components/DaysSchedule.vue";
import axios from "axios";

export default {
  components: {DaysSchedule, Navigation},
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
    }
  },

  methods: {
    async getGuarantorSubject(){
      try {
        // change to user.id
        axios.get("http://127.0.0.1:8000/api/subject?guarantor_id=2")
            .then(response => {
              this.guarantorSubject = response.data.data;
              localStorage.setItem('subject', JSON.stringify(this.guarantorSubject));
            })
            .catch(error => {
              console.error('Error response: ', error);
            });
      }catch (e) {
        console.log(e);
      }
    }
  },
  mounted() {
    this.getGuarantorSubject();
  },
}
</script>

<style scoped>
.main-container{
  justify-content: center;
  display: flex;
  width: 100%;
  height: 90vh;
}
.test{
  height: 100%;
  width: 100%;
  background: #3c763d;
}
</style>