import axios from 'axios';

console.log("Base URL:", process.env.REACT_APP_API_BASE_URL); // ✅ THIS LINE

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

export default api;
