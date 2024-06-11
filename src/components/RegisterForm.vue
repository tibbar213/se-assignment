<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="user_type">User Type:</label>
        <select v-model="user_type" required>
          <option value="超级管理员">超级管理员</option>
          <option value="管理员">管理员</option>
          <option value="学生">学生</option>
        </select>
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      user_type: '学生'
    };
  },
  methods: {
    register() {
      this.$store.dispatch('register', {
        username: this.username,
        password: this.password,
        user_type: this.user_type
      }).then(() => {
        this.$router.push('/login');
      }).catch(err => {
        console.error(err);
      });
    }
  }
};
</script>
