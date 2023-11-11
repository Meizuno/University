<template>
    <div class="cell" :style="colors.outside">
        <div :style="colors.inside">
            <p :style="colors.title">Subject</p>
            <p class="var">{{ activity.subject.code }}</p>
        </div>
        <div :style="colors.inside">
            <p :style="colors.title">Room</p>
            <p class="var">105</p>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    activity: {
      type: Object,
      default: {}
    }
  },
  data() {
    return{
      colors: {
        outside: { 'background-color': "#84D296" },
        inside: { 'background-color': "#9DDBAB" },
        title: { 'color': "#E2F4E6" }
      }
    }
  },
  mounted() {
    this.UpdateStyles()
  },
  methods: {
    UpdateStyles() {
      switch (this.activity.activity_type.description) {
        case "Lecture":
          this.colors = {
            outside: { 'background-color': "#84D296" },
            inside: { 'background-color': "#9DDBAB" },
            title: { 'color': "#E2F4E6" }
          };
          break;
        case "Practice":
          this.colors = {
            outside: { 'background-color': "#FFBB56" },
            inside: { 'background-color': "#FFB13B" },
            title: { 'color': "#FFD89D" }
          };
          break;
        case "Laboratory":
          this.colors = {
            outside: { 'background-color': "#45BFFF" },
            inside: { 'background-color': "#41B4F0" },
            title: { 'color': "#C5CAF6" }
          };
          break;
        case "Exam":
          this.colors = {
            outside: { 'background-color': "#717EEE" },
            inside: { 'background-color': "#8993ED" },
            title: { 'color': "#C5CAF6" }
          };
          break;
      }
    }
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

.cell > div {
    text-align: center;
    padding: 3px 10px;
    border-radius: 10px;
}

.cell > div > p:first-child {
    font-size: 12px;
}

.cell > div > p {
    margin: 0;
}

.var {
    font-size: 28px;
}

</style>