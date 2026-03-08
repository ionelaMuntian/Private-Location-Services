import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import { useEffect } from "react";
import "leaflet/dist/leaflet.css";

function RecenterMap({ userLocation, results }) {
  const map = useMap();

  useEffect(() => {
    if (results && results.length > 0) {
      map.setView([results[0].lat, results[0].lon], 16);
    } else if (userLocation) {
      map.setView([userLocation.lat, userLocation.lon], 16);
    }
  }, [map, userLocation, results]);

  return null;
}

export default function MapView({ userLocation, results }) {
  const safeResults = Array.isArray(results) ? results : [];
  const center = [46.7712, 23.6236];

  return (
    <MapContainer center={center} zoom={13} style={{ height: "600px", width: "100%" }}>
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <RecenterMap userLocation={userLocation} results={safeResults} />

      {userLocation && (
        <Marker position={[userLocation.lat, userLocation.lon]}>
          <Popup>Your simulated location</Popup>
        </Marker>
      )}

      {safeResults.map((poi, index) => (
        <Marker key={`${poi.id}-${index}`} position={[poi.lat, poi.lon]}>
          <Popup>
            <strong>{poi.name}</strong>
            <br />
            {poi.category}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}