export default function SummaryModal({ summary, onClose }) {
  if (!summary) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-card">
        <div className="modal-header">
          <h2>Conversation Summary</h2>
          <button className="modal-close" onClick={onClose}>×</button>
        </div>

        <div className="modal-body">
          {summary}
        </div>
      </div>
    </div>
  );
}
