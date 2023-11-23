<template>
    <form>
        <div>
            <p>Username <span style="color: red;">*</span></p>
            <input type="text" v-model="user.username" />
        </div>
        <div>
            <p>Email <span style="color: red;">*</span></p>
            <input type="email" v-model="user.email" />
        </div>
        <div class="password">
            <p>Password  <span style="color: red;">*</span></p>
            <input class="password-input" :type="showPassword ? 'text' : 'password'" v-model="user.password" />
            <img v-if="showPassword" @click="togglePasswordVisibility" src="../../assets/Eye.svg" alt="Hide Password" />
            <img v-else @click="togglePasswordVisibility" src="../../assets/EyeOff.svg" alt="Show Password" />
        </div>
        <div>
            <p>First name <span style="color: red;">*</span></p>
            <input type="text" v-model="user.first_name" />
        </div>
        <div>
            <p>Last name <span style="color: red;">*</span></p>
            <input type="text" v-model="user.last_name" />
        </div>
        <div>
            <p>Permission <span style="color: red;">*</span></p>
            <div class="custom-select" @click.stop="toggleDropdownPermission" :style="{'color': selectedPermission ? 'initial' : 'rgb(0,0,0,0.5)'}">
                {{ selectedPermission || 'Permission' }}
                <div v-if="isPermissionOpen" class="dropdown" ref="dropdown" @click.stop>
                <div v-for="permission in permissions" :key="permission.description" @click="selectValue(permission)">
                    {{ permission.description }}
                </div>
                </div>
            </div>
        </div>

        <div class="btns">
            <button @click.prevent="Back">Back</button>
            <button @click.prevent="CreateUser">Create</button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            user: {
                username: '',
                email: '',
                password: '',
                first_name: '',
                last_name: '',
                permission_id : null,
            },
            isPermissionOpen: false,
            selectedPermission: null,
            showPassword: false,
        }
    },
    props: {
        permissions: {
            type: Array,
            default: []
        }
    },
    methods: {
        Back() {
            this.$emit("back");
        },
        CreateUser() {
            this.$emit('create-user', this.user);
        },
        toggleDropdownPermission() {
            this.isPermissionOpen = !this.isPermissionOpen;
        },
        selectValue(permission) {
            this.selectedPermission = permission.description;
            this.isPermissionOpen = false;
            this.user.permission_id = permission.id;
        },
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
        },
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

.custom-select {
    position: relative;
    display: flex;
    border: 1px solid rgb(0, 0, 0, 0.4);
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    padding: 5px;
    font-size: 16px;
    color: rgb(0, 0, 0);
}

.dropdown {
  background-color: white;
  position: absolute;
  top: 100%;
  padding: 0px 7px;
  width: fit-content;
  border: 1px solid rgb(0, 0, 0, 0.2);
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  outline: none;
  z-index: 1;
}

.dropdown div:not(:last-child) {
  cursor: pointer;
  padding: 7px 0px;
  border-bottom: 1px solid #ccc;
  color: rgb(0, 0, 0, 0.5);
}


.dropdown div:last-child {
  cursor: pointer;
  padding: 7px 0px;
  color: rgb(0, 0, 0, 0.5);
}

.dropdown div:hover {
  color: rgb(0, 0, 0);
}


.password {
    position: relative;
}

.password-input {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 5px;
    border: 1px solid rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}

.password > img {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(20%);
}

</style>