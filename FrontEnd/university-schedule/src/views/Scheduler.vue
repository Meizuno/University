<template>
    <header>
        <Navigation :buttons="navigationButtons" :username="username" :status="status" />
    </header>

    <main>
        <div class="not-resolved-list">
            <NotResolvedCell v-for="(activityNotResolved, index) in activitiesNotResolved" :key="index" :code="activityNotResolved.code" :type="activityNotResolved.type" />
        </div>
    </main>
</template>


<script>
import Navigation from '../components/Navigation.vue'
import ScheduleCell from '../components/ScheduleCell.vue'
import NotResolvedCell from '../components/NotResolvedCell.vue'
import axios from 'axios';

export default {
    components: {
        Navigation,
        NotResolvedCell
    },
    data() {
        return {
            navigationButtons: [
                { text: 'Home', class: 'not-selected',  route: '/' },
                { text: 'Schedule', class: 'selected' }
            ],
            username: 'USERNAME',
            status : 'Scheduler',
            activitiesNotResolved: []
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/activity')
        .then(response => {
            this.activities = response.data.data;
            for (const activity of this.activities) {
                this.activitiesNotResolved.push({code: activity.subject.code, type: activity.activity_type.description});
            }
            console.log(this.activitiesNotResolved);
        })
        .catch(error => {
            console.error('Error response: ', error);
        });
    }
};

</script>

<style scoped>

.not-resolved-list {
    margin: 20px;
    background-color: white;
    border-radius: 15px 15px 0px 0px;
    padding: 20px;
    display: flex;
    gap: 20px;
    overflow-y: hidden;
    overflow-x: auto;
}

</style>