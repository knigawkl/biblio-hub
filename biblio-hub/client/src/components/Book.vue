<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
        <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script type="text/javascript">

import axios from 'axios';

export default {
  data() {
    return {
      file: '',
    };
  },
  methods: {
    submitFile() {
      const formData = new FormData();
      formData.append('file', this.file);
      axios.post('/single-file', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(() => {
          console.log('SUCCESS!!');
        })
        .catch(() => {
          console.log('FAILURE!!');
        });
    },
    handleFileUpload() {
      this.file = this.$refs.file.files;
    },
  },
};
</script>
