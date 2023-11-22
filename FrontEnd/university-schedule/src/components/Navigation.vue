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
                <button v-for="button in buttons" :key="button.text"  :class="{ 'selected': button.text === currentPage }" class="menu-item" @click="handleButtonClick(button.route)">
                    {{ button.text }}
                </button>
            </div>
            <div class="btn-login" @click="Auth">
                {{ authButton }}
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: 'Anonymous',
            status: '',
            buttons: [
                { text: 'Home', route: '/' },
            ],
            authButton: 'login',

            currentPage: '',
        }
    },
    mounted() {
        this.UpdateUserData();
        switch(this.$route.path){
            case "/admin":
                this.currentPage = "Administration";
                break;
            case "/scheduler":
                this.currentPage = "Schedule";
                break;
            case "/":
                this.currentPage = "Home";
                break;
        }
    },
    methods: {
        UpdateUserData() {
            if (localStorage.getItem("token")){
                this.username = localStorage.getItem("username");
                this.status = localStorage.getItem("status");
                this.authButton = localStorage.getItem("token") ? "logout" : "login";
            }

            switch(this.status){
                case "Admin":
                    this.buttons = [
                        { text: 'Home', route: '/' },
                        { text: 'Administration', route: '/admin' }
                    ];
                    break;
                case "Scheduler":
                    this.buttons = [
                        { text: 'Home', route: '/' },
                        { text: 'Schedule', route: '/scheduler' }
                    ];
                    break;
                default:
                    break;
            }
        },
        handleButtonClick(path) {
            if (path) {
                this.$router.push(path);
            }
        },
        Auth() {
            if (localStorage.getItem("token")){
                localStorage.clear();
                this.$router.push('/');
            }
            else{
                this.$router.push('/authorization');
            }
            
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
    border-radius: 15px;
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

.menu-item{
    color: rgba(0, 0, 0, 0.6);
    border: none;
    background-color: white;
    margin: 5%;
    font-size: 20px;
    font-weight: bold;
}

.menu-item:hover, .selected {
    text-decoration: underline;
    cursor: pointer;
    color: black;
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