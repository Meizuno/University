<template>
    <form>
        <div>
            <p>Code</p>
            <input type="text" v-model="subject.code" />
        </div>
        <div>
            <p>Name</p>
            <input type="email" v-model="subject.name" />
        </div>
        <div>
            <p>Description</p>
            <input type="text" v-model="subject.description" />
        </div>

        <div class="btns">
            <button @click.prevent="Back">Back</button>
            <button @click.prevent="UpdateSubject">Update</button>
            <button @click.prevent="DeleteSubject">Delete</button>
        </div>
    </form>
</template>

<script>
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    props: {
        subject: {
            type: Object,
            default: {}
        },
    },
    methods: {
        Back() {
            this.$emit("back");
        },
        UpdateSubject() {
            if (this.subject.code.length !== 3){
                toast.error("Code has 3 chars.", {
                    autoClose: 3000,
                    position: toast.POSITION.BOTTOM_LEFT,
                });
            }
            else{
                const id = this.subject["id"];
                delete this.subject["id"];
                delete this.subject["guarantor"];
                this.$emit('update-subject', id, this.subject);
            }
        },
        DeleteSubject() {
            this.$emit('delete-subject', this.subject["id"]);
        },
        selectValue(guarantor) {
            this.selectedGuarantor = guarantor.username;
            this.selectedGuarantorID = guarantor.id;
            this.isGuarantorOpen = false;
        }
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

</style>