<template>
  <navigation class="nav-bar"></navigation>

  <div class="main-container">
    <div class="schedule">
      <div class="time-div">
        <div>8 am</div>
        <div>9 am</div>
        <div>10 am</div>
        <div>11 am</div>
        <div>12 am</div>
        <div>13 am</div>
        <div>14 am</div>
        <div>15 am</div>
        <div>16 am</div>
      </div>
      <div class="days-div">
        <div class="day-cell">
          <div>Monday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div >Tuesday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Wednesday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Thursday</div>
          <div>dd.mm</div>
        </div>
        <div class="day-cell">
          <div>Friday</div>
          <div>dd.mm</div>
        </div>
      </div>

      <div class="Monday">
        <div class="lecture_two_hours" style="grid-column-start: 2">
          IIS Lecture
        </div>
        <div class="lecture_two_hours" style="grid-column-start: 6">
          IMS Lecture
        </div>
      </div>
      <div class="Tuesday">
        <div class="lecture_two_hours" style="grid-column-start: 3; background: #FFB13B">
          IMP Exercise
        </div>
      </div>
      <div class="Wednesday"> </div>
      <div class="Thursday">
        <div class="lecture_two_hours" style="grid-column-start: 2; background: #FFB13B">
          IZP Exercise
        </div></div>
      <div class="Friday"> </div>

    </div>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";

export default {
  components: {Navigation},
  Authorization() {
    this.$router.push('/authorization');
  }
}
</script>

<style scoped>
.nav-bar{
  margin-top: 5px;
  margin-bottom: 0;
}
.main-container{
  justify-content: center;
  display: flex;
  width: 100%;
  height: 85vh;
}
.schedule{
  margin-top: 10px;
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  grid-template-rows: repeat(6, 1fr);
  width: 95%;
  height: 90%;
  border: 4px solid #151832;
  background: white;
  border-radius: 10px;
  padding-bottom: 10px;
}
.time-div{
  font-weight: bold;
  display: flex;
  justify-content: space-around;
  align-items: center;
  grid-column-start: 2;
  grid-column-end: 11;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
}
.days-div{
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  grid-column-start: 1;
  grid-row-start: 2;
  grid-row-end: 7;
}
.day-cell{
  display: flex;
  flex-direction: column;
  font-weight: bold;
  justify-content: center;
  align-items: center;
}
.Thursday,
.Friday,
.Wednesday,
.Tuesday,
.Monday{
  display: grid;
  grid-template-columns: repeat(9,1fr);
  grid-column-start: 2;
  grid-column-end: 11;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
  align-items: center;
}

.lecture_two_hours{
  display: flex;
  justify-content: center;
  align-items: center;
  background: #84D296;
  border-radius: 20px;
  grid-column-end: span 2;
  height: 90%;
}
</style>