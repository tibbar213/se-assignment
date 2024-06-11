<template>
  <div>
    <h2>Edit Course</h2>
    <form @submit.prevent="editCourse">
      <div>
        <label for="course_name">Course Name:</label>
        <input type="text" v-model="course.course_name" required />
      </div>
      <div>
        <label for="course_code">Course Code:</label>
        <input type="text" v-model="course.course_code" required />
      </div>
      <div>
        <label for="course_description">Course Description:</label>
        <input type="text" v-model="course.course_description" required />
      </div>
      <div>
        <label for="instructor">Instructor:</label>
        <input type="text" v-model="course.instructor" required />
      </div>
      <div>
        <label for="credits">Credits:</label>
        <input type="number" v-model="course.credits" required />
      </div>
      <div>
        <label for="start_time">Start Time:</label>
        <input type="datetime-local" v-model="course.start_time" required />
      </div>
      <div>
        <label for="max_students">Max Students:</label>
        <input type="number" v-model="course.max_students" required />
      </div>
      <button type="submit">Update Course</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      course: {}
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
  },
  methods: {
    editCourse() {
      const courseId = this.$route.params.id;
      axios.put(`/courses/${courseId}`, this.course, {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push('/courses');
      })
      .catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
