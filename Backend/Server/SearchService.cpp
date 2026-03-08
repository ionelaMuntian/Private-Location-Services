#include "SearchService.h"
#include <algorithm>
#include <cctype>

static std::string toLowerCopy(const std::string& text)
{
    std::string result = text;
    std::transform(result.begin(), result.end(), result.begin(),
        [](unsigned char c) { return static_cast<char>(std::tolower(c)); });
    return result;
}

std::vector<POI> SearchService::searchByText(const std::string& query) const
{
    std::vector<POI> all = repository.getAllPOIs();
    std::vector<POI> results;

    std::string q = toLowerCopy(query);

    for (const auto& poi : all)
    {
        std::string name = toLowerCopy(poi.name);
        std::string category = toLowerCopy(poi.category);

        if (name.find(q) != std::string::npos || category.find(q) != std::string::npos)
        {
            results.push_back(poi);
        }
    }

    return results;
}