export default function ChatWindow({ messages }) {
  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={`chat-row ${
            msg.role === "doctor" ? "right" : "left"
          }`}
        >
          <div className="chat-bubble">
            <div className="bubble-original">
              {msg.original_text}
            </div>

            {msg.translated_text && (
              <div className="bubble-translation">
                {msg.translated_text}
              </div>
            )}

            {msg.audio_path && (
              <audio controls src={`http://127.0.0.1:8000/${msg.audio_path}`} />
            )}

            <div className="bubble-time">
              {new Date(msg.created_at).toLocaleTimeString()}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
