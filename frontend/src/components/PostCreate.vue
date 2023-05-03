<template>
<div class="container-sm">
  <form @submit="handlePost">
    <div>
      <label for="exampleFormControlTextarea1">Введите заголовок поста</label>
      <input class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="post_title">
    </div>
    <div>
      <label for="exampleFormControlTextarea1">Введите текст поста</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="post_text"></textarea>
    </div>
    <div>
        <label for="exampleFormControlTextarea1">Добавьте изображение:</label>
        <p>
          <input type="file" @change="uploadFile" ref="file">
        </p>
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>
</div>
</template>

<script>
import authHeader from '../services/auth-header';
export default {
    data() {
        return {
            post_text: '',
            post_title: '',
            image: null
        }
    },
    methods: {
        async handlePost() {
            const post_headers = authHeader();
            const post_data = {
                text: this.post_text,
                title: this.post_title
            };
            if (this.image) {
                post_headers['Content-Type'] = 'multipart/form-data'
                post_data['file'] = this.image
                await this.$http.post(
                    `http://127.0.0.1:8000/api/posts/`,
                    post_data,
                    {headers: post_headers}
                ).then(this.$router.push("/posts")
            );
            } else {
                await this.$http.post(
                    `http://127.0.0.1:8000/api/posts/`,
                    post_data,
                    {headers: post_headers}
                ).then(this.$router.push("/posts")
            );
            }
        },
        uploadFile() {
            this.image = this.$refs.file.files[0];
        },
    }
}
</script>