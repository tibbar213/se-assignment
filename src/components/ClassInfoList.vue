<template>
  <div>
    <h2>Class Info List</h2>
    <router-link to="/class_info/add">Add Class Info</router-link> <!-- 添加链接 -->
    <ul>
      <li v-for="classInfo in classInfoList" :key="classInfo.class_id">
        Course ID: {{ classInfo.course_id }} - Student Type: {{ classInfo.student_type }} - Year Limit: {{ classInfo.year_limit }}
        <button @click="deleteClassInfo(classInfo.class_id)">Delete</button>
        <router-link :to="'/class_info/edit/' + classInfo.class_id">Edit</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ClassInfoList',
  computed: {
    classInfoList() {
      return this.$store.getters.classInfo;
    }
  },
  created() {
    this.$store.dispatch('getClassInfo');
  },
  methods: {
    deleteClassInfo(classId) {
      this.$store.dispatch('deleteClassInfo', classId).then(() => {
        this.$store.dispatch('getClassInfo');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
