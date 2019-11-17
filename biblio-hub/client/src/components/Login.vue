<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form id="form" v-on:submit.prevent="login">
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
          <button type="submit" class="btn btn-sm btn-dark btn-block">Sign in</button>
        </form>
        <span>
          Click <a href="http://localhost:8081/#/register">here</a> to create a new account.
        </span>
      </div>
    </div>
  </div>
</template>
