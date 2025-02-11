<template>
  <div class="empty pt-0">
    <img :src="`${$root.asset}/images/403.webp`" />
    <div class="empty-action">
      <!-- <router-link :to="{ name: 'dashboard' }" class="btn btn-primary">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="icon"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
          <path d="M5 12l14 0"></path>
          <path d="M5 12l6 6"></path>
          <path d="M5 12l6 -6"></path>
        </svg>
        GO BACK
      </router-link> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFound",

  mounted() {
    this.$eventBus.$emit("pageTitle", { title: "Forbidden" });
  },
};
</script>


<style>
:where(.theme-dark, [data-bs-theme="dark"]) .tblr-illustrations-not-found-a {
  fill: #1a2030;
}
:where(.theme-dark, [data-bs-theme="dark"]) .tblr-illustrations-not-found-b {
  fill: black;
  opacity: 0.07;
}
:where(.theme-dark, [data-bs-theme="dark"]) .tblr-illustrations-not-found-c {
  fill: #454c5e;
}
:where(.theme-dark, [data-bs-theme="dark"]) .tblr-illustrations-not-found-d {
  fill: #232b41;
}
@media (prefers-color-scheme: dark) {
  .tblr-illustrations-not-found-a {
    fill: #1a2030;
  }
  .tblr-illustrations-not-found-b {
    fill: black;
    opacity: 0.07;
  }
  .tblr-illustrations-not-found-c {
    fill: #454c5e;
  }
  .tblr-illustrations-not-found-d {
    fill: #232b41;
  }
}
</style>