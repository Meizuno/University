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
    outsideColor: {
      type: String,
      default: 'red'
    },
    insideColor: {
      type: String,
      default: 'red'
    },
    titleColor: {
      type: String,
      default: 'white'
    }
  },
  computed: {
    outside() {
      return {
        backgroundColor: this.outsideColor
      };
    },
    inside() {
      return {
        backgroundColor: this.insideColor
      };
    },
    title() {
      return {
        color: this.titleColor
      };
    }
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