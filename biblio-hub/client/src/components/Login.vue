<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form id="form" v-on:submit.prevent="login">
          <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
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
          <button type="submit" class="btn btn-lg btn-dark btn-block">Sign in</button>
        </form>
        <button type="submit" class="btn btn-lg btn-dark btn-block">Sign up</button>
      </div>
    </div>
  </div>
</template>
