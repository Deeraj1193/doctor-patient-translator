import { useState, useRef } from "react";

export default function MessageInput({ onSend, onAudioSend }) {
  const [text, setText] = useState("");
  const [isRecording, setIsRecording] = useState(false);

  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);
  const streamRef = useRef(null);

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  const toggleRecording = async () => {
    // START RECORDING
    if (!isRecording) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        streamRef.current = stream;

        const recorder = new MediaRecorder(stream);
        mediaRecorderRef.current = recorder;
        chunksRef.current = [];

        recorder.ondataavailable = (e) => {
          if (e.data.size > 0) {
            chunksRef.current.push(e.data);
          }
        };

        recorder.onstop = async () => {
          const blob = new Blob(chunksRef.current, { type: "audio/webm" });

          // STOP microphone properly
          streamRef.current.getTracks().forEach(track => track.stop());

          if (blob.size > 0) {
            onAudioSend(blob);
          }

          setIsRecording(false);
        };

        recorder.start();
        setIsRecording(true);

      } catch (err) {
        console.error("Microphone error:", err);
      }
    }

    // STOP RECORDING
    else {
      mediaRecorderRef.current.stop();
    }
  };

  return (
    <div className="input-container">
      <input
        type="text"
        placeholder="Type your message..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />

      <button className="send-btn" onClick={handleSend}>
        Send
      </button>

      <button
        className={`mic-btn ${isRecording ? "recording" : ""}`}
        onClick={toggleRecording}
      >
        {isRecording ? "■" : "🎤"}
      </button>
    </div>
  );
}
