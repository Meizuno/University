<template>
    <div class="subject-main">
        <div v-for="subject in subjects" class="subject-card">
            <div class="subject-title">
                <p>{{ subject.code }}</p>
                <p>{{ subject.name }}</p>
            </div>
            <div class="subject-guarantor">
                <p>{{ subject.guarantor.first_name + " " + subject.guarantor.last_name}}</p>
            </div>
            <div class="subject-time-span">
                <p>Time span:</p>
                <ul>
                    <li>13 lectures</li>
                    <li>6 practices</li>
                </ul>
            </div>
            <div class="subject-description">
                <p>{{ subject.description }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      subjects: []
    };
  },
  mounted() {
    console.log();
    axios.get(`${import.meta.env.VITE_API_HOST}/subject`)
        .then(response => {
            this.subjects = response.data.data;
        })
        .catch(error => {
            console.error('Error response: ', error);
        });
  }
};
</script>

<style scoped>

.subject-main {
    padding: 0px 30px;
    height: auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.subject-card {
    margin: 20px 0px;
    height: auto;
    width: calc(50% - 100px);
    background-color: white;
    padding: 20px 40px;
    border-radius: 20px;
}

.subject-title {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    font-size: 28px;
}

.subject-title > p {
    margin: 5px 0px;
}

.subject-guarantor {
    text-decoration: underline;
    font-weight: bold;
    font-size: 24px;
    color: rgba(0, 0, 0, 0.6);
}

.subject-guarantor > p {
    margin: 5px 0px;
}

.subject-guarantor p:hover {
    cursor: pointer;
    color: rgba(0, 0, 0);
}

.subject-time-span > * {
    margin: 10px 0px;
    font-weight: bold;
    font-size: 20px;
    color: rgba(0, 0, 0, 0.5);
}

.subject-description > p {
    font-size: 18px;
    color: rgba(0, 0, 0, 0.5);
}

</style>