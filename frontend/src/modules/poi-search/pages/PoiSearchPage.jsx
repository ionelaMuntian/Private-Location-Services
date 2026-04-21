import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import PageShell from "../../../components/PageShell";
import "../styles/poi-search.css";

const API_URL = "http://127.0.0.1:8000/client/poi/nearest-k";

const initialForm = {
  category: "bank",
  k: 2,
  latitude_m: 5741384.185332346,
  longitude_m: 2362254.8313645967,
  scheme: "plaintext",
};

export default function PoiSearchPage() {
  const navigate = useNavigate();

  const [form, setForm] = useState(initialForm);
  const [results, setResults] = useState([]);
  const [responseMeta, setResponseMeta] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const hasResults = useMemo(() => results.length > 0, [results]);

  const handleChange = (field, value) => {
    setForm((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResults([]);
    setResponseMeta(null);

    try {
      const payload = {
        category: form.category,
        k: Number(form.k),
        latitude_m: Number(form.latitude_m),
        longitude_m: Number(form.longitude_m),
        scheme: form.scheme,
      };

      const response = await axios.post(API_URL, payload);

      setResponseMeta({
        scheme: response.data.scheme,
        category: response.data.category,
        k: response.data.k,
        resultCount: response.data.results?.length || 0,
      });

      setResults(response.data.results || []);
    } catch (err) {
      console.error(err);

      const backendMessage =
        err?.response?.data?.detail?.detail ||
        err?.response?.data?.detail ||
        err?.message ||
        "Request failed. Check that both backend services are running.";

      setError(
        typeof backendMessage === "string"
          ? backendMessage
          : JSON.stringify(backendMessage)
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <PageShell className="poi-page">
      <div className="poi-background-grid"></div>
      <div className="poi-background-glow glow-left"></div>
      <div className="poi-background-glow glow-right"></div>

      <div className="poi-container">
        <header className="poi-topbar">
          <div>
            <p className="poi-eyebrow">Nearest Points of Interest</p>
            <h1>Search nearby services</h1>
            <p className="poi-subtitle">
              Query nearby categories using plaintext, CKKS, or Concrete through
              the trusted client.
            </p>
          </div>

          <button className="secondary-btn" onClick={() => navigate("/home")}>
            Back to dashboard
          </button>
        </header>

        <section className="poi-hero">
          <div className="poi-hero-copy">
            <div className="poi-hero-badge">Module 1</div>
            <h2>Nearest POI retrieval</h2>
            <p>
              Choose a category, set the number of nearest results, and submit a
              location query through the trusted client.
            </p>

            <div className="poi-tags">
              <span>Trusted Client</span>
              <span>POI Search</span>
              <span>Plaintext / CKKS / Concrete</span>
            </div>
          </div>

          <div className="poi-orb">
            <div className="poi-orb-core"></div>
            <div className="poi-orb-ring ring-1"></div>
            <div className="poi-orb-ring ring-2"></div>
            <div className="poi-orb-ring ring-3"></div>
            <div className="poi-orb-node node-1"></div>
            <div className="poi-orb-node node-2"></div>
            <div className="poi-orb-node node-3"></div>
            <div className="poi-orb-node node-4"></div>
          </div>
        </section>

        <div className="poi-content-grid">
          <section className="poi-card poi-form-card">
            <div className="poi-card-header">
              <h3>Query form</h3>
              <p>Enter the query parameters below.</p>
            </div>

            <form onSubmit={handleSubmit} className="poi-form">
              <label>
                Category
                <select
                  value={form.category}
                  onChange={(e) => handleChange("category", e.target.value)}
                >
                  <option value="bank">bank</option>
                  <option value="cafe">cafe</option>
                  <option value="supermarket">supermarket</option>
                  <option value="dentist">dentist</option>
                  <option value="fitness_centre">fitness_centre</option>
                  <option value="fast_food">fast_food</option>
                  <option value="pharmacy">pharmacy</option>
                </select>
              </label>

              <label>
                K
                <input
                  type="number"
                  min="1"
                  max="50"
                  value={form.k}
                  onChange={(e) => handleChange("k", e.target.value)}
                />
              </label>

              <label>
                Latitude M
                <input
                  type="number"
                  step="any"
                  value={form.latitude_m}
                  onChange={(e) => handleChange("latitude_m", e.target.value)}
                />
              </label>

              <label>
                Longitude M
                <input
                  type="number"
                  step="any"
                  value={form.longitude_m}
                  onChange={(e) => handleChange("longitude_m", e.target.value)}
                />
              </label>

              <label className="full-width">
                Scheme
                <select
                  value={form.scheme}
                  onChange={(e) => handleChange("scheme", e.target.value)}
                >
                  <option value="plaintext">plaintext</option>
                  <option value="ckks">ckks</option>
                  <option value="concrete">concrete</option>
                </select>
              </label>

              {form.scheme === "concrete" && (
                <div className="full-width poi-alert">
                  Concrete mode may be slower because the trusted client and
                  service provider exchange encrypted artifacts for each query.
                </div>
              )}

              <div className="full-width poi-form-actions">
                <button className="primary-btn" type="submit" disabled={loading}>
                  {loading ? "Searching..." : "Search nearest POIs"}
                </button>
              </div>
            </form>

            {error && <div className="poi-alert poi-alert-error">{error}</div>}
          </section>

          <section className="poi-card poi-results-card">
            <div className="poi-card-header">
              <h3>Results</h3>
              <p>Returned nearest points of interest.</p>
            </div>

            {responseMeta && (
              <div className="poi-meta">
                <div className="poi-meta-item">
                  <span>Scheme</span>
                  <strong>{responseMeta.scheme}</strong>
                </div>
                <div className="poi-meta-item">
                  <span>Category</span>
                  <strong>{responseMeta.category}</strong>
                </div>
                <div className="poi-meta-item">
                  <span>K</span>
                  <strong>{responseMeta.k}</strong>
                </div>
                <div className="poi-meta-item">
                  <span>Returned</span>
                  <strong>{responseMeta.resultCount}</strong>
                </div>
              </div>
            )}

            {loading && <p className="poi-empty">Searching for nearest POIs...</p>}

            {!loading && !hasResults && !error && (
              <p className="poi-empty">No results yet. Run a query to see results.</p>
            )}

            {!loading && hasResults && (
              <div className="poi-table-wrap">
                <table className="poi-table">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Category</th>
                      <th>Latitude</th>
                      <th>Longitude</th>
                      <th>Distance (km)</th>
                    </tr>
                  </thead>
                  <tbody>
                    {results.map((poi) => (
                      <tr key={poi.id}>
                        <td>{poi.name}</td>
                        <td>{poi.category}</td>
                        <td>{poi.latitude}</td>
                        <td>{poi.longitude}</td>
                        <td>{poi.distance_km}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </section>
        </div>
      </div>
    </PageShell>
  );
}