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
                @add-to-calendar="HandleAddToCalendar"
            />
        </div>

        <Calendar
            ref="calendarRef"
            v-if="dataForCalendarReceived"
            :activities="activitiesResolved"
            :is-scheduler="true"
            @remove-from-calendar="HandleRemoveFromCalendar"
        />
    </main>
</template>


<script>
import Navigation from '../components/Navigation.vue';
import ScheduleCell from '../components/ScheduleCell.vue';
import NotResolvedCell from '../components/NotResolvedCell.vue';
import Calendar from '../components/Calendar.vue';
import axios from 'axios';

export default {
    emits: ["remove-from-calendar", "add-to-calendar", "add-to-calendar"],
    components: {
        Navigation,
        NotResolvedCell,
        ScheduleCell,
        Calendar
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

            dataForCalendarReceived: false,
        };
    },
    methods: {
        GetActivities() {
            this.dataForCalendarReceived = false;
            axios.get('http://127.0.0.1:8000/api/activity')
            .then(response => {
                let activities = response.data.data;
                this.activitiesNotResolved = [];
                this.activitiesResolved = [];
                for (const activity of activities) {
                    if (activity.time === null){
                        this.activitiesNotResolved.push(activity);
                    }
                    else {
                        this.activitiesResolved.push(activity);
                    }
                }
                this.dataForCalendarReceived = true;
            })
            .catch(error => {
                console.error('Error response for activity: ', error);
            });
        },
        HandleRemoveFromCalendar(activity) {
            axios.delete(`http://127.0.0.1:8000/api/scheduler-activity/${activity.id}`)
            .then(response => {
                this.GetActivities();
                this.$refs.calendarRef.UpdateCalendar();
            })
            .catch(error => {
                console.error(error);
            });
        },
        HandleAddToCalendar(activity, data) {
            axios.post(`http://127.0.0.1:8000/api/scheduler-activity/${activity.id}`, data)
            .then(response => {
                this.GetActivities();
                this.$refs.calendarRef.UpdateCalendar();
            })
            .catch(error => {
                console.error(error);
            });
        }
    },
    mounted() {
        this.GetActivities();

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
    position: relative;
    margin: 20px;
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

</style>