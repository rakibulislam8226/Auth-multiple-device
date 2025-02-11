import { defineConfig } from "vite";
import { djangoVitePlugin } from "django-vite-plugin";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
  plugins: [
    djangoVitePlugin([
      "frontend/main.js",
    ]),
    vue(),
  ],
  resolve: {
    alias: {
      vue: "vue/dist/vue.esm-bundler.js",
      "@": "/frontend",
    },
  },
});
