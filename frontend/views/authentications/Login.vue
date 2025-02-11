<template>
    <div>
        <h2>Login</h2>
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button @click="login">Login</button>
    </div>
</template>

<script>
import auth from "../../services/api"

export default {
    data() {
        return { username: "", password: "" };
    },
    methods: {
        async login() {
            try {
                await auth.login(this.username, this.password);
                this.$router.push('/register');
            } catch (error) {
                console.error("Login failed", error);
            }
        }
    }
};
</script>