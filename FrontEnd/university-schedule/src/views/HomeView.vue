<!--@authors-->
<!--xklima34, Aliaksei Klimau-->
<!--@file HomeView.vue-->
<!--@brief Instructor registered activites schedule view-->

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

// Buttons for navigation bar
const navigationButtons = [
  { text: 'Home', class: 'selected' },
];
</script>
