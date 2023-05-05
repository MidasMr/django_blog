<template>
<section class="vh-100" style="background-color: #9de2ff;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-md-9 col-lg-7 col-xl-5">
        <div class="card" style="border-radius: 15px;">
          <div class="card-body p-4">
            <div class="d-flex text-black">
              <div class="flex-shrink-0">
                <img src="//ssl.gstatic.com/accounts/ui/avatar_2x.png"
                  alt="Generic placeholder image" class="img-fluid"
                  style="width: 180px; border-radius: 10px;">
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="mb-1">{{ user.username }}</h5>
                <p class="mb-2 pb-1" style="color: #2b2a2a;">{{ user.email }}</p>
                <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                  style="background-color: #efefef;">
                  <div>
                    <p class="small text-muted mb-1">Articles</p>
                    <p class="mb-0"> ... </p>
                  </div>
                  <div class="px-3">
                    <p class="small text-muted mb-1">Followers</p>
                    <p class="mb-0"> ... </p>
                  </div>
                  <div>
                    <p class="small text-muted mb-1">Rating</p>
                    <p class="mb-0"> ... </p>
                  </div>
                </div>
                <div v-if="!self_profile" class="d-flex pt-1">
                  <button type="button" class="btn btn-outline-primary me-1 flex-grow-1">Chat</button>
                  <button type="button" class="btn btn-primary flex-grow-1">Follow</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import authHeader from '../services/auth-header'; 
export default {
    name: 'Profile',
    data() {
        return {
            user: null,
            self_profile: true
        }
    },
    methods: {
        async getCurrentUser() {
            try {
                var user_response = {}
                if (this.$route.params.username) {
                    this.self_profile = false
                    user_response = await this.$http.get(
                        `http://127.0.0.1:8000/api/auth/users/${this.$route.params.username}`,
                        {headers: authHeader()}
                    )
                } else {
                    user_response = await this.$http.get(
                        'http://127.0.0.1:8000/api/auth/users/me/',
                        {headers: authHeader()}
                    )
                }
                this.user = user_response.data
            } catch (error) {
                console.log(error);
            }
      }
    },
    created() {
        document.title = 'Профиль';
        this.getCurrentUser();
    }
};
</script>
