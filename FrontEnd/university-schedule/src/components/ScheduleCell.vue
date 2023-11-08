<template>
    <div class="practice" :style="outside">
        <div :style="inside">
            <p :style="title">Subject</p>
            <p class="var">ITU</p>
        </div>
        <div :style="inside">
            <p :style="title">Room</p>
            <p class="var">105</p>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'Lecture'
    }
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

.practice {
    display: flex;
    gap: 10px;
    width: fit-content;
    justify-content: center;
    color: white;
    padding: 15px 10px;
    border-radius: 20px;
}

.practice > div {
    text-align: center;
    padding: 3px 10px;
    border-radius: 10px;
}

.practice > div > p:first-child {
    font-size: 12px;
}

.practice > div > p {
    margin: 0;
}

.var {
    font-size: 28px;
}

</style>