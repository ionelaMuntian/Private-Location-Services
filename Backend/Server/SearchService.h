#pragma once

#include <string>
#include <vector>
#include "POI.h"
#include "DatasetRepository.h"

class SearchService
{
public:
    std::vector<POI> searchByText(const std::string& query) const;

private:
    DatasetRepository repository;
};