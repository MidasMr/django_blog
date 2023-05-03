import {createRouter, createWebHistory} from "vue-router";


import Login from '../components/Login'
import Register from "../components/Register.vue";
import Posts from '../components/Posts'
import PostCreate from '../components/PostCreate'
import PostDetail from '../components/PostDetail'
import Profile from '../components/Profile'


const routes = [
    { path: '/', redirect: '/posts' },
    { path: '/posts', component: Posts },
    { path: '/posts/:id', name: 'PostDetail', component: PostDetail },
    { path: '/profile', name: 'Profile', component: Profile},
    { path: '/profile/:username', name: 'AuthorProfile', component: Profile},
    { path: '/login', name: 'Login', component: Login},
    { path: '/posts/create', name: 'PostCreate', component: PostCreate},
    { path: '/register', name: 'Register', component: Register}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    const publicPages = ['/login', '/register', '/posts'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    if (authRequired && !loggedIn) {
      next('/login');
    } else {
      next();
    }
});

export default router;