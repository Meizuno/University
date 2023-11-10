<script setup>
import ScheduleCell from '../components/ScheduleCell.vue'
import NotResolvedCell from '../components/NotResolvedCell.vue'
</script>

<template>
    <ScheduleCell type="Lecture"/>
    <ScheduleCell type="Practice"/>
    <ScheduleCell type="Laboratory"/>
    <ScheduleCell type="Exam"/>

    <NotResolvedCell type="Lecture"/>
    <NotResolvedCell type="Practice"/>
    <NotResolvedCell type="Laboratory"/>
    <NotResolvedCell type="Exam"/>
</template>