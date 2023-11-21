<template>
    <div class="list">
        <div v-for="room in roomArray" @click="EditRoom(room)">{{ room.number }}</div>
        <div @click="CreateRoom">New Room</div>
    </div>
</template>


<script>

export default {
    props: {
        roomArray: {
            type: Array,
            default: [],
        },
    },
    methods: {
        CreateRoom() {
            this.$emit("new-room");
        },
        EditRoom(room){
            this.$emit("edit-room", room);
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