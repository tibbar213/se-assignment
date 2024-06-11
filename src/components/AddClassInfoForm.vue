<template>
  <div>
    <h2>Add Class Info</h2>
    <form @submit.prevent="addClassInfo">
      <div>
        <label for="course_id">Course ID:</label>
        <input type="number" v-model="course_id" required />
      </div>
      <div>
        <label for="student_type">Student Type:</label>
        <select v-model="student_type" required>
          <option value="本科生">本科生</option>
          <option value="研究生">研究生</option>
        </select>
      </div>
      <div>
        <label for="year_limit">Year Limit:</label>
        <input type="number" v-model="year_limit" required />
      </div>
      <button type="submit">Add Class Info</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddClassInfoForm',
  data() {
    return {
      course_id: '',
      student_type: '本科生',
      year_limit: ''
    };
  },
  methods: {
    addClassInfo() {
      this.$store.dispatch('addClassInfo', {
        course_id: this.course_id,
        student_type: this.student_type,
        year_limit: this.year_limit
      }).then(() => {
        this.$router.push('/class_info');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
