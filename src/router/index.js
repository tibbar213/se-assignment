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
import CourseDetail from '../components/CourseDetail.vue'; // 引入课程详情组件

const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/courses', name: 'CoursesPage', component: CoursesPage },
  { path: '/courses/:id', name: 'CourseDetailPage', component: CourseDetail }, // 添加课程详情路由
  { path: '/enrollments', name: 'EnrollmentsPage', component: EnrollmentsPage },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  { path: '/courses/add', name: 'AddCourseForm', component: AddCourseForm },
  { path: '/courses/edit/:id', name: 'EditCourseForm', component: EditCourseForm },
  { path: '/enrollments/list', name: 'EnrollmentsList', component: EnrollmentsList },
  { path: '/enrollments/form', name: 'EnrollmentForm', component: EnrollmentForm },
  { path: '/class_info/add', name: 'AddClassInfoForm', component: AddClassInfoForm }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
