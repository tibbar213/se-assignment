import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/Home.vue';
import CoursesPage from '../views/Courses.vue';
import EnrollmentsPage from '../views/Enrollments.vue';
import LoginPage from '../views/Login.vue';
import RegisterPage from '../views/Register.vue';
import AddCourseForm from '../components/AddCourseForm.vue';
import EditCourseForm from '../components/EditCourseForm.vue';
import EnrollmentsList from '../components/EnrollmentsList.vue';
import EnrollmentForm from '../components/EnrollmentForm.vue';
import AddClassInfoForm from '../components/AddClassInfoForm.vue';
import EditClassInfoForm from '../components/EditClassInfoForm.vue';
import ClassInfoList from '../components/ClassInfoList.vue';
import CourseDetail from '../components/CourseDetail.vue';

const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/courses', name: 'CoursesPage', component: CoursesPage },
  { path: '/courses/:id', name: 'CourseDetailPage', component: CourseDetail },
  { path: '/courses/add', name: 'AddCourseForm', component: AddCourseForm },
  { path: '/courses/edit/:id', name: 'EditCourseForm', component: EditCourseForm },
  { path: '/enrollments', name: 'EnrollmentsPage', component: EnrollmentsPage },
  { path: '/enrollments/list', name: 'EnrollmentsList', component: EnrollmentsList },
  { path: '/enrollments/form', name: 'EnrollmentForm', component: EnrollmentForm },
  { path: '/class_info', name: 'ClassInfoList', component: ClassInfoList },
  { path: '/class_info/add', name: 'AddClassInfoForm', component: AddClassInfoForm },
  { path: '/class_info/edit/:id', name: 'EditClassInfoForm', component: EditClassInfoForm },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
