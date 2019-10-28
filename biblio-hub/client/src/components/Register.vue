<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form id="form" v-on:submit.prevent="register">
          <h1 class="h3 mb-3 font-weight-normal">Register</h1>
          <div class="form-group">
            <label id="login_label" for="login">Login</label>
            <div id="msg"></div>
            <input id="login" type="text" v-model="login" class="form-control" name="login"
                   placeholder="Enter login">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input id="password" type="password" v-model="password" class="form-control"
                   name="password" placeholder="Enter Password">
          </div>
          <button type="submit" class="btn btn-lg btn-dark btn-block">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">

import axios from 'axios';

window.onload = () => {
  document.getElementById('form').onkeypress = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
    }
  };

  document.getElementById('form').addEventListener('submit', (e) => {
    e.preventDefault();
  });

  document.getElementById('login').addEventListener('change', (e) => {
    const input = e.target;
    const path = '/register/';
    axios.post(path, {
      login: input.value,
      password: 'mock',
    }).then((response) => {
      if (response.data === 'Username available') {
        document.getElementById('login_label').innerHTML = 'Login available!';
        document.getElementById('login_label').style.color = 'green';
      } else {
        document.getElementById('login_label').innerHTML = 'Login already in the database!';
        document.getElementById('login_label').style.color = 'red';
      }
    });
  });
};

export default {
  data() {
    return {
      login: '',
      password: '',
    };
  },
  methods: {
    register() {
      const path = '/register/';

      axios.post(path, {
        login: this.login,
        password: this.password,
      }).then((resp) => {
        if (resp.data === 'Username available') {
          this.$router.push({ name: 'Login' });
        } else {
          alert('Cannot register with this login');
        }
      });
    },
  },
};

</script>
