<template>
    <div class="header">
        <div class="user">
            <img src="../assets/avatar.svg" alt="">
            <div>
                <p class="username">{{ username }}</p>
                <p class="status">{{ status }}</p>
            </div>
        </div>
        <nav>
            <div class="menu">
                <button v-for="button in buttons" :key="button.text" :class=button.class>
                    {{ button.text }}
                </button>
            </div>
            <div class="btn-login" @click="Authorization">
                Login
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    props: {
        buttons: {
            type: Array,
            default: () => []
        },
        username: {
            type: String,
            default: 'Anonymous'
        },
        status: {
            type: String,
            default: ''
        }
    },
    methods: {
        Authorization() {
            this.$router.push('/authorization');
        },
        ToHome() {
            this.$router.push('/');
        }
    }
};
</script>

<style scoped>

.header {
    margin: 20px;
    background-color: white;
    border-radius: 30px;
    padding: 10px 40px;
    display: flex;
    flex-wrap: nowrap;
}

.header nav {
    display: flex;
    flex-wrap: nowrap;
    margin-left: auto;
    align-items: center;
}
.btn-login {
    background: rgba(0, 0, 0, 0.7);
    padding: 10px 20px;
    border-radius: 20px;
    color: rgba(255,255,255,1);
    font-size: 20px;
    text-transform: uppercase;
}

.btn-login:hover {
    background: rgba(0, 0, 0, 0.6);
    cursor: pointer;
}

.menu {
    display: flex;
    flex-wrap: nowrap;
    position: relative;
    right: 30%;
}

.selected {
    text-decoration: underline;
    color: black;
}


button {
    border: none;
    background-color: white;
    margin: 5%;
    font-size: 20px;
    font-weight: bold;
    color: rgba(0, 0, 0, 0.6);
}


.user {
    display: flex;
    gap: 20px;
    flex-wrap: nowrap;
    align-items: center;
    margin-right: auto;
}

.user img {
    color: rgba(0, 0, 0, 0.6);
    height: 50px;
    width: 50px;
}

.username {
    margin: 0px;
    font-size: 20px;
    font-weight: bold;
    color: rgba(0, 0, 0, 0.7);
}

.status {
    margin: 0px;
    font-size: 14px;
    font-weight: bold;
    color: rgba(0, 0, 0, 0.4);
}

</style>