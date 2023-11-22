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
            <button @click.prevent="CreateRoom">Create</button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            room: {
                number: '',
                description: '',
            },
        }
    },
    methods: {
        Back() {
            this.$emit("back");
        },
        CreateRoom() {
            this.room.number = parseInt(this.room.number, 10);
            this.$emit('create-room', this.room);
        }
    }
}

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

.btns > button:first-child {
    background-color: #00A7FF;
}

.btns > button:first-child:hover {
    background-color: #45BFFF;
    cursor: pointer;
}

.btns > button:last-child {
    background-color: #70C784;
}

.btns > button:last-child:hover {
    background-color: #84D296;
    cursor: pointer;
}

</style>