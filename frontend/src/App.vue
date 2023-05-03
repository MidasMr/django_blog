<template>
  <MyHeader></MyHeader>
    <div id="app">
      <router-view></router-view>
    </div>
  <MyFooter></MyFooter>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  @import '~bootstrap/dist/css/bootstrap.css';
</style>
