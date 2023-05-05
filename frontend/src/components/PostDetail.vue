<template>
<div class="container">
  <h2 class="blog-post-title mb-1"> {{ post.title }}</h2>
  <p class="blog-post-meta">{{ dateTime(post.pub_date)}} by <a :href="`http://localhost:8080/profile/${post.author}`">@{{ post.author }}</a></p>
  <div class="row text-container">
    <div class="col p-4 d-flex flex-column position-static"><p>{{post.text}}</p></div>
    <div v-if="post.image" class="col-auto d-none d-lg-block rounded p-4"><img :src="`${post.image}`" style="width: 150px; height: 150px; object-fit: fill; border-radius: 10px;" class="col-12 col-md-3"></div>
    <div class="card" style="background-color: #f8f8f8;">
      <div class="card-body">
        <form @submit="handleComment">
          <div class="form-group mb-1">
            <textarea
                id="comment"
                class="form-control"
                v-model="comment_text"
                placeholder="Оставьте свой комментарий"
            ></textarea>
          </div>
          <button type="submit" class="btn btn-success">Отправить</button>
        </form>
      </div>
    </div>
  </div>
  <div class="text-container" style="margin: 1% ;" v-if="hasComments">
    <h5>Комментарии:</h5>
    <div v-for="comment in comments" :key="comment" class="media mb-4" id="accordion">
      <div class="media-body border-bottom">
        <a :href="`http://localhost:8080/profile/${post.author}`">@{{ comment.author }}</a>
        <p>{{ comment.text }}</p>
        <p class="comment-meta">{{ dateTime(comment.created)}}</p>
      </div>
    </div>
  </div>
  <div v-else><h5>Комментариев пока нет! Прокомментируйте первым</h5></div>
  <ul class="pagination justify-content-center">
    <li class="page-item" ><button class="btn btn-primary" :class="{'disabled': !showPrevButton}" @click="loadPrev()">Предыдущая страница</button></li>
    <li class="page-item"><a class="page-link">Текущая страница: {{ currnent_page }}</a></li>
    <li class="page-item" ><button class="btn btn-primary" :class="{'disabled': !showNextButton}" @click="loadNext()">Следуюущая страница</button></li>
  </ul>
</div>
</template>

<script>
import moment from 'moment';
import authHeader from '../services/auth-header';

moment.locale('ru');

export default {
        data() {
            return {
                post: {},
                comments: [],
                comment_text: '',
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
                    const posts_response = await this.$http.get(
                            `http://127.0.0.1:8000/api/posts/${this.$route.params.id}`,
                            { headers: authHeader() }
                        )
                    this.post = posts_response.data;

                    await fetch(
                        `http://127.0.0.1:8000/api/posts/${this.$route.params.id}/comments/?page=${this.currnent_page}`,
                        { headers: authHeader() }
                    )
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
                            this.comments = data.results;
                        })
                } catch (error) {
                    console.log(error);
                }
            },
            async handleComment() {
                await this.$http.post(
                    `http://127.0.0.1:8000/api/posts/${this.$route.params.id}/comments/`,
                    {text: this.comment_text},
                    {headers: authHeader()}
                );
            },
            dateTime(value) {
                return moment(value).format('D MMMM, YYYY в HH:MM');
            },
        },
        computed: {
            hasComments() {
                return this.comments.length > 0
            }
        },
        created() {
            document.title = 'Пост';
            this.getData();
        }
    }
</script>

<style>
.text-container {
    background-color:#f4f4f4;
    border-radius: 10px;
    padding: 1%;
}

.comment-meta {
    margin-top: 1rem;
    margin-bottom: 1rem;
    color: #727272;
}

.post-detail {
    margin-top: 1rem;
}
</style>