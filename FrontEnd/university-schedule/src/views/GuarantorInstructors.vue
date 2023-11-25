<template>
  <navigation
      class="nav-bar"
      :username="'test username'"
      :status="'guarantor'"
      :buttons="buttons"
  >
  </navigation>
  <ListOfInstructors
      :instructors="instructors"
      :registered_instructors="registered_instructors"
      @unregister_instructor="unregisterInstructor"
      @instructor_register2="registerInstructor"
  >
  </ListOfInstructors>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import RegisterSubjectCard from "@/components/RegisterSubjectCard.vue";
import RegisteredSubjectCard from "@/components/RegisteredSubjectCard.vue";
import RegisterInstructorCard from "@/components/RegisterInstructorCard.vue";
import ListOfInstructors from "@/components/ListOfInstructors.vue";
import {toast} from "vue3-toastify";

export default {
  components: {ListOfInstructors, RegisterInstructorCard, RegisteredSubjectCard, RegisterSubjectCard, Navigation},
  data(){
    return{
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'not-selected', route:'/guarantor'},
        {text:'Instructors', class:'selected', route: '/guarantor/instructors'},
        {text:'Activities', class:'not-selected', route: '/guarantor/activities'},
      ],
      instructors : [],
      registered_instructors: [],
      guarantorSubject : {},
    }
  },

  methods:{
    async getSubject(){
      try {
        // change to user.id
        const storedSubject = localStorage.getItem('subject');
        if(storedSubject) {
          this.guarantorSubject = JSON.parse(storedSubject);
        }

      }catch (e) {
        console.log(e);
      }

    },
    getInstructors(){
      try {
        axios.get("http://127.0.0.1:8000/api/get_all_instructors")
            .then(response => {
              const allInstructors = response.data.data;
              const tempInstructors = [];
              const tempRegisteredInstructors = [];

              allInstructors.forEach(instructor => {
                if (this.guarantorSubject.instructors.includes(instructor.id)) {
                  tempRegisteredInstructors.push(instructor);
                } else {
                  tempInstructors.push(instructor);
                }
              });

              this.instructors = tempInstructors;
              this.registered_instructors = tempRegisteredInstructors;
            })
            .catch(error => {
              console.error('Error response: ', error);
            });
      } catch (e) {
        console.log(e);
      }
    },

    async loadData(){
      await this.getSubject();
      await this.getInstructors();
    },
    unregisterInstructor(instructor) {
      try {
        axios.delete(`http://127.0.0.1:8000/api/register_instructor/${instructor.id}/${this.guarantorSubject.id}`)
            .then(response => {
              const index = this.registered_instructors.findIndex(regInstructor => regInstructor.id === instructor.id);
              if (index !== -1) {
                const removedInstructor = this.registered_instructors.splice(index, 1)[0];
                this.instructors.push(removedInstructor);
              } else {
                console.log("Instructor not found in registered instructors.");
              }
              toast.success("Instructor was successfully unregistered!", {
                autoClose: 5000,
                position: toast.POSITION.BOTTOM_RIGHT,
              });
            });
      } catch (e) {
        console.error(e);
      }
    },

    registerInstructor(instructor) {
      try {
        axios.post(`http://127.0.0.1:8000/api/register_instructor/${instructor.id}/${this.guarantorSubject.id}`)
            .then(response => {
              console.log(response.data);
              const index = this.instructors.findIndex(inst => inst.id === instructor.id);
              if (index !== -1) {
                const removedInstructor = this.instructors.splice(index, 1)[0];
                this.registered_instructors.push(removedInstructor);
              } else {
                console.log("Instructor not found in instructors list.");
              }
              toast.success("Instructor was successfully registered!", {
                autoClose: 5000,
                position: toast.POSITION.BOTTOM_RIGHT,
              });
            });
      } catch (e) {
        console.error(e);
      }
    },

  },

  mounted() {
    this.loadData();
  }

}
</script>

<style scoped>

</style>