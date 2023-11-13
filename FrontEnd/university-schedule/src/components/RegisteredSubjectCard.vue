<template>
  <div class="card">
    <div class="code">{{ this.subject.code }}</div>
    <div class="subject-info">
      <div class="subject-name">{{ this.subject.name }}</div>
    </div>
    <div class="register" @click="unregisterSubject(this.user_id,this.subject.id)">
      <cross></cross>
    </div>
  </div>
</template>

<script>
import Cross from "@/components/icons/Cross.vue";
import axios from "axios";

export default {
  components: {Cross},
  data(){
    return{
      user_id : Number,
    }
  },
  props: {
    subject:{
      type: Object,
      required: true,
    },
  },
  methods: {
    unregisterSubject(user_id, subject_id){
      axios.delete(`http://127.0.0.1:8000/api/register/${user_id}/${subject_id}`)
          .then(response => {
            console.log("ok unregister");
            this.$emit('subjectsUpdate');
          })
          .catch(error => {
            console.error('Error response: ', error);
          });
    }
  },
  mounted() {
    const storedUser = localStorage.getItem('user');
    if(storedUser){
      this.user_id = JSON.parse(storedUser).id;
    }
  },

}
</script>

<style scoped>
.card{
  background: white;
  display: flex;
  border: 3px solid black;
  width: 550px;
  height: 57px;
  font-size: 22px;
  align-items: center;
  margin-bottom: 10px;
}
.subject-info{
  display: flex;
  margin-left: 20px;
  background: teal;
  width: 70%;
  height: 80%;
  align-items: center;
  background: rgba(0, 0, 0, 0.1);
  padding-left: 5px;
  padding-right: 5px;
}
.code{
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 10px;
  height: 80%;
  background: rgba(0, 0, 0, 0.1);
  width: 40px;
  padding: 0 3px;
}
.register{
  display: flex;
  align-items: center;
  margin-left: auto;
  margin-right: 10px;
  height: 80%;
  background: rgba(0, 0, 0, 0.1);
  padding-left: 3px;
  padding-right: 3px;
  cursor: pointer;
}

</style>