#pragma once

#include <vector>
#include "POI.h"

class DatasetRepository
{
public:
    std::vector<POI> getAllPOIs() const;
};