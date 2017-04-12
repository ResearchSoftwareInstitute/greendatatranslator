# swagger_client.DefaultApi

All URIs are relative to *https://exposures.renci.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exposures_exposure_type_coordinates_get**](DefaultApi.md#exposures_exposure_type_coordinates_get) | **GET** /exposures/{exposure_type}/coordinates | Get exposure location(s) as latitude, longitude coordinates
[**exposures_exposure_type_dates_get**](DefaultApi.md#exposures_exposure_type_dates_get) | **GET** /exposures/{exposure_type}/dates | Get exposure start date and end date range for exposure type
[**exposures_exposure_type_scores_get**](DefaultApi.md#exposures_exposure_type_scores_get) | **GET** /exposures/{exposure_type}/scores | Get exposure score for a given environmental factor at exposure location(s)
[**exposures_exposure_type_values_get**](DefaultApi.md#exposures_exposure_type_values_get) | **GET** /exposures/{exposure_type}/values | Get exposure value for a given environmental factor at exposure location(s)
[**exposures_get**](DefaultApi.md#exposures_get) | **GET** /exposures | Get list of exposure types


# **exposures_exposure_type_coordinates_get**
> list[Coordinate] exposures_exposure_type_coordinates_get(exposure_type, latitude=latitude, longitude=longitude, radius=radius)

Get exposure location(s) as latitude, longitude coordinates

Returns paginated list of available latitude, longitude coordinates for given exposure_type. Optionally the user can provide a latitude, longitude coordinate with a radius in meters to discover if an exposure location is within the requested range

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exposure_type = 'exposure_type_example' # str | The name of the exposure factor (currently limited to pm25, o3).
latitude = 'latitude_example' # str | Search coordinates that match or are like 'latitude' (optional)
longitude = 'longitude_example' # str | Search coordinates that match or are like 'longitude' (optional)
radius = '0' # str | radius in meters to search within for exposure point when a coordinate is provided (optional) (default to 0)

try: 
    # Get exposure location(s) as latitude, longitude coordinates
    api_response = api_instance.exposures_exposure_type_coordinates_get(exposure_type, latitude=latitude, longitude=longitude, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_exposure_type_coordinates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exposure_type** | **str**| The name of the exposure factor (currently limited to pm25, o3). | 
 **latitude** | **str**| Search coordinates that match or are like &#39;latitude&#39; | [optional] 
 **longitude** | **str**| Search coordinates that match or are like &#39;longitude&#39; | [optional] 
 **radius** | **str**| radius in meters to search within for exposure point when a coordinate is provided | [optional] [default to 0]

### Return type

[**list[Coordinate]**](Coordinate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exposures_exposure_type_dates_get**
> DateRange exposures_exposure_type_dates_get(exposure_type)

Get exposure start date and end date range for exposure type

Returns exposure start date and end date range for given exposure type

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exposure_type = 'exposure_type_example' # str | The name of the exposure factor (currently limited to pm25, o3).

try: 
    # Get exposure start date and end date range for exposure type
    api_response = api_instance.exposures_exposure_type_dates_get(exposure_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_exposure_type_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exposure_type** | **str**| The name of the exposure factor (currently limited to pm25, o3). | 

### Return type

[**DateRange**](DateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exposures_exposure_type_scores_get**
> list[Exposure] exposures_exposure_type_scores_get(exposure_type, start_date, end_date, exposure_point, temporal_resolution=temporal_resolution, score_type=score_type)

Get exposure score for a given environmental factor at exposure location(s)

Retrieve the computed exposure score(s) for a given environmental exposure factor, time period, and location(s)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exposure_type = 'exposure_type_example' # str | The name of the exposure factor (currently limited to pm25, o3).
start_date = '2010-01-01' # date | The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored. (default to 2010-01-01)
end_date = '2010-01-05' # date | The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored. (default to 2010-01-05)
exposure_point = '35.9131996,-79.0558445' # str | A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.720278,-79.176389') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.720278,-79.176389,Sa0813;35.720278,-79.176389,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.720278,-79.176389,0614,35.731944,-78.852778,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.720278,-79.176389,Sa,35.731944,-78.852778,Su'). (default to 35.9131996,-79.0558445)
temporal_resolution = 'day' # str | The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day' (optional) (default to day)
score_type = '7dayrisk' # str | The exposure score type to return. The accepted values vary by exposure factor. For pm25 values are '7dayrisk', '14dayrisk' (NOT COMPLETE) (optional) (default to 7dayrisk)

try: 
    # Get exposure score for a given environmental factor at exposure location(s)
    api_response = api_instance.exposures_exposure_type_scores_get(exposure_type, start_date, end_date, exposure_point, temporal_resolution=temporal_resolution, score_type=score_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_exposure_type_scores_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exposure_type** | **str**| The name of the exposure factor (currently limited to pm25, o3). | 
 **start_date** | **date**| The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored. | [default to 2010-01-01]
 **end_date** | **date**| The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored. | [default to 2010-01-05]
 **exposure_point** | **str**| A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example &#39;35.720278,-79.176389&#39;) or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example &#39;35.720278,-79.176389,Sa0813;35.720278,-79.176389,other&#39;) indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example &#39;35.720278,-79.176389,0614,35.731944,-78.852778,1424&#39;) gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example &#39;35.720278,-79.176389,Sa,35.731944,-78.852778,Su&#39;). | [default to 35.9131996,-79.0558445]
 **temporal_resolution** | **str**| The temporal resolution to use for results, should be one of &#39;hour&#39; or &#39;day&#39;. Default is &#39;day&#39; | [optional] [default to day]
 **score_type** | **str**| The exposure score type to return. The accepted values vary by exposure factor. For pm25 values are &#39;7dayrisk&#39;, &#39;14dayrisk&#39; (NOT COMPLETE) | [optional] [default to 7dayrisk]

### Return type

[**list[Exposure]**](Exposure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exposures_exposure_type_values_get**
> list[Exposure] exposures_exposure_type_values_get(exposure_type, start_date, end_date, exposure_point, temporal_resolution=temporal_resolution, statistical_type=statistical_type)

Get exposure value for a given environmental factor at exposure location(s)

Retrieve the computed exposure value(s) for a given environmental exposure factor, time period, and location(s)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exposure_type = 'exposure_type_example' # str | The name of the exposure factor (currently limited to pm25, o3).
start_date = '2010-01-01' # date | The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored. (default to 2010-01-01)
end_date = '2010-01-05' # date | The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored. (default to 2010-01-05)
exposure_point = '35.9131996,-79.0558445' # str | A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.720278,-79.176389') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.720278,-79.176389,Sa0813;35.720278,-79.176389,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.720278,-79.176389,0614,35.731944,-78.852778,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.720278,-79.176389,Sa,35.731944,-78.852778,Su'). (default to 35.9131996,-79.0558445)
temporal_resolution = 'day' # str | The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day' (optional) (default to day)
statistical_type = 'max' # str | The statistic to use for results, should be one of 'max', 'mean', or 'median'. Default is 'max' (optional) (default to max)

try: 
    # Get exposure value for a given environmental factor at exposure location(s)
    api_response = api_instance.exposures_exposure_type_values_get(exposure_type, start_date, end_date, exposure_point, temporal_resolution=temporal_resolution, statistical_type=statistical_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_exposure_type_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exposure_type** | **str**| The name of the exposure factor (currently limited to pm25, o3). | 
 **start_date** | **date**| The starting date to obtain exposures for (example 1985-04-12 is April 12th 1985). Currently time of day is ignored. | [default to 2010-01-01]
 **end_date** | **date**| The ending date to obtain exposures for (example 1985-04-13 is April 13th 1985). Currently time of day is ignored. | [default to 2010-01-05]
 **exposure_point** | **str**| A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example &#39;35.720278,-79.176389&#39;) or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example &#39;35.720278,-79.176389,Sa0813;35.720278,-79.176389,other&#39;) indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example &#39;35.720278,-79.176389,0614,35.731944,-78.852778,1424&#39;) gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example &#39;35.720278,-79.176389,Sa,35.731944,-78.852778,Su&#39;). | [default to 35.9131996,-79.0558445]
 **temporal_resolution** | **str**| The temporal resolution to use for results, should be one of &#39;hour&#39; or &#39;day&#39;. Default is &#39;day&#39; | [optional] [default to day]
 **statistical_type** | **str**| The statistic to use for results, should be one of &#39;max&#39;, &#39;mean&#39;, or &#39;median&#39;. Default is &#39;max&#39; | [optional] [default to max]

### Return type

[**list[Exposure]**](Exposure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exposures_get**
> list[ExposureType] exposures_get()

Get list of exposure types

Returns a list of all available exposure types

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Get list of exposure types
    api_response = api_instance.exposures_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExposureType]**](ExposureType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

