<template>
  <div>
    <h2>Add Course</h2>
    <form @submit.prevent="addCourse">
      <div>
        <label for="course_name">Course Name:</label>
        <input type="text" v-model="course_name" required />
      </div>
      <div>
        <label for="course_code">Course Code:</label>
        <input type="text" v-model="course_code" required />
      </div>
      <div>
        <label for="course_description">Course Description:</label>
        <input type="text" v-model="course_description" required />
      </div>
      <div>
        <label for="instructor">Instructor:</label>
        <input type="text" v-model="instructor" required />
      </div>
      <div>
        <label for="credits">Credits:</label>
        <input type="number" v-model="credits" required />
      </div>
      <div>
        <label for="start_time">Start Time:</label>
        <input type="datetime-local" v-model="start_time" required />
      </div>
      <div>
        <label for="max_students">Max Students:</label>
        <input type="number" v-model="max_students" required />
      </div>
      <button type="submit">Add Course</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      course_name: '',
      course_code: '',
      course_description: '',
      instructor: '',
      credits: '',
      start_time: '',
      max_students: ''
    };
  },
  methods: {
    addCourse() {
      this.$store.dispatch('addCourse', {
        course_name: this.course_name,
        course_code: this.course_code,
        course_description: this.course_description,
        instructor: this.instructor,
        credits: this.credits,
        start_time: this.start_time,
        max_students: this.max_students
      }).then(() => {
        this.$router.push('/courses');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
