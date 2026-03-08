#include "DatasetRepository.h"
#include "AppConfig.h"

#include <tinyxml2.h>
#include <string>
#include <vector>

using namespace tinyxml2;

std::vector<POI> DatasetRepository::getAllPOIs() const
{
    std::vector<POI> pois;

    XMLDocument doc;
    if (doc.LoadFile(AppConfig::OSM_FILE_PATH) != XML_SUCCESS)
    {
        return pois;
    }

    XMLElement* root = doc.FirstChildElement("osm");
    if (!root)
    {
        return pois;
    }

    for (XMLElement* node = root->FirstChildElement("node");
        node != nullptr;
        node = node->NextSiblingElement("node"))
    {
        long long id = 0;
        double lat = 0.0;
        double lon = 0.0;

        node->QueryInt64Attribute("id", &id);
        node->QueryDoubleAttribute("lat", &lat);
        node->QueryDoubleAttribute("lon", &lon);

        std::string name;
        std::string category;
        bool relevant = false;

        for (XMLElement* tag = node->FirstChildElement("tag");
            tag != nullptr;
            tag = tag->NextSiblingElement("tag"))
        {
            const char* k = tag->Attribute("k");
            const char* v = tag->Attribute("v");

            if (!k || !v)
            {
                continue;
            }

            std::string key = k;
            std::string value = v;

            if (key == "name")
            {
                name = value;
            }

            if (key == "amenity")
            {
                if (value == "hospital" || value == "pharmacy")
                {
                    category = value;
                    relevant = true;
                }
            }

            if (key == "place")
            {
                if (value == "city" || value == "town" || value == "village")
                {
                    category = value;
                    relevant = true;
                }
            }
        }

        if (relevant && !name.empty())
        {
            pois.push_back(POI{ id, name, category, lat, lon });
        }
    }


    return pois;
}