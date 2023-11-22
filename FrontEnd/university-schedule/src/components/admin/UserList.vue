<template>
    <div class="list">
        <div v-for="user in userArray" @click="EditUser(user)">{{user.first_name }} {{user.last_name }} ({{ user.username }})</div>
        <div @click="CreateUser">New User</div>
    </div>
</template>


<script>

export default {
    props: {
        userArray: {
            type: Array,
            default: [],
        }
    },
    methods: {
        CreateUser() {
            this.$emit("new-user");
        },
        EditUser(user){
            this.$emit("edit-user", user);
        }
    }
}

</script>


<style scoped>
.list {
    display: flex;
    flex-direction: column;
    max-height: 470px;
    overflow: auto;
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