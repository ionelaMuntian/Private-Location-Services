#pragma once

#include <crow.h>
#include "Location.h"
#include "POI.h"

namespace JsonUtils
{
    crow::json::wvalue locationToJson(const Location& location);
    crow::json::wvalue poiToJson(const POI& poi);
    crow::json::wvalue poiListToJson(const std::vector<POI>& pois);
}