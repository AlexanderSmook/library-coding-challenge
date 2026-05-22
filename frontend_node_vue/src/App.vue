<script>

</script>

<template>
  <div id="app">
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/new">Add book</router-link>
  </nav>

  <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav a {
  background-color: #2c3e50;
  color: #fff;
  padding: 14px 16px;
  margin: 16px;
  border-radius: 4px;
}

nav a:hover {
  background-color: #36648f;
}
</style>
