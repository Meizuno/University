<template>
    <form>
        <div>
            <p>Username</p>
            <input type="text" v-model="user.username" />
        </div>
        <div>
            <p>Email</p>
            <input type="email" v-model="user.email" />
        </div>
        <div>
            <p>Password</p>
            <input type="password" v-model="user.password" />
        </div>
        <div>
            <p>First name</p>
            <input type="text" v-model="user.first_name" />
        </div>
        <div>
            <p>Last name</p>
            <input type="text" v-model="user.last_name" />
        </div>
        <div>
            <p>Permission</p>
            <input type="text" v-model="user.permission.description" />
        </div>

        <button @click.prevent="UpdateUser">Update</button>
        <button @click.prevent="DeleteUser">Delete</button>
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
    methods: {
        UpdateUser() {
            let data = Object.assign({}, this.user);
            const description = data["permission"]["description"];
            delete data["permission"];
            const foundPermission = this.permissions.find(permission => permission.description === description);
            data["permission_id"] = foundPermission.id;
            this.$emit('update-user', data);
        },
        DeleteUser() {
            this.$emit('delete-user', this.user["id"]);
        }
    }
};

</script>