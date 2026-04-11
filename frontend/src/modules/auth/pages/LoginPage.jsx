import { useNavigate } from "react-router-dom";
import PageShell from "../../../components/PageShell";
import "../styles/login.css";

export default function LoginPage() {
  const navigate = useNavigate();

  return (
    <PageShell className="login-page">
      <div className="login-hero">
        <div className="background-grid"></div>
        <div className="background-glow glow-1"></div>
        <div className="background-glow glow-2"></div>

        <header className="hero-nav">
          <div className="brand-text">
            <div className="brand-name">Private Location Services</div>
            <div className="brand-subtitle">Prototype Platform</div>
          </div>
        </header>

        <main className="hero-content">
          <section className="hero-left">
            <div className="globe-shell">
              <div className="globe-core"></div>

              <div className="globe-ring outer-ring"></div>
              <div className="globe-ring ring-a"></div>
              <div className="globe-ring ring-b"></div>
              <div className="globe-ring ring-c"></div>
              <div className="globe-ring ring-d"></div>
              <div className="globe-ring ring-e"></div>

              <div className="latitude lat-1"></div>
              <div className="latitude lat-2"></div>
              <div className="latitude lat-3"></div>

              <div className="longitude lon-1"></div>
              <div className="longitude lon-2"></div>
              <div className="longitude lon-3"></div>

              <div className="orbit orbit-1"></div>
              <div className="orbit orbit-2"></div>
              <div className="orbit orbit-3"></div>

              <div className="node node-1"></div>
              <div className="node node-2"></div>
              <div className="node node-3"></div>
              <div className="node node-4"></div>
              <div className="node node-5"></div>
              <div className="node node-6"></div>

              <div className="arc arc-1"></div>
              <div className="arc arc-2"></div>
              <div className="arc arc-3"></div>
            </div>
          </section>

          <section className="hero-right">
            <p className="eyebrow">Privacy-preserving location services</p>
            <h1>Find me if you can</h1>
            <p className="minimal-subtitle">
              Secure, modular, location-aware services.
            </p>

            <div className="hero-tags">
              <span>POI Search</span>
              <span>Location Sharing</span>
              <span>Encrypted Queries</span>
            </div>

            <button className="primary-btn login-btn" onClick={() => navigate("/home")}>
              Log in
            </button>
          </section>
        </main>
      </div>
    </PageShell>
  );
}