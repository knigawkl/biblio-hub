import Vue from 'vue';
import Router from 'vue-router';
import SimpleVueValidation from 'simple-vue-validator';
import Register from './components/Register.vue';
import Login from './components/Login.vue';

Vue.use(Router, SimpleVueValidation);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: '/register',
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
    },
  ],
});
