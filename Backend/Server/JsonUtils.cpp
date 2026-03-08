#include "JsonUtils.h"

namespace JsonUtils
{
    crow::json::wvalue locationToJson(const Location& location)
    {
        crow::json::wvalue json;
        json["lat"] = location.lat;
        json["lon"] = location.lon;
        return json;
    }

    crow::json::wvalue poiToJson(const POI& poi)
    {
        crow::json::wvalue json;
        json["id"] = static_cast<double>(poi.id);
        json["name"] = poi.name;
        json["category"] = poi.category;
        json["lat"] = poi.lat;
        json["lon"] = poi.lon;
        return json;
    }

    crow::json::wvalue poiListToJson(const std::vector<POI>& pois)
    {
        crow::json::wvalue json;

        for (size_t i = 0; i < pois.size(); ++i)
        {
            json[i] = poiToJson(pois[i]);
        }

        return json;
    }
}