<template>
  <div>
    <h2>Courses</h2>
    <ul>
      <li v-for="course in courses" :key="course.course_id">
        <router-link :to="'/courses/' + course.course_id">{{ course.course_name }}</router-link>
        <button @click="deleteCourse(course.course_id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  computed: {
    courses() {
      return this.$store.getters.courses;
    }
  },
  created() {
    this.$store.dispatch('getCourses');
  },
  methods: {
    deleteCourse(courseId) {
      this.$store.dispatch('deleteCourse', courseId).then(() => {
        this.$store.dispatch('getCourses');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
