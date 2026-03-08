const API_BASE_URL = "http://localhost:18080";

export async function fetchUserLocation() {
  const response = await fetch(`${API_BASE_URL}/user-location`);
  if (!response.ok) {
    throw new Error("Failed to fetch user location");
  }
  return response.json();
}

export async function searchLocations(query) {
  const response = await fetch(
    `${API_BASE_URL}/search?query=${encodeURIComponent(query)}`
  );
  if (!response.ok) {
    throw new Error("Failed to search locations");
  }
  return response.json();
}