import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('access_token') || null,
  },
  getters: {
    loggedIn(state) {
      return state.token !== null;
    },
  },
  actions: {
    destroyToken(context) {
      axios.defaults.headers.common.Authorization += `Bearer ${context.state.token}`;
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axios.post('/logout')
            .then((response) => {
              localStorage.removeItem('access_token');
              context.commit('destroyToken');
              resolve(response);
            })
            .catch((error) => {
              localStorage.removeItem('access_token');
              context.commit('destroyToken');
              reject(error);
            });
        });
      }
      return null;
    },
    retrieveToken(context, credentials) {
      return new Promise((resolve, reject) => {
        axios.post('http://localhost:5000/login/', {
          login: credentials.login,
          password: credentials.password,
        }, { headers: { 'Content-Type': 'application/json' } })
          .then((response) => {
            const { token } = response.data;
            console.log(token);
            // localStorage.setItem('access_token', token);
            // context.commit('retrieveToken', token);
            resolve(response);
          })
          .catch((error) => {
            reject(error);
          });
      });
    },
  },
});
