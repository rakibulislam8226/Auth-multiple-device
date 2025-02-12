<template>
  <section class="bg-gray-100 dark:bg-gray-900">
    <div
      class="flex flex-col items-center justify-center px-6 py-3 mx-auto md:h-screen lg:py-0"
    >
      <a
        href="#"
        class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
      >
        <img
          class="w-8 h-8 mr-2"
          src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
          alt="logo"
        />
        DUTTOS
      </a>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Sign in to your account
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="login">
            <div>
              <label
                for="username"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your Username</label
              >
              <input
                type="username"
                id="username"
                v-model="username"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="name@company.com"
              />
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Password</label
              >
              <input
                type="password"
                id="password"
                v-model="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              />
            </div>
            <div class="flex items-end justify-between">
              <button
                href="#"
                class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"
              >
                Forgot password?
              </button>
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-600 hover:bg-blue-900 rounded-lg text-sm sm:w-auto px-5 py-2.5 text-center"
            >
              Sign in
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Don’t have an account yet? <a href="#" class="">Sign up</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
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
        iziToast.success({ message: "Login successful" });
        this.$router.push("/profile");
      } catch (error) {
        // render error message from the server
        let message = "Login failed";
        if (error.response && error.response.data) {
          message =
            error.response.data.message || JSON.stringify(error.response.data);
        }
        iziToast.error({ message });
      }
    },
  },
};
</script>
