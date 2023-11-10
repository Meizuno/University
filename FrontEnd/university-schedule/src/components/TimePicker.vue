<template>
    <div class="custom-select" ref="customSelect" @click="handleCustomSelectClick">
      {{ selectedOption || 'Time' }}
      <div v-if="isDropdownOpen" class="dropdown" ref="dropdown" @click.stop>
        <div v-for="time in times" :key="time" @click="selectOption(time)">
          {{ time }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isDropdownOpen: false,
        selectedOption: null,
        times: ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],
      };
    },
    created() {
      window.addEventListener('click', this.handleClickOutside);
    },
    methods: {
      toggleDropdown() {
        this.isDropdownOpen = !this.isDropdownOpen;
        if (this.isDropdownOpen) {
          this.$nextTick(() => {
            this.$refs.dropdown.focus();
          });
        }
      },
      selectOption(option) {
        this.selectedOption = option;
        this.isDropdownOpen = false;
      },
      handleClickOutside(event) {
        const customSelect = this.$refs.customSelect;
        if (customSelect && !customSelect.contains(event.target)) {
          this.isDropdownOpen = false;
        }
      },
      handleCustomSelectClick() {
        this.toggleDropdown();
      },
    },
  };
  </script>
  
  <style scoped>
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
    overflow-y: auto;
    overflow-x: hidden;
    outline: none;
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
  