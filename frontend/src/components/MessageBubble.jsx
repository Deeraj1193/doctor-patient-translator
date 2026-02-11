export default function MessageBubble({ message }) {
  return (
    <div className={`message-row ${message.role}`}>
      <div className="message-bubble">
        {message.original_text && (
          <div className="original">{message.original_text}</div>
        )}

        {message.translated_text && (
          <div className="translated">{message.translated_text}</div>
        )}

        {message.audio_path && (
          <audio controls src={`http://127.0.0.1:8000/${message.audio_path}`} />
        )}

        <div className="timestamp">
          {new Date(message.created_at).toLocaleTimeString()}
        </div>
      </div>
    </div>
  );
}
