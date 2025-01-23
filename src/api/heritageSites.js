import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const fetchHeritageSites = async () => {
    const response = await axios.get(`${API_BASE_URL}/sites/`);
    return response.data;
};

export const addHeritageSite = async (siteData) => {
    const response = await axios.post(`${API_BASE_URL}/sites/`, siteData);
    return response.data;
};
