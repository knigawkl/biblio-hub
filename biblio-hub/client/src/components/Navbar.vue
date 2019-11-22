<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <div class="pull-left">
        <img src="../assets/logo.png" width="50%" alt="logo">
      </div>
      <div class="pull-right">
        <ul class="nav">
          <li style="float:right" v-if="!loggedIn">
            <router-link :to="{ name: 'Login' }">Sign in</router-link>
          </li>
          <li style="float:right" v-if="!loggedIn">
            <router-link :to="{ name: 'Register' }">Sign up</router-link>
          </li>
          <li style="float:right" v-if="loggedIn">
            <router-link :to="{ name: 'Logout' }">Log out</router-link>
          </li>
        </ul>
      </div>
    </nav>
</template>

<script>
export default {
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn;
    },
  },
};
</script>
