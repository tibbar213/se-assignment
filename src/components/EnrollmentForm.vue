<template>
  <div>
    <h2>Enroll in a Course</h2>
    <form @submit.prevent="enroll">
      <div>
        <label for="course">Select Course:</label>
        <select v-model="selectedCourse" required>
          <option v-for="course in courses" :key="course.course_id" :value="course.course_id">
            {{ course.course_name }} - {{ course.instructor }} - {{ course.credits }} credits
          </option>
        </select>
      </div>
      <button type="submit">Enroll</button>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      selectedCourse: ''
    };
  },
  computed: {
    ...mapGetters(['courses'])
  },
  created() {
    this.$store.dispatch('getCourses');
  },
  methods: {
    enroll() {
      this.$store.dispatch('enroll', { course_id: this.selectedCourse }).then(() => {
        this.$router.push('/enrollments');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
