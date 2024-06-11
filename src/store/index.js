import { createStore } from 'vuex';
import axios from '../axios';

export default createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: {},
    courses: [],
    enrollments: [],
    classInfo: []
  },
  mutations: {
    auth_success(state, token, user) {
      state.token = token;
      state.user = user;
    },
    logout(state) {
      state.token = '';
      state.user = {};
    },
    set_courses(state, courses) {
      state.courses = courses;
    },
    set_enrollments(state, enrollments) {
      state.enrollments = enrollments;
    },
    set_class_info(state, classInfo) {
      state.classInfo = classInfo;
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        axios.post('/auth/login', user)
          .then(resp => {
            const token = resp.data.access_token;
            const user = resp.data.user;
            localStorage.setItem('token', token);
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
            commit('auth_success', token, user);
            resolve(resp);
          })
          .catch(err => {
            localStorage.removeItem('token');
            reject(err);
          });
      });
    },
    register(_, user) {
      return new Promise((resolve, reject) => {
        axios.post('/auth/register', user)
          .then(resp => {
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve) => {
        commit('logout');
        localStorage.removeItem('token');
        delete axios.defaults.headers.common['Authorization'];
        resolve();
      });
    },
    getCourses({ commit }) {
      axios.get('/courses')
        .then(resp => {
          commit('set_courses', resp.data);
        });
    },
    addCourse({ commit }, course) {
      return new Promise((resolve, reject) => {
        axios.post('/courses', course, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_courses', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    deleteCourse({ commit }, courseId) {
      return new Promise((resolve, reject) => {
        axios.delete(`/courses/${courseId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_courses', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    getEnrollments({ commit }) {
      axios.get('/enrollments', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(resp => {
          commit('set_enrollments', resp.data);
        });
    },
    enroll({ commit }, enrollment) {
      return new Promise((resolve, reject) => {
        axios.post('/enrollments', enrollment, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_enrollments', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    dropCourse({ commit }, courseId) {
      return new Promise((resolve, reject) => {
        axios.delete(`/enrollments/${courseId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_enrollments', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    getClassInfo({ commit }) {
      axios.get('/class_info', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(resp => {
          commit('set_class_info', resp.data);
        });
    },
    addClassInfo({ commit }, classInfo) {
      return new Promise((resolve, reject) => {
        axios.post('/class_info', classInfo, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_class_info', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    updateClassInfo({ commit }, { class_id, classInfo }) {
      return new Promise((resolve, reject) => {
        axios.put(`/class_info/${class_id}`, classInfo, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_class_info', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    deleteClassInfo({ commit }, class_id) {
      return new Promise((resolve, reject) => {
        axios.delete(`/class_info/${class_id}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(resp => {
            commit('set_class_info', resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    courses: state => state.courses,
    enrollments: state => state.enrollments,
    classInfo: state => state.classInfo
  }
});
