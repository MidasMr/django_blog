<template>
<div class="container-sm">
  <Form @submit="handlePostCreate" :validation-schema="schema">
    <div v-if="!successful">
      <div class="form-group">
        <label for="post_title">Заголовок</label>
        <Field name="post_title" type="text" class="form-control" />
        <ErrorMessage name="post_title" class="error-feedback" style="color: red;"/>
      </div>
      <div class="form-group">
        <label for="post_text">Введите текст поста</label>
        <Field name="post_text" as="textarea" class="form-control" ></Field>
        <ErrorMessage name="post_text" class="error-feedback" style="color: red;"/>
      </div>
      <div class="form-group">
        <label for="file">Добавьте изображение:</label>
        <p><input type="file" @change="uploadFile" ref="file"></p>
      </div>
      <button class="btn btn-primary btn-block" type="submit" :disabled="loading">
        <span
          v-show="loading"
          class="spinner-border spinner-border-sm"
        ></span>
        Отправить
      </button>
    </div>
  </Form>
  <div
    v-if="message"
    class="alert"
    :class="successful ? 'alert-success' : 'alert-danger'"
  >
    {{ message }}
  </div>
</div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";


import authHeader from '../services/auth-header';

export default {
    components: {
        Form,
        Field,
        ErrorMessage,
    },
    data() {
        const schema = yup.object().shape({
            post_title: yup
              .string()
              .required("Заголовок обязателен!")
              .min(3, "Длина заголовка может быть минимум 3 символа")
              .max(20, "Длина заголовка может быть максимум 20 символов"),
            post_text: yup
              .string()
              .required("Текст поста обязателен")
              .min(3, "Длина поста может быть минимум 3 символа")
              .max(5000, "Текст поста может быть максимум 5000 символов"),
        });
        return {
            successful: false,
            loading: false,
            message: "",
            iamge: null,
            schema,
        }
    },
    methods: {
        async handlePostCreate(user) {
            this.message = "";
            this.successful = false;
            this.loading = true;
            const post_headers = authHeader();
            const post_data = {
                text: user.post_text,
                title: user.post_title
            };
            if (this.image) {
                post_headers['Content-Type'] = 'multipart/form-data'
                post_data['file'] = this.image
            }
            await this.$http.post(
                `http://127.0.0.1:8000/api/posts/`,
                post_data,
                {headers: post_headers}
            ).then(
                (data) => {
                this.message = data.message;
                this.successful = true;
                this.loading = false;
                this.$router.push("/posts");
                },
                (error) => {
                    this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                    this.successful = false;
                    this.loading = false;
                }
            );
        },
        uploadFile() {
            this.image = this.$refs.file.files[0];
        },
    },
    created() {
        document.title = 'Создать пост'
    }
}
</script>