<template>
<div class="container">
  <div class="col-mb-2">
    <div>
      <h2 class="pb-4 mb-4 fst-italic border-bottom"> Последние обновления на сайте </h2>
    </div>
    <article v-for="post in posts" :key="post">
      <div class="row blog-post">
        <h2 class="blog-post-title mb-1"> {{ post.title }}</h2>
        <p class="blog-post-meta">{{ dateTime(post.pub_date)}} by <a :href="`profile/${post.author}`">@{{ post.author }}</a></p>
        <div class="col p-4 d-flex flex-column position-static"><p>{{ post.text }}</p></div>
        <div v-if="post.image" class="col-auto d-none d-lg-block rounded p-4"><img :src="`${post.image}`" style="width: 150px; height: 150px; object-fit: fill; border-radius: 10px;" class="col-12 col-md-3"></div>
        <p>
          <router-link :to="{ name: 'PostDetail', params: { id: post.id } }">
            <a class="btn btn-outline-success rounded-pill" href="">Подробнее / Добавить комментарий</a>
          </router-link>
        </p>
      </div>
    </article>
    <ul class="pagination justify-content-center">
      <li class="page-item" ><button class="btn btn-primary" :class="{'disabled': !showPrevButton}" @click="loadPrev()">Предыдущая страница</button></li>
      <li class="page-item"><a class="page-link">Текущая страница: {{ currnent_page }}</a></li>
      <li class="page-item" ><button class="btn btn-primary" :class="{'disabled': !showNextButton}" @click="loadNext()">Следуюущая страница</button></li>
    </ul>
  </div>
</div>
</template>

<script>
    import moment from 'moment';
    export default {
        data() {
            return {
                posts: [],
                currnent_page: 1,
                showNextButton: false,
                showPrevButton: false
            }
        },
        methods: {
            loadNext() {
                this.currnent_page += 1
                this.getData()
            },
            loadPrev() {
                this.currnent_page -= 1
                this.getData()
            },
            async getData() {
                try {
                    await fetch(`http://127.0.0.1:8000/api/posts/?page=${this.currnent_page}`)
                        .then(response => {
                            return response.json()
                        })
                        .then(data => {
                            if (data.next) {
                                this.showNextButton = true
                            } else {
                                this.showNextButton = false
                            }
                            if (data.previous) {
                                this.showPrevButton = true
                            } else {
                                this.showPrevButton = false
                            }
                            this.posts = data.results;
                        })
                } catch (error) {
                    console.log(error);
                }
            },
            dateTime(value) {
                return moment(value).format('D MMMM, YYYY');
            },
        },
        computed: {
            currentUser() {
                return this.$store.state.auth.user;
            }
        },
        mounted() {
            this.getData()
        },
    }
</script>

<style>
.blog-post {
    background-color:#f9f9f9;
    border-radius: 10px;
    margin-bottom: 1rem;
    padding: 1%;
}
.blog-post-meta {
    margin-bottom: 1.25rem;
    color: #727272;
}
</style>
