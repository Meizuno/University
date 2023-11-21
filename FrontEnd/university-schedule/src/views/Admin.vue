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
                    @back="UserBack"
                    @create-user="CreateUser"
                />
                <UserUpdateDelete
                    v-if="Object.keys(user).length > 0 && permissions.length > 0 && isUpdateDeleteUserOpen"
                    :user="user"
                    :permissions="permissions"
                    @back="UserBack"
                    @update-user="UpdateUser"
                    @delete-user="DeleteUser"
                />
            </div>
            <div>
                <h2>Subject</h2>
                <SubjectList 
                    v-if="subjectArray.length > 0 && isSubjectListOpen"
                    :subjectArray="subjectArray"
                    @new-subject="NewSubject"
                    @edit-subject="EditSubject"
                />
                <CreateSubject
                    v-if="Object.keys(subject).length > 0 && isCerateSubjectOpen"
                    :guarantors="guarantors"
                    @back="SubjectBack"
                    @create-subject="CreateSubject"
                />
                <SubjectUpdateDelete
                    v-if="Object.keys(subject).length > 0 && isUpdateDeleteSubjectOpen"
                    :subject="subject"
                    :guarantors="guarantors"
                    @back="SubjectBack"
                    @update-subject="UpdateSubject"
                    @delete-subject="DeleteSubject"
                />
            </div>
            <div>
                <h2>Room</h2>
                <RoomList 
                    v-if="roomArray.length > 0 && isRoomListOpen"
                    :roomArray="roomArray"
                    @new-room="NewRoom"
                    @edit-room="EditRoom"
                />
                <CreateRoom
                    v-if="Object.keys(room).length > 0 && isCerateRoomOpen"
                    @back="RoomBack"
                    @create-room="CreateRoom"
                />
                <RoomUpdateDelete
                    v-if="Object.keys(room).length > 0 && isUpdateDeleteRoomOpen"
                    :room="room"
                    @back="RoomBack"
                    @update-room="UpdateRoom"
                    @delete-room="DeleteRoom"
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

import RoomList from '../components/admin/RoomList.vue';
import CreateRoom from '../components/admin/CreateRoom.vue';
import RoomUpdateDelete from '../components/admin/RoomUpdateDelete.vue';

import axios from 'axios';

export default {
    emits: [
        "new-user", "edit-user", "back", "create-user", "update-user", "delete-user",
        "new-subject", "edit-subject", "create-subject", "update-subject", "delete-subject",
        "new-room", "edit-room", "create-room", "update-room", "delete-room"
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
            guarantors: [],

            isUserListOpen: true,
            isCerateUserOpen: false,
            isUpdateDeleteUserOpen: false,

            subjectArray: [],
            subject: {},

            isSubjectListOpen: true,
            isCerateSubjectOpen: false,
            isUpdateDeleteSubjectOpen: false,

            roomArray: [],
            room: {},

            isRoomListOpen: true,
            isCerateRoomOpen: false,
            isUpdateDeleteRoomOpen: false,
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

        RoomList,
        CreateRoom,
        RoomUpdateDelete
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

        this.GetSubjectList();
        this.GetRoomList();
    },
    methods: {
        GetUserList(){
            axios.get('http://127.0.0.1:8000/api/user')
            .then(response => {
                this.userArray = response.data.data;
                this.guarantors = this.userArray.filter(user => user.permission.level === 2);
            })
            .catch(error => {
                console.error(error);
            });
        },
        UserBack() {
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
        },

        GetSubjectList() {
            axios.get('http://127.0.0.1:8000/api/subject')
            .then(response => {
                this.subjectArray = response.data.data;
            })
            .catch(error => {
                console.error(error);
            });
        },
        SubjectBack() {
            this.isSubjectListOpen = true;
            this.isCerateSubjectOpen = false;
            this.isUpdateDeleteSubjectOpen = false;
        },
        NewSubject() {
            this.isSubjectListOpen = false;
            this.isCerateSubjectOpen = true;
            this.isUpdateDeleteSubjectOpen = false;
        },
        CreateSubject(subject) {
            axios.post(`http://127.0.0.1:8000/api/subject`, subject)
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        EditSubject(subject) {
            this.subject = subject;
            this.isSubjectListOpen = false;
            this.isCerateSubjectOpen = false;
            this.isUpdateDeleteSubjectOpen = true;
        },
        UpdateSubject(id, subject) {
            axios.put(`http://127.0.0.1:8000/api/subject/${id}`, subject)
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        DeleteSubject(id){
            axios.delete(`http://127.0.0.1:8000/api/subject/${id}`)
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },

        GetRoomList() {
            axios.get('http://127.0.0.1:8000/api/room')
            .then(response => {
                this.roomArray = response.data.data;
            })
            .catch(error => {
                console.error(error);
            });
        },
        RoomBack() {
            this.isRoomListOpen = true;
            this.isCerateRoomOpen = false;
            this.isUpdateDeleteRoomOpen = false;
        },
        NewRoom() {
            this.isRoomListOpen = false;
            this.isCerateRoomOpen = true;
            this.isUpdateDeleteRoomOpen = false;
        },
        CreateRoom(room) {
            axios.post(`http://127.0.0.1:8000/api/room`, room)
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        EditRoom(room) {
            this.room = room;
            this.isRoomListOpen = false;
            this.isCerateRoomOpen = false;
            this.isUpdateDeleteRoomOpen = true;
        },
        UpdateRoom(id, room) {
            axios.put(`http://127.0.0.1:8000/api/room/${id}`, room)
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        DeleteRoom(id){
            axios.delete(`http://127.0.0.1:8000/api/room/${id}`)
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
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

