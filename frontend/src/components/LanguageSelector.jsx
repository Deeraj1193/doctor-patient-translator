export default function LanguageSelector({ language, setLanguage }) {
  return (
    <select
      className="language-selector"
      value={language}
      onChange={(e) => setLanguage(e.target.value)}
    >
      <option value="English">English</option>
      <option value="Spanish">Spanish</option>
    </select>
  );
}
