<template>
    <form>
        <div>
            <p>Number:</p>
            <input type="text" v-model="room.number" />
        </div>
        <div>
            <p>Description:</p>
            <input type="email" v-model="room.description" />
        </div>

        <div class="btns">
            <button @click.prevent="Back">Back</button>
            <button @click.prevent="UpdateRoom">Update</button>
            <button @click.prevent="DeleteRoom">Delete</button>
        </div>
    </form>
</template>

<script>

export default {
    props: {
        room: {
            type: Object,
            default: {}
        },
    },
    methods: {
        Back() {
            this.$emit("back");
        },
        UpdateRoom() {
            console.log(this.room);
            const id = this.room["id"];
            delete this.room["id"];
            this.$emit('update-room', id, this.user);
        },
        DeleteRoom() {
            this.$emit('delete-room', this.room["id"]);
        },
    }
};

</script>

<style scoped>

form > div {
    border-radius: 10px;
    margin: 20px 10px;
}

form > div > p {
    margin: 10px 0px;
}

form > div > input {
    width: 100%;
    padding: 5px;
    font-size: 16px;
    border: 1px solid rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}

.btns {
    display: flex;
    justify-content: end;
    gap: 10px;
}

.btns > button {
    font-size: 18px;
    padding: 7px 20px;
    border: none;
    color: white;
    font-weight: 600;
    border-radius: 7px;
}

.btns > button:not(:last-child) {
    background-color: #00A7FF;
}

.btns > button:not(:last-child):hover {
    background-color: #45BFFF;
    cursor: pointer;
}

.btns > button:last-child {
    background-color: #FF6975;
}

.btns > button:last-child:hover {
    background-color: #FF7783;
    cursor: pointer;
}

</style>