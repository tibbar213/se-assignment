<template>
  <div>
    <h2>My Enrollments</h2>
    <ul>
      <li v-for="enrollment in enrollments" :key="enrollment.enrollment_id">
        Course ID: {{ enrollment.course_id }} - Enrollment Date: {{ enrollment.enrollment_date }}
        <button @click="dropCourse(enrollment.course_id)">Drop</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'EnrollmentsList',
  computed: {
    enrollments() {
      return this.$store.getters.enrollments;
    }
  },
  created() {
    this.$store.dispatch('getEnrollments');
  },
  methods: {
    dropCourse(courseId) {
      this.$store.dispatch('dropCourse', courseId).then(() => {
        this.$store.dispatch('getEnrollments');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
