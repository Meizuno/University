<template>
    <header>
        <Navigation :buttons="navigationButtons" :username="username" :status="status" />
    </header>

    <main>
        <div class="not-resolved-list">
            <NotResolvedCell v-for="(notResolvedCell, index) in notResolvedCells" :key="index" :name="notResolvedCell.name" :type="notResolvedCell.type" />
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
            notResolvedCells: []
        };
    },
    created() {
        this.notResolvedCells.push({name: "ITU", type: "Lecture"});
        this.notResolvedCells.push({name: "ITU", type: "Practice"});
        this.notResolvedCells.push({name: "ITU", type: "Laboratory"});
        this.notResolvedCells.push({name: "ITU", type: "Exam"});

        this.notResolvedCells.push({name: "IIS", type: "Lecture"});
        this.notResolvedCells.push({name: "IIS", type: "Practice"});
        this.notResolvedCells.push({name: "IIS", type: "Laboratory"});
        this.notResolvedCells.push({name: "IIS", type: "Exam"});
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