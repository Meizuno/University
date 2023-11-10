<template>
  <div class="card">
    <div class="code">{{ this.code }}</div>
    <div class="subject-info">
      <div class="subject-name">{{ this.sName }}</div>
      <div class="subject-capacity">({{ this.sCapacity }})</div>
    </div>
    <div class="register" @click="registerSubject(this.user_id, this.sId)">
      <checkmark></checkmark>
    </div>
  </div>
</template>

<script>
import Checkmark from "@/components/icons/Checkmark.vue";
import axios from "axios";

export default {
  components: {Checkmark},
  data(){
    return{
      user_id: Number,
    }
  },
  methods: {
    registerSubject(user_id, subject_id){
      axios.post(`http://127.0.0.1:8000/api/register/${user_id}/${subject_id}`)
          .then(response => {
            console.log("ok unregister");
            this.$emit('subjectsUpdate');
          })
          .catch(error => {
            console.error('Error response: ', error);
          });
    }
  },
  // передавать юзера через пропс
  mounted() {
    const storedUser = localStorage.getItem('user');
    if(storedUser){
      this.user_id = JSON.parse(storedUser).id;
    }
  },
  props: {
    code: {
      type: String,
      required: true,
    },
    sName: {
      type: String,
      required: true,
    },
    sCapacity: {
      type: String,
      required: true,
    },
    sId:{
      type: Number,
      required: true,
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
  height: 53px;
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
.subject-capacity{
  margin-left: auto;
  margin-right: 10px;
}
</style>