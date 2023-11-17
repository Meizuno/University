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
        <!-- <div>
            <p>Guarantor</p>
            <input type="text" v-model="subject.permission.description" />
        </div> -->

        <button @click.prevent="CreateSubject">Create</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            subject: {
                code: '',
                name: '',
                description: '',
                guarantor: {
                    id: ''
                }
            }
        }
    },
    methods: {
        CreateSubject() {
            this.$emit('create-subject', this.subject);
        }
    }
}

</script>