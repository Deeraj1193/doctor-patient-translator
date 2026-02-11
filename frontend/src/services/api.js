import axios from "axios";

const API_BASE = "http://127.0.0.1:8000"; // change after deployment

export const createSession = async () => {
  const res = await axios.post(`${API_BASE}/sessions/`);
  return res.data;
};

export const sendMessage = async (payload) => {
  const res = await axios.post(`${API_BASE}/messages/`, payload);
  return res.data;
};

export const getSummary = async (sessionId) => {
  const res = await axios.post(`${API_BASE}/summary/${sessionId}`);
  return res.data;
};
