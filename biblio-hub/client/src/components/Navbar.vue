<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <a href="#" class="pull-left"><img src="../assets/logo.png" width="50%"></a>
    </nav>
</template>

<script>
import EventBus from './EventBus.vue';

export default {
  data() {
    return {
      auth: '',
      user: '',
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('usertoken');
    },
  },
  mounted() {
    EventBus.$on('logged-in', (status) => {
      this.auth = status;
    });
  },
};
</script>
