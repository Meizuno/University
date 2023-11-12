<template>
    <div class="cell" :style="colors.outside">
      <div class="col-1" :style="colors.inside">
          <p :style="colors.title">Subject</p>
          <p class="var">{{ activity.subject.code }}</p>
      </div>
      <div class="col-2">
        <div class="custom-select" ref="customSelectRoom" @click="toggleDropdownRoom">
          {{ selectedRoom || 'Room' }}
          <div v-if="isRoomOpen" class="dropdown" @click.stop>
            <div v-for="room in rooms" :key="room" @click="selectValue('room', room.number)">
              {{ room.number }}
            </div>
          </div>
        </div>
        <div class="sub-col">
          <div class="custom-select" @click="toggleDropdownDay">
            {{ selectedDay || 'Day' }}
            <div v-if="isDayOpen" class="dropdown" @click.stop>
              <div v-for="day in days" :key="day" @click="selectValue('day', day)">
                {{ day }}
              </div>
            </div>
          </div>
          <div class="custom-select" @click="toggleDropdownTime">
            {{ selectedTime || 'Time' }}
            <div v-if="isTimeOpen" class="dropdown" @click.stop>
              <div v-for="time in times" :key="time" @click="selectValue('time', time)">
                {{ time }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  props: {
    activity: {
      type: Object,
      default: {}
    },
    rooms: {
      type: Array,
      default: {}
    }
  },
  data() {
    return {
      isRoomOpen: false,
      selectedRoom: null,

      isDayOpen: false,
      selectedDay: null,
      days: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],

      isTimeOpen: false,
      selectedTime: null,
      times: ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],

      colors: {
        outside: { 'background-color': "#84D296" },
        inside: { 'background-color': "#9DDBAB" },
        title: { 'color': "#E2F4E6" }
      },
    };
  },
  created() {
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
    };
  },
  methods: {
    selectValue(option, value) {
      switch (option) {
        case "room":
          this.selectedRoom = value;
          this.isRoomOpen = false;
          break;
        case "day":
          this.selectedDay = value;
          this.isDayOpen = false;
          break;
        case "time":
          this.selectedTime = value;
          this.isTimeOpen = false;
          break;
      }
    },
    toggleDropdownRoom() {
      this.isRoomOpen = !this.isRoomOpen;
      this.isDayOpen = false;
      this.isTimeOpen = false;
      if (this.isRoomOpen) {
        this.$nextTick(() => {
          this.$refs.dropdown.focus();
        });
      }
    },
    toggleDropdownDay() {
      this.isDayOpen = !this.isDayOpen;
      this.isRoomOpen = false;
      this.isTimeOpen = false;
      if (this.isDayOpen) {
        this.$nextTick(() => {
          this.$refs.dropdown.focus();
        });
      }
    },
    toggleDropdownTime() {
      this.isTimeOpen = !this.isTimeOpen;
      this.isRoomOpen = false;
      this.isDayOpen = false;
      if (this.isTimeOpen) {
        this.$nextTick(() => {
          this.$refs.dropdown.focus();
        });
      }
    },
  },
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


.custom-select {
  position: relative;
  display: flex;
  justify-content: center;
  padding: 5px 10px;
  border: 1px solid white;
  border-radius: 7px;
  cursor: pointer;
  color: white;
  font-size: 12px;
  font-weight: 700;
}

.dropdown {
  background-color: white;
  position: absolute;
  top: 100%;
  left: auto;
  right: auto;
  padding: 0px 7px;
  width: fit-content;
  border: 1px solid rgb(0, 0, 0, 0.2);
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  max-height: 80px;
  outline: none;
  overflow-y: auto;
  overflow-x: hidden;
  z-index: 1;
}

.dropdown div:not(:last-child) {
  cursor: pointer;
  padding: 7px 0px;
  border-bottom: 1px solid #ccc;
  color: rgb(0, 0, 0, 0.5);
}

.dropdown div:hover {
  color: rgb(0, 0, 0);
}

.dropdown div:last-child {
  cursor: pointer;
  padding: 7px 0px;
  color: rgb(0, 0, 0, 0.5);
}

</style>