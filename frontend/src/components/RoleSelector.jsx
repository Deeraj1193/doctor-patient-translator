export default function RoleSelector({ role, setRole }) {
  return (
    <div className="role-selector">
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
  );
}
