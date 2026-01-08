import axios from 'axios';

// Vite uses import.meta.env for environment variables
// We will set VITE_API_URL in Render later
const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

export default axios.create({
    baseURL: BASE_URL
});