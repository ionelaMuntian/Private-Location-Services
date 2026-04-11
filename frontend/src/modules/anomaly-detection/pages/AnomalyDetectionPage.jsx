import { useNavigate } from "react-router-dom";
import PageShell from "../../../components/PageShell";

export default function AnomalyDetectionPage() {
  const navigate = useNavigate();

  return (
    <PageShell>
      <div className="placeholder-page">
        <h1>Impossible Travel Detection</h1>
        <p>This module will be added next.</p>
        <button className="secondary-btn" onClick={() => navigate("/home")}>
          Back to dashboard
        </button>
      </div>
    </PageShell>
  );
}