<template>
    <header>
        <Navigation :buttons="navigationButtons" :username="username" :status="status" />
    </header>

    <main>
        <div class="not-resolved-list">
            <NotResolvedCell 
                v-for="activity in activitiesNotResolved" 
                :key="activity.id" 
                :activity="activity" 
                :rooms="rooms"
                @update-activity="NewActivity"
            />
        </div>
        <div>
            <ScheduleCell 
                v-for="activity in activitiesResolved"
                :key="activity.id"
                :activity="activity"
                :isScheduler="true"
                @delete-activity="NewActivity"
            />
        </div>
    </main>
</template>


<script>
import Navigation from '../components/Navigation.vue';
import ScheduleCell from '../components/ScheduleCell.vue';
import NotResolvedCell from '../components/NotResolvedCell.vue';
import axios from 'axios';

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
            status : 'Scheduler',
            activitiesNotResolved: [],
            activitiesResolved: [],
            rooms: [],
        };
    },
    methods: {
        NewActivity() {
            axios.get('http://127.0.0.1:8000/api/activity')
            .then(response => {
                let activities = response.data.data;
                this.activitiesNotResolved = [];
                this.activitiesResolved = [];
                for (const activity of activities) {
                    if (activity.date_time === null){
                        this.activitiesNotResolved.push(activity);
                    }
                    else {
                        this.activitiesResolved.push(activity);
                    }
                }
            })
            .catch(error => {
                console.error('Error response for activity: ', error);
            });
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/activity')
        .then(response => {
            let activities = response.data.data;
            for (const activity of activities) {
                if (activity.date_time === null){
                    this.activitiesNotResolved.push(activity);
                }
                else {
                    this.activitiesResolved.push(activity);
                }
            }
        })
        .catch(error => {
            console.error('Error response for activity: ', error);
        });

        axios.get('http://127.0.0.1:8000/api/room')
        .then(response => {
            this.rooms = response.data.data;
        })
        .catch(error => {
            console.error('Error response for rooms: ', error);
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