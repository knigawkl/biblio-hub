<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form id="form" v-on:submit.prevent="register">
          <div class="form-group">
            <label for="email">Email Address</label>
            <input id="email" type="email" v-model="email" class="form-control" name="email"
                   placeholder="Enter email" required>
          </div>
          <div class="form-group">
            <label id="login_label" for="reg_login">Login</label>
            <div id="msg"></div>
            <input id="reg_login" type="text" v-model="login" class="form-control" name="reg_login"
                   placeholder="Enter login" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input id="password" type="password" v-model="password" class="form-control"
                   name="password" placeholder="Enter Password" required>
          </div>
          <button type="submit" class="btn btn-sm btn-dark btn-block">Register</button>
        </form>
        <span>
          Click <a href="http://localhost:8081/#/login">here</a> to sign in with an existing account.
        </span>
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

  document.getElementById('reg_login').addEventListener('change', (e) => {
    const input = e.target;
    const path = 'http://localhost:5000/register/';
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
      email: '',
      login: '',
      password: '',
    };
  },
  methods: {
    register() {
      const path = 'http://localhost:5000/register/';

      axios.post(path, {
        email: this.email,
        login: this.reg_login,
        password: this.password,
      }).then((resp) => {
        if (resp.data === 'Username available') {
          this.$router.push({ name: 'Login' });
        }
      });
    },
  },
};

</script>
