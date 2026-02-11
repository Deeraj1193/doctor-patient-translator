import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

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

export const uploadAudio = async (formData) => {
  const res = await axios.post(`${API_BASE}/messages/upload-audio/`, formData);
  return res.data;
};

export const searchMessages = async (query, sessionId) => {
  const res = await axios.get(
    `${API_BASE}/search?query=${query}&session_id=${sessionId}`
  );
  return res.data;
};
