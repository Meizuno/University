<template>
  <navigation
      class="nav-bar"
      :username="'test username'"
      :status="'guarantor'"
      :buttons="buttons"
  >
  </navigation>
  <div class="main-container">
    <div class="request-container">
      <div class="title">
        <div class="title__body">Unresolved requests</div>
      </div>
      <div class="list__request">
        <div class="list_body">
          <guarant-request
              v-for="request in requests"
              :key="request.id"
              :request="request"
              :subject="guarantorSubject"
              @deleteRequest="deleteRequest"
          ></guarant-request>
        </div>
      </div>
      <div class="request__form">
        <div class="form-box">
          <div class="select-type">
            <div class="input-label">Type:</div>
            <select class="custom-select" v-model="selectedType">
              <option
                  v-for="typeOption in typeOptions"
                  :key="typeOption.value"
                  :value="typeOption.value"
              >
                {{ typeOption.text }}
              </option>
            </select>
          </div>

          <div class="select-duration">
            <div class="input-label">Duration:</div>
            <select class="custom-select" v-model="selectedDuration">
              <option
                  v-for="duration in durationOptions"
                  :key="duration.value"
                  :value="duration.value"
              >
                {{ duration.text }}
              </option>
            </select>
          </div>

          <div class="select-repeating">
            <div class="input-label">Repeating:</div>
            <select class="custom-select" v-model="selectedRepeating">
              <option
                  v-for="repeating in repeatingOptions"
                  :key="repeating.value"
                  :value="repeating.value"
              >
                {{ repeating.text }}
              </option>
            </select>
          </div>
          <div class="select-date">
            <div class="input-date"> Date:
              <VDatePicker
                  v-model="range"
                  is-range
                  :masks="masks"
                  v-model.string="customer.birthday"
              >
                <template #default="{ inputValue, inputEvents }">
                  <div class="flex justify-center items-center">
                    <input
                        :value="inputValue.start"
                        v-on="inputEvents.start"
                        class="custom-select custom-date"
                        placeholder="Date from"
                    />
                    <input
                        :value="inputValue.end"
                        v-on="inputEvents.end"
                        class="custom-date custom-select"
                        placeholder="Date to"
                    />
                  </div>
                </template>
              </VDatePicker>
            </div>
          </div>

          <div class="notes">
            <div class="notes-label">Notes:</div>
            <textarea class="custom-textarea" v-model="notes"></textarea>
          </div>
        </div>
      </div>
      <div class="send__request">
        <div class="send_body" @click="sendRequest">Add request</div>
      </div>
    </div>
  </div>


</template>

<script>
import Navigation from "@/components/Navigation.vue";
import GuarantRequest from "@/components/GuarantRequest.vue";
import axios from "axios";
import {reactive, ref} from "vue";
import Cross from "@/components/icons/Cross.vue";


export default {
  components: {Cross, GuarantRequest, Navigation},
  data(){
    return{
      masks: ref({
        modelValue: 'YYYY-MM-DD',
      }),
      customer: reactive({
        name: 'Nathan Reyes',
        birthday: '1983-01-21',
      }),

      range: ref(null),
      buttons: [
        {text:'Home', class:'not-selected', route: '/'},
        {text:'Schedule', class:'not-selected', route:'/guarantor'},
        {text:'Instructors', class:'not-selected', route: '/guarantor/instructors'},
        {text:'Activities', class:'selected', route: '/guarantor/activities'},
      ],
      selectedType: 0,
      typeOptions : [
        {text: 'Lecture', value: 1},
        {text: 'Exercise', value: 2},
        {text: 'Laboratory', value: 3},
        {text: 'Exam', value: 4}
      ],
      selectedDuration: 0,
      durationOptions : [
        {text: '1 hour', value: 1},
        {text: '2 hour', value: 2},
        {text: '3 hour', value: 3},
        {text: '4 hour', value: 4},
      ],
      selectedRepeating: 0,
      repeatingOptions : [
        {text: 'Every week', value: 1},
        {text: 'One time', value: 4},
        {text: 'Odd week', value: 3},
        {text: 'Even week', value: 2},
      ],
      notes: '',
      requests: {},
      guarantorSubject: {},
      selectedDate: null,
    }
  },
  methods:{

    sendRequest(){
      const dataToSend = {
        "guarantor_notes": this.notes,
        "duration": this.selectedDuration,
        "activity_type_id": this.selectedType,
        "subject_id": 1, // CHANGE TO DYNAMIC {FOR TEST}
        "date_from": this.range.start,
        "date_to": this.range.end,
        "activity_repetition_id": this.selectedRepeating,
      };
      console.log(dataToSend);
      axios.post("http://127.0.0.1:8000/api/activity", dataToSend)
          .then(response=>{
            console.log(response);
            this.getRequests()
          })
          .catch(error=>{
            console.log(error);
          });

      this.selectedRepeating = 0;
      this.selectedDuration = 0;
      this.selectedType = 0;
      this.notes = '';
      this.range = ref(null);

    },
    getRequests(){
      // change to subject id
      axios.get("http://127.0.0.1:8000/api/get_requests/1")
          .then(response=>{
            this.requests = response.data.data;
          })
          .catch(error=>{
            console.log(error)
          });
    },
    async getSubject(){
      try {
        // change to user.id
        const response = await axios.get("http://127.0.0.1:8000/api/subject?guarantor_id=2")
        this.guarantorSubject = response.data.data[0];

      }catch (e) {
        console.log(e);
      }
    },
    deleteRequest(activity){
      axios.delete(`http://127.0.0.1:8000/api/activity/${activity.id}`)
          .then(response=>{
            console.log(response);
            this.getRequests();
          })
          .catch(e=>{
            console.log(e);
          })

    }

  },
  async mounted() {
    this.getRequests();
    await this.getSubject();
  }
}
</script>

<style scoped>
.main-container{
  background: none;
  display: flex;
  height: 83vh;
  justify-content: center;
}
.request-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  height: 93%;
  width: 60%;
  background: white;
  border-radius: 10px;
  border: 3px solid black;
}
.title{
  width: 100%;
  height: 7%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: bold;
}
.list__request{
  width: 100%;
  height: 28%;
  display: flex;
  justify-content: center;
}
.list_body{
  background: #E0CFB1;
  border: none;
  border-radius: 10px;
  display: flex;
  height: 97%;
  width: 90%;
  padding-left: 10px;
  justify-content: left;
  align-items: center;
  overflow: auto;
}
.request__form{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}
.send__request{
  width: 100%;
  height: 8%;
}
.form-box{
  height: 95%;
  width: 70%;
  background: #E0CFB1;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
}
.list_body::-webkit-scrollbar {
  width: 1px;
}

.list_body::-webkit-scrollbar-track {
  background-color: #d3d3d3;
  border: none;
  border-radius: 5px;
}

.list_body::-webkit-scrollbar-thumb {
  background-color: black;
  border-radius: 10px;
  border: 3px solid #d3d3d3;
  height: 100%;

}
.select-type{
  margin-top: 10px;
  width: 100%;
  height: 15%;
  display: flex;
  align-items: center;
  font-size: 25px;
  font-weight: bold;
}
.select-duration{
  display: flex;
  align-items: center;
  font-size: 25px;
  font-weight: bold;
  width: 100%;
  height: 15%;
}
.select-repeating{
  width: 100%;
  height: 15%;
  display: flex;
  align-items: center;
  font-size: 25px;
  font-weight: bold;
}
.select-date{
  width: 100%;
  height: 15%;
  display: flex;
  align-items: center;
  font-size: 25px;
  font-weight: bold;
}
.notes{
  flex-grow: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  font-size: 25px;
  font-weight: bold;
}
.input-label{
  margin-left: 10px;
}
.custom-select{
  margin-left: 20px;
  width: 200px;
  height: 30px;
  border: 2px solid black;
  font-size: 19px;
  cursor: pointer;
}
.notes-label{
  margin-top: 10px;
  margin-left: 10px;
}
.custom-textarea {
  width: 80%;
  height: 40%;
  border: 3px solid black;
  resize: none;
  font-size: 19px;
  align-self: center;
  padding: 10px;
}
.send__request{
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 25px;
}
.send_body{
  margin-top: 3px;
  border-bottom: 2px solid black;
  cursor: pointer;
}
.input-date{
  display: flex;
  margin-left: 10px;
  align-items: start;
}
.custom-date{
  margin-left: 15px;
  height: 25px;
}
</style>