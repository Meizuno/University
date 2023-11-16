<template>
  <div class="card">
    <div class="instructor_name">PhD {{ instructor.first_name }} {{ instructor.last_name }}</div>
    <div class="checkmark" @click="sendDataToList">
      <checkmark></checkmark>
    </div>

  </div>
</template>

<script>
import Checkmark from "@/components/icons/Checkmark.vue";

export default {
  components: {Checkmark},
  data(){
    return{

    }
  },
  props:{
    instructor:{
      type: Object,
      required: true,
    }
  },
  methods:{
    sendDataToList(){
      this.$emit('instructor_register', this.instructor);
    }
  },


}
</script>

<style scoped>
.card{
  display: flex;
  width: 400px;
  height: 50px;
  background: none;
  border: 4px solid black;
  margin-top: 20px;
  border-radius: 15px;
  align-items: center;
}
.instructor_name{
  display: flex;
  justify-content: left;
  align-items: center;
  border-right: 3px solid black;
  font-size: 23px;
  font-weight: bold;
  margin-left: 10px;
  height: 100%;
  width: 80%;
}
.checkmark{
  margin-left: auto;
  height: 100%;
  margin-right: 5px;
  cursor: pointer;
}
</style>