import { useNavigate } from "react-router-dom";

export default function ServiceCard({ title, description, route, status }) {
  const navigate = useNavigate();

  return (
    <div className="service-card">
      <div className="service-card-top">
        <span className={`status-badge ${status?.toLowerCase() || "planned"}`}>
          {status || "Planned"}
        </span>
      </div>

      <h3>{title}</h3>
      <p>{description}</p>

      <button className="primary-btn" onClick={() => navigate(route)}>
        Open service
      </button>
    </div>
  );
}