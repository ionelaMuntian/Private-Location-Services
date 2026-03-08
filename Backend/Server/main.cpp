#include <crow.h>
#include "LocationService.h"
#include "SearchService.h"
#include "JsonUtils.h"
#include "AppConfig.h"

int main()
{
    crow::SimpleApp app;
    LocationService locationService;
    SearchService searchService;

    CROW_ROUTE(app, "/health")([]() {
        crow::response res("Backend is running");
        res.set_header("Access-Control-Allow-Origin", "http://localhost:5173");
        return res;
        });

    CROW_ROUTE(app, "/user-location")
        ([&locationService]() {
        Location location = locationService.getSimulatedUserLocation();

        crow::response res(JsonUtils::locationToJson(location));
        res.set_header("Access-Control-Allow-Origin", "http://localhost:5173");
        return res;
            });

    CROW_ROUTE(app, "/search")
        ([&searchService](const crow::request& req) {
        const char* query = req.url_params.get("query");

        if (!query)
        {
            crow::json::wvalue errorJson;
            errorJson["error"] = "Missing query parameter";

            crow::response res(400, errorJson);
            res.set_header("Access-Control-Allow-Origin", "http://localhost:5173");
            return res;
        }

        auto results = searchService.searchByText(query);

        crow::response res(JsonUtils::poiListToJson(results));
        res.set_header("Access-Control-Allow-Origin", "http://localhost:5173");
        return res;
            });

    app.port(AppConfig::SERVER_PORT).multithreaded().run();

    return 0;
}