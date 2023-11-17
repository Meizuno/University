<template>
    <div class="list">
        <p v-for="subject in subjectArray">{{ subject.code }}</p>
    </div>
</template>


<script>

export default {
    props: {
        subjectArray: {
            type: Array,
            default: [],
        }
    }
}

</script>


<style scoped>
.list {
    display: flex;
    flex-direction: column;
}

</style>