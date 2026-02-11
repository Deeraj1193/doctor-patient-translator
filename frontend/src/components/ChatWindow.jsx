import { useEffect, useRef, useState } from "react";
import TopBar from "./TopBar";
import RoleSelector from "./RoleSelector";
import LanguageSelector from "./LanguageSelector";
import MessageBubble from "./MessageBubble";
import MessageInput from "./MessageInput";
import { createSession, sendMessage, getSummary } from "../services/api";

export default function ChatWindow() {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [role, setRole] = useState("doctor");
  const [language, setLanguage] = useState("Spanish");
  const chatRef = useRef(null);

  useEffect(() => {
    const initSession = async () => {
      const session = await createSession();
      setSessionId(session.id);
    };
    initSession();
  }, []);

  useEffect(() => {
    chatRef.current?.scrollTo({
      top: chatRef.current.scrollHeight,
      behavior: "smooth"
    });
  }, [messages]);

  const handleSend = async (text) => {
    const payload = {
      session_id: sessionId,
      role: role,
      original_text: text,
      source_language: role === "doctor" ? "English" : language,
      target_language: role === "doctor" ? language : "English"
    };

    const response = await sendMessage(payload);
    setMessages((prev) => [...prev, response]);
  };

  const handleSummary = async () => {
    const summary = await getSummary(sessionId);
    alert(summary.summary);
  };

  return (
    <div className="chat-card">
      <TopBar />

      <div className="controls">
        <RoleSelector role={role} setRole={setRole} />
        <LanguageSelector language={language} setLanguage={setLanguage} />
        <button className="summary-btn" onClick={handleSummary}>
          Generate Summary
        </button>
      </div>

      <div className="chat-body" ref={chatRef}>
        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} />
        ))}
      </div>

      <MessageInput onSend={handleSend} />
    </div>
  );
}
