<template>
  <div v-if="course">
    <h2>{{ course.course_name }}</h2>
    <p>{{ course.course_description }}</p>
    <p>Instructor: {{ course.instructor }}</p>
    <p>Credits: {{ course.credits }}</p>
    <p>Start Time: {{ course.start_time }}</p>
    <p>Max Students: {{ course.max_students }}</p>
    <router-link :to="'/courses/edit/' + course.course_id">
      <button>Edit Course</button>
    </router-link>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'CourseDetail',
  data() {
    return {
      course: null
    };
  },
  created() {
    const courseId = this.$route.params.id;
    axios.get(`/courses/${courseId}`)
        .then(response => {
          this.course = response.data;
        })
        .catch(error => {
          console.error('Error fetching course details:', error);
        });
  }
};
</script>
