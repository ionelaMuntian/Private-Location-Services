export default function UserLocationButton({ onClick }) {
  return (
    <button onClick={onClick} style={{ marginBottom: "16px" }}>
      Show My Location
    </button>
  );
}