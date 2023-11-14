<template>
  <div class="request_card">
    <div class="header">
      <div class="head-name">
        IIS Lecture
      </div>
      <div class="cross">
        <cross></cross>
      </div>
    </div>
    <div class="body">
      <div class="repeating">Repeating: </div>
      <div class="duration">Duration: </div>
      <div class="notes">Notes: </div>
    </div>
  </div>
</template>

<script>
import Cross from "@/components/icons/Cross.vue";

export default {
  components: {Cross}

}
</script>

<style scoped>
.request_card{
  display: flex;
  flex-direction: column;
  background: #3c763d;
  width: 340px;
  min-height: 170px;
  height: fit-content;
  border: 3px solid black;
  margin-top: 5px;
}
.header{
  background: teal;
  height: 40px;
  display: flex;
  align-items: center;
  font-size: 25px;
  font-weight: bold;
}
.body{
  height: 75%;
  display: flex;
  flex-direction: column;
  font-size: 25px;
  padding-top: 3px;
  padding-left: 3px;
}
.cross{
  background: #1f69c0;
  margin-left: auto;
  width: 13%;
  height: 100%;
}
.head-name{
  height: 100%;
  display: flex;
  align-items: center;
  margin-left: 5px;
}
</style>