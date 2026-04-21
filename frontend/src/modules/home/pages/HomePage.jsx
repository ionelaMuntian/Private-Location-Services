import { useNavigate } from "react-router-dom";
import PageShell from "../../../components/PageShell";
import ServiceCard from "../../../components/ServiceCard";
import "../styles/home.css";

export default function HomePage() {
  const navigate = useNavigate();

  return (
    <PageShell className="home-page">
      <header className="topbar">
        <div>
          <p className="eyebrow">Trusted Client Dashboard</p>
          <h1>Choose a service</h1>
        </div>

        <button className="secondary-btn" onClick={() => navigate("/login")}>
          Sign out
        </button>
      </header>

      <section className="hero-banner">
        <div>
          <h2>Privacy-Preserving Location-Based Services</h2>
          <p>
            Select one of the available modules to continue. Each service is
            designed as an independent feature, making the frontend easy to
            extend and maintain.
          </p>
        </div>
      </section>

      <section className="services-grid">
        <ServiceCard
          title="Nearest Points of Interest"
          description="Search for the nearest hospitals, pharmacies, or other points of interest using plaintext, CKKS, or Concrete query flows."
          route="/poi-search"
          status="Ready"
        />

        <ServiceCard
          title="Location Sharing"
          description="Share and compare protected locations between users while preserving privacy through secure computation."
          route="/location-sharing"
          status="Planned"
        />

        <ServiceCard
          title="Impossible Travel Detection"
          description="Inspect suspicious travel patterns and anomaly scenarios while minimizing direct exposure of sensitive location history."
          route="/anomaly-detection"
          status="Planned"
        />
      </section>
    </PageShell>
  );
}