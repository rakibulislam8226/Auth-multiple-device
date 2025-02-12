import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/v1';

export default {
  async login(username, password) {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    localStorage.setItem('accessToken', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh);
    return response.data;
  },
  
  async refreshToken() {
    const refreshToken = localStorage.getItem('refreshToken');
    if (!refreshToken) return null;

    const response = await axios.post(`${API_URL}/refresh`, { refresh: refreshToken });
    localStorage.setItem('accessToken', response.data.access);
    return response.data;
  },

  logout() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  },

  getToken() {
    return localStorage.getItem('accessToken');
  }
};
