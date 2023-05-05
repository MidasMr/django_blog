<template>
  <MyHeader></MyHeader>
    <div id="app">
      <title>Последние обновления</title>
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
