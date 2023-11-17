<template>
    <div class="list">
        <p v-for="user in userArray">{{ user.username }}</p>
    </div>
</template>


<script>

export default {
    props: {
        userArray: {
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