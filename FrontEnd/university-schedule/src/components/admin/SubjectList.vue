<template>
    <div class="list">
        <div v-for="subject in subjectArray" @click="EditSubject(subject)">{{ subject.code }}</div>
        <div @click="CreateSubject">New Subject</div>
    </div>
</template>


<script>

export default {
    props: {
        subjectArray: {
            type: Array,
            default: [],
        },
    },
    methods: {
        CreateSubject() {
            this.$emit("new-subject");
        },
        EditSubject(subject){
            this.$emit("edit-subject", subject);
        }
    }
}

</script>


<style scoped>
.list {
    display: flex;
    flex-direction: column;
}

.list {
    display: flex;
    flex-direction: column;
}

.list > div {
    border: 1px solid rgb(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 10px;
    margin: 5px 10px;
}

.list > div:last-child {
    font-weight: 600;
}

.list > div:hover {
    cursor: pointer;
    background-color: rgb(0, 0, 0, 0.05);
}

</style>