<template>
    <form>
        <div>
            <p>Username:</p>
            <input type="text" v-model="user.username" />
        </div>
        <div>
            <p>Email:</p>
            <input type="email" v-model="user.email" />
        </div>
        <div>
            <p>Password:</p>
            <div class="password-input">
                <input :type="showPassword ? 'text' : 'password'" v-model="user.password" />
                <img v-if="showPassword" @click="togglePasswordVisibility" src="../../assets/Eye.svg" alt="Hide Password" />
                <img v-else @click="togglePasswordVisibility" src="../../assets/EyeOff.svg" alt="Show Password" />
            </div>
        </div>
        <div>
            <p>First name:</p>
            <input type="text" v-model="user.first_name" />
        </div>
        <div>
            <p>Last name:</p>
            <input type="text" v-model="user.last_name" />
        </div>
        <div>
            <p>Permission:</p>
            <div class="custom-select" @click.stop="toggleDropdownPermission">
                {{ selectedPermission }}
                <div v-if="isPermissionOpen" class="dropdown" ref="dropdown" @click.stop>
                <div v-for="permission in permissions" :key="permission.description" @click="selectValue(permission)">
                    {{ permission.description }}
                </div>
                </div>
            </div>
        </div>

        <div class="btns">
            <button @click.prevent="Back">Back</button>
            <button @click.prevent="UpdateUser">Update</button>
            <button @click.prevent="DeleteUser">Delete</button>
        </div>
    </form>
</template>

<script>

export default {
    props: {
        user: {
            type: Object,
            default: {}
        },
        permissions: {
            type: Array,
            default: []
        }
    },
    data() {
        return {
            isPermissionOpen: false,
            selectedPermission: this.user.permission.description,
            showPassword: false,
        }
    },
    methods: {
        Back() {
            this.$emit("back");
        },
        UpdateUser() {
            const id = this.user["id"];
            const permission = this.permissions.find(p => p.description === this.selectedPermission);
            this.user["permission_id"] = permission.id;
            delete this.user["permission"];
            delete this.user["id"];
            this.$emit('update-user', id, this.user);
        },
        DeleteUser() {
            this.$emit('delete-user', this.user["id"]);
        },
        toggleDropdownPermission() {
            this.isPermissionOpen = !this.isPermissionOpen;
        },
        selectValue(permission) {
            this.selectedPermission = permission.description;
            this.isPermissionOpen = false;
        },
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
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

.dropdown div:hover {
  color: rgb(0, 0, 0);
}

.dropdown div:last-child {
  cursor: pointer;
  padding: 7px 0px;
  color: rgb(0, 0, 0, 0.5);
}

.password-input {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 5px;
    border: 1px solid rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}

.password-input > input {
    border: none;
    font-size: 16px;
    outline: none;
}

</style>