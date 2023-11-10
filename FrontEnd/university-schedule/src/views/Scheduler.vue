<script setup>
import ScheduleCell from '../components/ScheduleCell.vue'
import RoomPicker from '../components/RoomPicker.vue'
import DayPicker from '../components/DayPicker.vue'
import TimePicker from '../components/TimePicker.vue'
</script>

<template>
    <ScheduleCell type="Lecture"/>
    <ScheduleCell type="Practice"/>
    <ScheduleCell type="Laboratory"/>
    <ScheduleCell type="Exam"/>

    <RoomPicker width="100px"/>
    <DayPicker width="50px"/>
    <TimePicker width="50px"/>
</template>