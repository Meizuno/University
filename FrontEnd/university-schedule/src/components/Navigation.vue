<script></script>

<template>
    <div class="header">
        <div class="user">
            <img src="../assets/avatar.svg" alt="">
            <p>Anonymous</p>
        </div>
        <nav>
            <div class="menu">
                <p>Home</p>
            </div>
            <div class="btn-login">
                Login
            </div>
        </nav>
    </div>
</template>

<style scoped>

.header {
    background-color: white;
    border-radius: 30px;
    padding: 2% 3%;
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
    font-size: 32px;
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

.menu > * {
    margin: 5%;
    font-size: 32px;
    font-weight: bold;
    text-decoration: underline;
}

.user {
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    margin-right: auto;
}

.user p {
    font-size: 32px;
    font-weight: bold;
    color: rgba(0, 0, 0, 0.7);
    margin-left: 20px;
}

.user img {
    color: rgba(0, 0, 0, 0.6);
}

</style>