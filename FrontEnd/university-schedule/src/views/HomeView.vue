
<template>
  <header>
    <Navigation :buttons="navigationButtons"/>
  </header>
  
  <main>
    <SubjectCard/>
  </main>
</template>

<script setup>
import Navigation from '../components/Navigation.vue'
import SubjectCard from '../components/SubjectCard.vue'


const navigationButtons = [
  { text: 'Home', class: 'selected' },
];
</script>
