import { useEffect, useState } from "react";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import SummaryModal from "./components/SummaryModal";
import "./App.css";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [role, setRole] = useState("doctor");
  const [language, setLanguage] = useState("Spanish");
  const [summary, setSummary] = useState("");
  const [search, setSearch] = useState("");

  const fetchMessages = async () => {
    const res = await fetch("http://127.0.0.1:8000/messages/1");
    const data = await res.json();
    setMessages(data);
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  const sendMessage = async (text) => {
    await fetch("http://127.0.0.1:8000/messages/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: 1,
        role,
        original_text: text,
        source_language: "English",
        target_language: language,
      }),
    });

    fetchMessages();
  };

  const sendAudio = async (blob) => {
    const formData = new FormData();
    formData.append("file", blob);
    formData.append("session_id", 1);
    formData.append("role", role);
    formData.append("source_language", "English");
    formData.append("target_language", language);

    await fetch("http://127.0.0.1:8000/messages/audio", {
      method: "POST",
      body: formData,
    });

    fetchMessages();
  };

  const generateSummary = async () => {
    const res = await fetch("http://127.0.0.1:8000/summary/1");
    const data = await res.json();
    setSummary(data.summary);
  };

  const filteredMessages = messages.filter((msg) =>
    msg.original_text.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <Header />

      <div className="controls">
        <input
          className="search-input"
          placeholder="Search conversation..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <div className="toggle-group">
          <button
            className={role === "doctor" ? "active" : ""}
            onClick={() => setRole("doctor")}
          >
            Doctor
          </button>

          <button
            className={role === "patient" ? "active" : ""}
            onClick={() => setRole("patient")}
          >
            Patient
          </button>
        </div>

        <select
          className="language-select"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        >
          <option>Spanish</option>
          <option>French</option>
          <option>German</option>
        </select>

        <button className="summary-btn" onClick={generateSummary}>
          Generate Summary
        </button>
      </div>

      <ChatWindow messages={filteredMessages} />

      <MessageInput onSend={sendMessage} onAudioSend={sendAudio} />

      <SummaryModal summary={summary} onClose={() => setSummary("")} />
    </>
  );
}
