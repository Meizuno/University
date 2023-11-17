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

        <button @click.prevent="UpdateSubject">Update</button>
        <button @click.prevent="DeleteSubject">Delete</button>
    </form>
</template>

<script>

export default {
    props: {
        subject: {
            type: Object,
            default: {}
        },
    },
    methods: {
        UpdateSubject() {
            this.$emit('update-subject', this.subject);
        },
        DeleteSSubject() {
            this.$emit('delete-subject', this.subject["id"]);
        }
    }
};

</script>