<template>
    <header>
        <Navigation />
    </header>

    <main>
        <div class="admin">
            <div>
                <h2>User</h2>
                <UserList 
                    v-if="isUserLoad && isUserListOpen"
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
                    v-if="isUserLoad && permissions.length > 0 && isUpdateDeleteUserOpen"
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
                    v-if="isSubjectLoad && isSubjectListOpen"
                    :subjectArray="subjectArray"
                    @new-subject="NewSubject"
                    @edit-subject="EditSubject"
                />
                <CreateSubject
                    v-if="isCerateSubjectOpen"
                    :guarantors="guarantors"
                    @back="SubjectBack"
                    @create-subject="CreateSubject"
                />
                <SubjectUpdateDelete
                    v-if="isSubjectLoad && isUpdateDeleteSubjectOpen"
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
                    v-if="isRoomLoad && isRoomListOpen"
                    :roomArray="roomArray"
                    @new-room="NewRoom"
                    @edit-room="EditRoom"
                />
                <CreateRoom
                    v-if="isCerateRoomOpen"
                    @back="RoomBack"
                    @create-room="CreateRoom"
                />
                <RoomUpdateDelete
                    v-if="isRoomLoad && isUpdateDeleteRoomOpen"
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
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    emits: [
        "new-user", "edit-user", "back", "create-user", "update-user", "delete-user",
        "new-subject", "edit-subject", "create-subject", "update-subject", "delete-subject",
        "new-room", "edit-room", "create-room", "update-room", "delete-room"
    ],
    data() {
        return{
            header: {
                "Authorization": localStorage.getItem("token"),
            },

            user: {},
            permissions: [],
            userArray: [],
            guarantors: [],

            isUserListOpen: true,
            isCerateUserOpen: false,
            isUpdateDeleteUserOpen: false,
            isUserLoad: false,

            subjectArray: [],
            subject: {},

            isSubjectListOpen: true,
            isCerateSubjectOpen: false,
            isUpdateDeleteSubjectOpen: false,
            isSubjectLoad: false,

            roomArray: [],
            room: {},

            isRoomListOpen: true,
            isCerateRoomOpen: false,
            isUpdateDeleteRoomOpen: false,
            isRoomLoad: false,
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

        axios.get(`${import.meta.env.VITE_API_HOST}/permission`, {headers: this.header})
        .then(response => {
            this.permissions = response.data.data;
        })
        .catch(error => {
            for (const key in error.response.data.errors) {
                if (error.response.data.errors.hasOwnProperty(key)) {
                    const errorDes = error.response.data.errors[key];
                    const errorMessage = `${key}: ${errorDes}`;
    
                    toast.error(errorMessage, {
                        autoClose: 5000,
                        position: toast.POSITION.BOTTOM_LEFT,
                        hideProgressBar: true,
                    });
                }
            }
        });

        this.GetSubjectList();
        this.GetRoomList();
    },
    methods: {
        GetUserList(){
            axios.get(`${import.meta.env.VITE_API_HOST}/user`, {headers: this.header})
            .then(response => {
                this.userArray = response.data.data;
                this.userArray.sort((a, b) => {
                    const nameA = a.first_name.toUpperCase();
                    const nameB = b.first_name.toUpperCase();

                    if (nameA < nameB) {
                    return -1;
                    }

                    if (nameA > nameB) {
                    return 1;
                    }

                    return 0;
                });
                this.guarantors = this.userArray.filter(user => user.permission.level === 2);
                this.isUserLoad = true;
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
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
            axios.post(`${import.meta.env.VITE_API_HOST}/user`, user, {headers: this.header})
            .then(response => {
                this.GetUserList();
                this.isUserListOpen = true;
                this.isCerateUserOpen = false;
                this.isUpdateDeleteUserOpen = false;
                toast.success("Create user is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_RIGHT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_RIGHT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        EditUser(user){
            this.user = user;
            this.isUserListOpen = false;
            this.isCerateUserOpen = false;
            this.isUpdateDeleteUserOpen = true;
        },
        UpdateUser(id, user){
            axios.put(`${import.meta.env.VITE_API_HOST}/user/${id}`, user, {headers: this.header})
            .then(response => {
                this.GetUserList();
                this.isUserListOpen = true;
                this.isCerateUserOpen = false;
                this.isUpdateDeleteUserOpen = false;
                toast.success("Update user is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_RIGHT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_RIGHT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        DeleteUser(id){
            axios.delete(`${import.meta.env.VITE_API_HOST}/user/${id}`, {headers: this.header})
            .then(response => {
                this.GetUserList();
                this.isUserListOpen = true;
                this.isCerateUserOpen = false;
                this.isUpdateDeleteUserOpen = false;
                toast.success("Delete user is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_RIGHT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_RIGHT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },

        GetSubjectList() {
            axios.get(`${import.meta.env.VITE_API_HOST}/subject`, {headers: this.header})
            .then(response => {
                this.subjectArray = response.data.data;
                this.subjectArray.sort((a, b) => {
                    const nameA = a.code.toUpperCase();
                    const nameB = b.code.toUpperCase();

                    if (nameA < nameB) {
                    return -1;
                    }

                    if (nameA > nameB) {
                    return 1;
                    }

                    return 0;
                });
                this.isSubjectLoad = true;
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
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
            axios.post(`${import.meta.env.VITE_API_HOST}/subject`, subject, {headers: this.header})
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
                toast.success("Create subject is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        EditSubject(subject) {
            this.subject = subject;
            this.isSubjectListOpen = false;
            this.isCerateSubjectOpen = false;
            this.isUpdateDeleteSubjectOpen = true;
        },
        UpdateSubject(id, subject) {
            axios.put(`${import.meta.env.VITE_API_HOST}/subject/${id}`, subject, {headers: this.header})
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
                toast.success("Update subject is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        DeleteSubject(id){
            axios.delete(`${import.meta.env.VITE_API_HOST}/subject/${id}`, {headers: this.header})
            .then(response => {
                this.GetSubjectList();
                this.isSubjectListOpen = true;
                this.isCerateSubjectOpen = false;
                this.isUpdateDeleteSubjectOpen = false;
                toast.success("Delete subject is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },

        GetRoomList() {
            axios.get(`${import.meta.env.VITE_API_HOST}/room`, {headers: this.header})
            .then(response => {
                this.roomArray = response.data.data;
                this.roomArray.sort((a, b) => a.number - b.number);
                this.isRoomLoad = true;
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
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
            axios.post(`${import.meta.env.VITE_API_HOST}/room`, room, {headers: this.header})
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
                toast.success("Create room is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        EditRoom(room) {
            this.room = room;
            this.isRoomListOpen = false;
            this.isCerateRoomOpen = false;
            this.isUpdateDeleteRoomOpen = true;
        },
        UpdateRoom(id, room) {
            axios.put(`${import.meta.env.VITE_API_HOST}/room/${id}`, room, {headers: this.header})
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
                toast.success("Update room is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
        DeleteRoom(id){
            axios.delete(`${import.meta.env.VITE_API_HOST}/room/${id}`, {headers: this.header})
            .then(response => {
                this.GetRoomList();
                this.isRoomListOpen = true;
                this.isCerateRoomOpen = false;
                this.isUpdateDeleteRoomOpen = false;
                toast.success("Delete room is success!", {
                    autoClose: 5000,
                    position: toast.POSITION.BOTTOM_LEFT,
                    hideProgressBar: true,
                });
            })
            .catch(error => {
                for (const key in error.response.data.errors) {
                    if (error.response.data.errors.hasOwnProperty(key)) {
                        const errorDes = error.response.data.errors[key];
                        const errorMessage = `${key}: ${errorDes}`;
        
                        toast.error(errorMessage, {
                            autoClose: 5000,
                            position: toast.POSITION.BOTTOM_LEFT,
                            hideProgressBar: true,
                        });
                    }
                }
            });
        },
    }
};
</script>

<style scoped>

template {
    max-height: 100%;
}

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
    margin: 10px;
}

</style>

