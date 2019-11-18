import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import {store} from './store/store'

window.axios = axios;
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
  store: store,
}).$mount('#app');
