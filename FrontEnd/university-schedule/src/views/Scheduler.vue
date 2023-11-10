<template>
    <header>
        <Navigation :buttons="navigationButtons" :username="username" :status="status" />
    </header>

    <main>
        <div class="not-resolved-list">
            <!-- <NotResolvedCell /> -->
            <NotResolvedCell :type="'Practice'"/>
        </div>
    </main>
</template>


<script>
import Navigation from '../components/Navigation.vue'
import ScheduleCell from '../components/ScheduleCell.vue'
import NotResolvedCell from '../components/NotResolvedCell.vue'

export default {
    components: {
    Navigation,
    NotResolvedCell,
    ScheduleCell
  },
  data() {
    return {
        navigationButtons: [
            { text: 'Home', class: 'not-selected',  route: '/' },
            { text: 'Schedule', class: 'selected' }
        ],
        username: 'USERNAME',
        status : 'Scheduler'
    };
  },
};

</script>