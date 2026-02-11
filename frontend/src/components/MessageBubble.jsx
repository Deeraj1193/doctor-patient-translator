export default function MessageBubble({ message }) {
  return (
    <div className={`message-row ${message.role}`}>
      <div className="message-bubble">
        <div className="original">{message.original_text}</div>
        <div className="translated">{message.translated_text}</div>
        <div className="timestamp">
          {new Date(message.created_at).toLocaleTimeString()}
        </div>
      </div>
    </div>
  );
}
