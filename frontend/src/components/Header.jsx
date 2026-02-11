import { useEffect, useState } from "react";

export default function Header() {
  const [time, setTime] = useState("");

  useEffect(() => {
    const interval = setInterval(() => {
      const now = new Date();
      setTime(
        now.toLocaleDateString() +
          " | " +
          now.toLocaleTimeString()
      );
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <header className="header">
      <div className="header-title">
        Doctor–Patient AI Translator
      </div>
      <div className="header-time">{time}</div>
    </header>
  );
}
