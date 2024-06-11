<template>
  <div>
    <h1>Login</h1>
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue';

export default {
  name: 'LoginPage',
  components: {
    LoginForm
  }
};
</script>
