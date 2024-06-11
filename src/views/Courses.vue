<template>
  <div>
    <h1>Courses</h1>
    <CourseList />
    <router-link to="/courses/add">Add Course</router-link>
  </div>
</template>

<script>
import CourseList from '../components/CourseList.vue';

export default {
  name: 'CoursesPage',
  components: {
    CourseList
  }
};
</script>
