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
      minHeight: "100vh",
      width: "100vw",
      background: "linear-gradient(135deg, #7b2ff2 0%, #f357a8 100%)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontFamily: "Inter, Arial, sans-serif",
    }}>
      <div style={{
        background: "#fff",
        borderRadius: 18,
        boxShadow: "0 8px 32px rgba(80,0,120,0.18)",
        maxWidth: 420,
        width: "100%",
        padding: 40,
        margin: 16,
        textAlign: "center",
      }}>
        <h2 style={{ color: "#7b2ff2", marginBottom: 24 }}>Convite — Previsão de Receita</h2>
        <div style={{ marginBottom: 20 }}>
          <label style={{ fontWeight: 600 }}>
            País:&nbsp;
            <select
              value={country}
              onChange={e => setCountry(e.target.value)}
              style={{
                padding: 8, borderRadius: 6, border: "1px solid #ccc",
                minWidth: 120, fontSize: 16
              }}
            >
              <option value="USA">USA</option>
              <option value="EIRE">EIRE</option>
              <option value="Germany">Germany</option>
              <option value="Singapore">Singapore</option>
            </select>
          </label>
        </div>
        <div style={{ marginBottom: 20 }}>
          <label style={{ fontWeight: 600 }}>
            Data:&nbsp;
            <input
              type="date"
              value={date}
              onChange={e => setDate(e.target.value)}
              style={{
                padding: 8, borderRadius: 6, border: "1px solid #ccc",
                fontSize: 16
              }}
            />
          </label>
        </div>
        <button
          onClick={handlePredict}
          disabled={loading || !date}
          style={{
            width: "100%", padding: 12, borderRadius: 8,
            background: loading ? "#b39ddb" : "#7b2ff2",
            color: "#fff", border: "none", fontWeight: 700,
            fontSize: 18, cursor: loading || !date ? "not-allowed" : "pointer",
            boxShadow: "0 2px 8px #e1bee7",
            transition: "background 0.2s"
          }}
        >
          {loading ? "Consultando..." : "Prever"}
        </button>
        {result && (
          <div style={{
            marginTop: 32, background: "#f6f8fa", borderRadius: 12,
            padding: 22, fontSize: 18, textAlign: "center", color: "#333",
            boxShadow: "0 1px 4px #eee"
          }}>
            {result.error ? (
              <span style={{ color: "#c00" }}>Erro: {result.error}</span>
            ) : (
              <>
                <div><strong>País:</strong> {result.country}</div>
                <div><strong>Data:</strong> {result.target_date}</div>
                <div style={{ fontSize: 22, color: "#7b2ff2", marginTop: 12 }}>
                  <strong>Receita prevista:</strong> R$ {result.predicted_revenue.toLocaleString("pt-BR")}
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
