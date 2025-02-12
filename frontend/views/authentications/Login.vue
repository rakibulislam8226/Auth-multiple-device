<template>
    <div>
        <h2>Login</h2>
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button @click="login">Login</button>
    </div>
</template>

<script>
import auth from "../../services/api";
import iziToast from "izitoast";

export default {
    data() {
        return { username: "", password: "" };
    },
    methods: {
        async login() {
            try {
                await auth.login(this.username, this.password);
                iziToast.success({ title: "Success", message: "Login successful" });
                this.$router.push('/profile');
            } catch (error) {
                console.error("Login failed", error);
            }
        }
    }
};
</script>