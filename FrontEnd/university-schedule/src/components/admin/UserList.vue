<template>
    <div class="list">
        <div v-for="(user, index) in paginatedUserArray" :key="index" @click="EditUser(user)">
            <p>{{user.first_name }} {{user.last_name }} ({{ user.username }})</p>
            <img src="../../assets/edit-item.svg" alt="">
        </div>
    </div>
    <div v-if="totalPages > 1" class="pagination">
        <button @click="prevPage">
            <img src="../../assets/prev-page.svg" alt="">
        </button>
        <span>Page {{ currentPage }}</span>
        <button @click="nextPage">
            <img src="../../assets/next-page.svg" alt="">
        </button>
    </div>
</template>


<script>

export default {
    data() {
        return {
            currentPage: 1,
            itemsPerPage: 5,
            totalPages: null,
        };
    },
    props: {
        userArray: {
            type: Array,
            default: [],
        }
    },
    mounted() {
        this.totalPages = Math.ceil(this.userArray.length / this.itemsPerPage);
    },
    computed: {
        paginatedUserArray() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            return this.userArray.slice(startIndex, endIndex);
        },
    },
    methods: {
        EditUser(user){
            this.$emit("edit-user", user);
        },  
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage += 1;
            }
        },

        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage -= 1;
            }
        },
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
    display: flex;
    justify-content: space-between;
}

p {
    margin: 0;
}

.list > div:hover {
    cursor: pointer;
    background-color: rgb(0, 0, 0, 0.05);
}

img {
    width: 20px;
    height: 20px;
}

.pagination {
    border: 1px solid rgb(0, 0, 0, 0.2);
    border-radius: 20px;
    margin: 5px auto;
    width: fit-content;
    display: flex;
    gap: 15px;
    align-items: center;
    overflow: hidden;
}

.pagination > button {
    border: none;
    background-color: white;
    padding: 10px;
}

.pagination > button:hover{
    background-color: rgb(0,0,0, 0.05);
}

.pagination > button > img {
    width: 15px;
    height: 15px;
}

</style>