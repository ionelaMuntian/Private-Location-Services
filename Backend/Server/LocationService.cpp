#include "LocationService.h"
#include "AppConfig.h"

Location LocationService::getSimulatedUserLocation() const
{
    return Location{ AppConfig::SIMULATED_USER_LAT, AppConfig::SIMULATED_USER_LON };
}