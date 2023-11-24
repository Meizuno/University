<template>
  <div class="modal">
    <div class="modal-content">
      <h2>{{ activity.title }}</h2>
      <p>{{ activity.description }}</p>
      <textarea v-model="notes" placeholder="Enter notes..."></textarea>
      <div class="buttons">
        <button @click="register">Register activity</button>
        <button @click="close">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    activity: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      notes: '',
    };
  },
  methods: {
    register() {
      this.$emit('register-activity', { activity: this.activity, notes: this.notes });
      this.close();
    },
    close() {
      this.$emit('close-modal');
    },
  },
};
</script>
<style scoped>

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
}

textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
  font-size: 20px;
}

.buttons {
  display: flex;
  justify-content: space-between;
}

button {
  font-size: 20px;
  padding: 10px 20px;
  border-radius: 5px;
  border: 2px solid black;
  cursor: pointer;
  margin-left: 5px;
  margin-right: 5px;
}

button:first-child {
  background-color: #00cc00;
  color: white;
}

button:last-child {
  background-color: #ff3300;
  color: white;
}
</style>
