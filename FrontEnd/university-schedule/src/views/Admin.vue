<template>
    <div class="user">
        <UserList 
            v-if="userArray.length > 0"
            :userArray="userArray"
        />
        <CreateUser
            v-if="permissions.length > 0"
            :permissions="permissions"
            @create-user="CreateUser"
        />
        <UserUpdateDelete
            v-if="Object.keys(user).length > 0 && permissions.length > 0"
            :user="user"
            :permissions="permissions"
            @update-user="UpdateUser"
            @delete-user="DeleteUser"
        />
    </div>
    <div class="subject">
        <SubjectList 
            v-if="subjectArray.length > 0"
            :subjectArray="subjectArray"
        />
        <CreateSubject
            @create-subject="CreateSubject"
        />
        <SubjectUpdateDelete
            v-if="Object.keys(user).length > 0 && permissions.length > 0"
            :subject="subject"
            @update-subject="UpdateSubject"
            @delete-subject="DeleteSubject"
        />
    </div>
</template>
  
<script>
import UserList from '../components/admin/UserList.vue';
import CreateUser from '../components/admin/CreateUser.vue';
import UserUpdateDelete from '../components/admin/UserUpdateDelete.vue';

import SubjectList from '../components/admin/SubjectList.vue';
import CreateSubject from '../components/admin/CreateSubject.vue';
import SubjectUpdateDelete from '../components/admin/SubjectUpdateDelete.vue';

import axios from 'axios';

export default {
    emits: [
        "create-user", "update-user", "delete-user",
        "create-subject", "update-subject", "delete-subject",
    ],
    data() {
        return{
            user: {},
            permissions: [],
            userArray: [],

            subjectArray: [],
            subject: {},
        }
    },
    components: {
        UserList,
        CreateUser,
        UserUpdateDelete,

        SubjectList,
        CreateSubject,
        SubjectUpdateDelete,
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/user')
        .then(response => {
            this.userArray = response.data.data;
        })
        .catch(error => {
            console.error(error);
        });

        axios.get('http://127.0.0.1:8000/api/user/5')
        .then(response => {
            this.user = response.data.data;
        })
        .catch(error => {
            console.error(error);
        });

        axios.get('http://127.0.0.1:8000/api/permission')
        .then(response => {
            this.permissions = response.data.data;
        })
        .catch(error => {
            console.error(error);
        });

        axios.get('http://127.0.0.1:8000/api/subject')
        .then(response => {
            this.subjectArray = response.data.data;
        })
        .catch(error => {
            console.error(error);
        });

        axios.get('http://127.0.0.1:8000/api/subject/1')
        .then(response => {
            this.subject = response.data.data;
        })
        .catch(error => {
            console.error(error);
        });
    },
    methods: {
        CreateUser(data) {
            axios.post(`http://127.0.0.1:8000/api/user`, data)
            .then(response => {
                console.log("Create user success!");
            })
            .catch(error => {
                console.error(error);
            });
        },
        UpdateUser(data) {
            const id = data["id"];
            delete data["id"];
            axios.put(`http://127.0.0.1:8000/api/user/${id}`, data)
            .then(response => {
                console.log("Update user success!");
            })
            .catch(error => {
                console.error(error);
            });
        },
        DeleteUser(id) {
            axios.delete(`http://127.0.0.1:8000/api/user/${id}`)
            .then(response => {
                console.log("Delete user success!");
            })
            .catch(error => {
                console.error(error);
            });
        },
        CreateSubject() {

        },
        UpdateSubject() {

        },
        DeleteSubject() {

        },
    }
};
</script>

<style scoped>

.user {
    display: flex;
    gap: 30px;
}

.subject {
    display: flex;
    gap: 30px;
}

</style>

