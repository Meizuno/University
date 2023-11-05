<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue'
import SubjectCard from './components/SubjectCard.vue'
</script>

<template>
  <header>
      <Navigation />
  </header>

  <main>
    <SubjectCard />
  </main>

  <RouterView />
</template>

<style scoped>

</style>
