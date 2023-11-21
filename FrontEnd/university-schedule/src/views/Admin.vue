<template>
    <header>
        <Navigation :buttons="navigationButtons" :username="username" :status="status" />
    </header>

    <main>
        <div class="admin">
            <div>
                <h2>User</h2>
                <UserList 
                    v-if="userArray.length > 0 && isUserListOpen"
                    :userArray="userArray"
                    @new-user="NewUser"
                    @edit-user="EditUser"
                />
                <CreateUser
                    v-if="permissions.length > 0 && isCerateUserOpen"
                    :permissions="permissions"
                    @back="Back"
                    @create-user="CreateUser"
                />
                <UserUpdateDelete
                    v-if="Object.keys(user).length > 0 && permissions.length > 0 && isUpdateDeleteUserOpen"
                    :user="user"
                    :permissions="permissions"
                    @back="Back"
                    @update-user="UpdateUser"
                    @delete-user="DeleteUser"
                />
            </div>
            <div>
                <SubjectList 
                    v-if="subjectArray.length > 0"
                    :subjectArray="subjectArray"
                />
                <CreateSubject
                />
                <SubjectUpdateDelete
                    v-if="Object.keys(user).length > 0 && permissions.length > 0"
                    :subject="subject"
                />
            </div>
        </div>
    </main>
</template>
  
<script>
import Navigation from '../components/Navigation.vue';

import UserList from '../components/admin/UserList.vue';
import CreateUser from '../components/admin/CreateUser.vue';
import UserUpdateDelete from '../components/admin/UserUpdateDelete.vue';

import SubjectList from '../components/admin/SubjectList.vue';
import CreateSubject from '../components/admin/CreateSubject.vue';
import SubjectUpdateDelete from '../components/admin/SubjectUpdateDelete.vue';

import axios from 'axios';

export default {
    emits: [
        "new-user", "edit-user", "back", "create-user", "update-user", "delete-user"
    ],
    data() {
        return{
            navigationButtons: [
                { text: 'Home', class: 'not-selected',  route: '/' },
                { text: 'Administration', class: 'selected' }
            ],
            username: 'USERNAME',
            status : 'Admin',

            user: {},
            permissions: [],
            userArray: [],
            isUserListOpen: true,
            isCerateUserOpen: false,
            isUpdateDeleteUserOpen: false,

            subjectArray: [],
            subject: {},
        }
    },
    components: {
        Navigation,

        UserList,
        CreateUser,
        UserUpdateDelete,

        SubjectList,
        CreateSubject,
        SubjectUpdateDelete,
    },
    mounted() {
        this.GetUserList();

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
        GetUserList(){
            axios.get('http://127.0.0.1:8000/api/user')
            .then(response => {
                this.userArray = response.data.data;
            })
            .catch(error => {
                console.error(error);
            });
        },
        Back() {
            this.isUserListOpen = true;
            this.isCerateUserOpen = false;
            this.isUpdateDeleteUserOpen = false;
        },
        NewUser() {
            this.isUserListOpen = false;
            this.isCerateUserOpen = true;
            this.isUpdateDeleteUserOpen = false;
        },
        CreateUser(user) {
            axios.post(`http://127.0.0.1:8000/api/user`, user)
            .then(response => {
                this.GetUserList();
            })
            .catch(error => {
                console.error(error);
            });
        },
        EditUser(user){
            this.user = user;
            this.isUserListOpen = false;
            this.isCerateUserOpen = false;
            this.isUpdateDeleteUserOpen = true;
        },
        UpdateUser(id, user){
            axios.put(`http://127.0.0.1:8000/api/user/${id}`, user)
            .then(response => {
                this.GetUserList();
                this.isUserListOpen = true;
                this.isCerateUserOpen = false;
                this.isUpdateDeleteUserOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        DeleteUser(id){
            axios.delete(`http://127.0.0.1:8000/api/user/${id}`)
            .then(response => {
                this.GetUserList();
                this.isUserListOpen = true;
                this.isCerateUserOpen = false;
                this.isUpdateDeleteUserOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        }
    }
};
</script>

<style scoped>

.admin {
    margin: 20px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.admin > div {
    background-color: white;
    padding: 20px;
    border-radius: 20px;

}

h2 {
    text-align: center;
}

</style>

