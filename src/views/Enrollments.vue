<template>
  <div>
    <h1>My Enrollments</h1>
    <EnrollmentsList />
    <EnrollmentForm />
  </div>
</template>

<script>
import EnrollmentsList from '../components/EnrollmentsList.vue';
import EnrollmentForm from '../components/EnrollmentForm.vue';

export default {
  name: 'EnrollmentsPage',
  components: {
    EnrollmentsList,
    EnrollmentForm
  }
};
</script>
