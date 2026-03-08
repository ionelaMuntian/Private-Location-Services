import { useState } from "react";
import MapView from "./components/MapView";
import SearchBar from "./components/SearchBar";
import UserLocationButton from "./components/UserLocationButton";
import { fetchUserLocation, searchLocations } from "./services/api";

function App() {
  const [userLocation, setUserLocation] = useState(null);
  const [results, setResults] = useState([]);

  const handleShowUserLocation = async () => {
    try {
      const location = await fetchUserLocation();
      console.log("User location:", location);
      setUserLocation(location);
    } catch (error) {
      console.error(error);
      alert("Failed to load user location");
    }
  };

  const handleSearch = async (query) => {
    try {
      const data = await searchLocations(query);
      console.log("Search query:", query);
      console.log("Search results:", data);

      const safeResults = Array.isArray(data) ? data : [];
      setResults(safeResults);
    } catch (error) {
      console.error(error);
      alert("Failed to search locations");
      setResults([]);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Private Location Frontend</h1>
      <SearchBar onSearch={handleSearch} />
      <UserLocationButton onClick={handleShowUserLocation} />
      <p>Results count: {results ? results.length : 0}</p>
      <MapView userLocation={userLocation} results={results || []} />
    </div>
  );
}

export default App;