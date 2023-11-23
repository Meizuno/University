<template>
    <form>
        <div>
            <p>Code <span style="color: red;">*</span></p>
            <input type="text" v-model="subject.code" />
        </div>
        <div>
            <p>Name <span style="color: red;">*</span></p>
            <input type="email" v-model="subject.name" />
        </div>
        <div>
            <p>Description <span style="color: red;">*</span></p>
            <input type="text" v-model="subject.description" />
        </div>
        <div>
            <p>Guarantor <span style="color: red;">*</span></p>
            <div class="custom-select" @click.stop="toggleDropdownGuarantor" :style="{'color': selectedGuarantor ? 'initial' : 'rgb(0,0,0,0.5)'}">
                {{ selectedGuarantor || 'Guarantor' }}
                <div v-if="isGuarantorOpen" class="dropdown" ref="dropdown" @click.stop>
                <div v-for="guarantor in guarantors" :key="guarantor.id" @click="selectValue(guarantor)">
                    {{ guarantor.username }}
                </div>
                </div>
            </div>
        </div>

        <div class="btns">
            <button @click.prevent="Back">Back</button>
            <button @click.prevent="CreateSubject">Create</button>
        </div>
    </form>
</template>

<script>
export default {
    props: {
        guarantors: {
            type: Array,
            default: [],
        },
    },

    data() {
        return {
            subject: {
                code: '',
                name: '',
                description: '',
                guarantor_id: null,
            },
            isGuarantorOpen: false,
            selectedGuarantor: null,
            selectedGuarantorID: null,
        }
    },

    methods: {
        Back() {
            this.$emit('back');
        },
        CreateSubject() {
            this.subject.guarantor_id = this.selectedGuarantorID;
            this.$emit('create-subject', this.subject);
        },
        toggleDropdownGuarantor() {
            this.isGuarantorOpen = !this.isGuarantorOpen;
        },
        selectValue(guarantor) {
            this.selectedGuarantor = guarantor.username;
            this.selectedGuarantorID = guarantor.id;
            this.isGuarantorOpen = false;
        }
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

</style>