<template>
  <nav class="navbar navbar-expand-lg navbar-light" id="mainNav" style="background-color: powderblue;">
    <div class="container px-1 px-lg-1">
      <a class="navbar-brand" href="/posts">MBlog</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Меню
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ms-auto py-4 py-lg-0">
          <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="/posts">
            <i class="bi bi-house"></i> Домой</a>
          </li>
          <li class="nav-item" v-if="loggedIn"><a class="nav-link px-lg-3 py-3 py-lg-4" href="" @click.prevent="postCreate">
            <i class="bi bi-plus-square"></i> Cоздать пост</a>
          </li>
          <li class="nav-item" v-if="loggedIn"><a class="nav-link px-lg-3 py-3 py-lg-4" href="/profile">
            <i class="bi bi-person-fill"></i> Профиль</a>
          </li>
          <li class="nav-item" v-if="loggedIn"><a class="nav-link px-lg-3 py-3 py-lg-4" href="" @click.prevent="logOut">
            <i class="bi bi-box-arrow-right"></i> Выйти</a>
          </li>
          <li class="nav-item" v-if="!loggedIn"><a class="nav-link px-lg-3 py-3 py-lg-4" href="/login">
            <i class="bi bi-box-arrow-in-right"></i> Войти</a>
          </li>
          <li class="nav-item" v-if="!loggedIn"><a class="nav-link px-lg-3 py-3 py-lg-4" href="/register">
            <i class="bi bi-person-plus-fill"></i> Регистрация</a>
          </li>
        </ul>
      </div>
  </div>
</nav>
</template>

<script>
export default {
  name: 'app',
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout');
      this.$router.push('/login');
    },
    postCreate() {
        this.$router.push('/posts/create')
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  }
}
</script>