<template>
  <div>
    <h2>Edit Class Info</h2>
    <form @submit.prevent="editClassInfo">
      <div>
        <label for="course_id">Course ID:</label>
        <input type="number" v-model="classInfo.course_id" required />
      </div>
      <div>
        <label for="student_type">Student Type:</label>
        <select v-model="classInfo.student_type" required>
          <option value="本科生">本科生</option>
          <option value="研究生">研究生</option>
        </select>
      </div>
      <div>
        <label for="year_limit">Year Limit:</label>
        <input type="number" v-model="classInfo.year_limit" required />
      </div>
      <button type="submit">Update Class Info</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'EditClassInfoForm',
  data() {
    return {
      classInfo: {
        course_id: '',
        student_type: '',
        year_limit: ''
      }
    };
  },
  created() {
    const classId = this.$route.params.id;
    axios.get(`/class_info/${classId}`)
        .then(response => {
          this.classInfo = response.data;
        })
        .catch(error => {
          console.error('Error fetching class info details:', error);
        });
  },
  methods: {
    editClassInfo() {
      const classId = this.$route.params.id;
      axios.put(`/class_info/${classId}`, this.classInfo, {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`
        }
      })
          .then(() => {
            this.$router.push('/class_info');
          })
          .catch(err => {
            console.error(err);
          });
    }
  }
};
</script>
