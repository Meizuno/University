<template>
    <div class="cell" :style="outside">
      <div class="col-1" :style="inside">
          <p :style="title">Subject</p>
          <p class="var">{{ code }}</p>
      </div>
      <div class="col-2">
        <RoomPicker />
        <div class="sub-col">
          <DayPicker />
          <TimePicker />
        </div>
      </div>
    </div>
</template>

<script>

import RoomPicker from './RoomPicker.vue';
import DayPicker from './DayPicker.vue';
import TimePicker from './TimePicker.vue';

export default {
  props: {
    type: {
      type: String,
      default: 'Lecture'
    },
    code: {
      type: String,
      default: 'XXX'
    }
  },
  components: {
    RoomPicker,
    DayPicker,
    TimePicker
  },
  computed: {
    outside() {
      let backgroundColor;
      switch (this.type) {
        case 'Lecture':
          backgroundColor = '#84D296';
          break;
        case 'Practice':
          backgroundColor = '#FFBB56';
          break;
        case 'Laboratory':
          backgroundColor = '#45BFFF';
          break;
        case 'Exam':
          backgroundColor = '#717EEE';
          break;
      }
      return {
        backgroundColor
      };
    },
    inside() {
      let backgroundColor;
      switch (this.type) {
        case 'Lecture':
          backgroundColor = '#9DDBAB';
          break;
        case 'Practice':
          backgroundColor = '#FFB13B';
          break;
        case 'Laboratory':
          backgroundColor = '#41B4F0';
          break;
        case 'Exam':
          backgroundColor = '#8993ED';
          break;
      }
      return {
        backgroundColor
      };
    },
    title() {
      let color;
      switch (this.type) {
        case 'Lecture':
          color = '#E2F4E6';
          break;
        case 'Practice':
          color = '#FFD89D';
          break;
        case 'Laboratory':
          color = '#C5CAF6';
          break;
        case 'Exam':
          color = '#A2DAF8';
          break;
      }
      return {
        color
      };
    },
  }
};
</script>

<style scoped>

.cell {
    display: flex;
    gap: 10px;
    width: fit-content;
    justify-content: center;
    color: white;
    padding: 15px 10px;
    border-radius: 20px;
}

.col-1 {
    text-align: center;
    padding: 3px 10px;
    border-radius: 10px;
}

.col-1 > p:first-child {
    font-size: 12px;
}

.col-1 > p {
    margin: 0;
}

.var {
    font-size: 28px;
}

.col-2{
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.sub-col{
  display: flex;
  gap: 5px;
}

</style>