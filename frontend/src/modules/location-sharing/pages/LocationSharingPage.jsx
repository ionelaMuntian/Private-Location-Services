import { useNavigate } from "react-router-dom";
import PageShell from "../../../components/PageShell";

export default function LocationSharingPage() {
  const navigate = useNavigate();

  return (
    <PageShell>
      <div className="placeholder-page">
        <h1>Location Sharing</h1>
        <p>This module will be added next.</p>
        <button className="secondary-btn" onClick={() => navigate("/home")}>
          Back to dashboard
        </button>
      </div>
    </PageShell>
  );
}