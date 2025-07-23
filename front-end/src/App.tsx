import React, { useState } from "react";

function App() {
  const [country, setCountry] = useState("USA");
  const [date, setDate] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    setResult(null);
    try {
      const res = await fetch(
        `http://localhost:5000/predict?country=${country}&date=${date}`
      );
      const data = await res.json();
      setResult(data);
    } catch {
      setResult({ error: "Falha na requisição" });
    }
    setLoading(false);
  };

  return (
    <div style={{
      maxWidth: 420, margin: "80px auto", fontFamily: "sans-serif",
      padding: 32, borderRadius: 12, background: "#fff", boxShadow: "0 2px 12px #eee"
    }}>
      <h2 style={{ textAlign: "center", marginBottom: 24 }}>Convite — Previsão de Receita</h2>
      <div style={{ marginBottom: 16 }}>
        <label>País:&nbsp;
          <select value={country} onChange={e => setCountry(e.target.value)}>
            <option value="USA">USA</option>
            <option value="EIRE">EIRE</option>
            <option value="Germany">Germany</option>
            <option value="Singapore">Singapore</option>
          </select>
        </label>
      </div>
      <div style={{ marginBottom: 16 }}>
        <label>Data:&nbsp;
          <input type="date" value={date} onChange={e => setDate(e.target.value)} />
        </label>
      </div>
      <button
        onClick={handlePredict}
        disabled={loading || !date}
        style={{
          width: "100%", padding: 10, borderRadius: 6, background: "#1976d2",
          color: "#fff", border: "none", fontWeight: 600, cursor: loading ? "not-allowed" : "pointer"
        }}
      >
        {loading ? "Consultando..." : "Prever"}
      </button>
      {result && (
        <div style={{
          marginTop: 32, background: "#f6f8fa", borderRadius: 8,
          padding: 18, fontSize: 18, textAlign: "center"
        }}>
          {result.error ? (
            <span style={{ color: "#c00" }}>Erro: {result.error}</span>
          ) : (
            <>
              <div><strong>País:</strong> {result.country}</div>
              <div><strong>Data:</strong> {result.target_date}</div>
              <div><strong>Receita prevista:</strong> R$ {result.predicted_revenue.toLocaleString("pt-BR")}</div>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
