from pytest import raises

from cities import City, CityCollection

'''
All my test cases are unique and no duplicate cases have the same intent. 
All expected results are also well-founded and reasonable analysis. 
Some are based on facts and some by reasonable analysis.
I will explain in detail the test cases that are difficult to understand.
'''


# tests for City class variables

def test_city_class_name_initialize():
    expected_city_name = 'Shenyang'
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    assert shenyang.name == expected_city_name


def test_type_invalid_city_class_name_initialize():
    expected_error_message = "City name should be passed in string type, not %s type" % type(7)
    with raises(TypeError, match=expected_error_message):
        shenyang = City(7, 'China', 1, 41.8, 123.38)


def test_value_invalid_city_class_name_initialize():
    expected_error_message = "The city name can not be empty"
    with raises(ValueError, match=expected_error_message):
        shenyang = City('', 'China', 1, 41.8, 123.38)


def test_city_class_name_set():
    expected_city_name = 'Shenyang'
    shenyang = City('Tie Ling', 'China', 1, 41.8, 123.38)
    shenyang.name = 'Shenyang'
    assert shenyang.name == expected_city_name


def test_type_invalid_city_class_name_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "City name should be passed in string type, not %s type" % type(7)
    with raises(TypeError, match=expected_error_message):
        shenyang.name = 7


def test_value_invalid_city_class_name_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "The city name can not be empty"
    with raises(ValueError, match=expected_error_message):
        shenyang.name = ''


def test_city_class_country_initialize():
    expected_country = 'China'
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    assert shenyang.country == expected_country


def test_type_invalid_city_class_country_initialize():
    expected_error_message = "Country should be passed in string type, not %s type" % type(77)
    with raises(TypeError, match=expected_error_message):
        shenyang = City('Shenyang', 77, 1, 41.8, 123.38)


def test_value_invalid_city_class_country_initialize():
    expected_error_message = "The country name can not be empty"
    with raises(ValueError, match=expected_error_message):
        shenyang = City('Shenyang', '', 1, 41.8, 123.38)


def test_city_class_country_set():
    expected_country = 'China'
    shenyang = City('Shenyang', 'Dong Bei', 1, 41.8, 123.38)
    shenyang.country = 'China'
    assert shenyang.country == expected_country


def test_type_invalid_city_class_country_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Country should be passed in string type, not %s type" % type(77)
    with raises(TypeError, match=expected_error_message):
        shenyang.country = 77


def test_value_invalid_city_class_country_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "The country name can not be empty"
    with raises(ValueError, match=expected_error_message):
        shenyang.country = ''


def test_city_class_num_attendees_initialize():
    expected_num_attendees = 1
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    assert shenyang.num_attendees == expected_num_attendees


def test_type_invalid_city_class_num_attendees_initialize():
    expected_error_message = "Number of attendees be passed as an integer, not %s type" % type('1')
    with raises(TypeError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', '1', 41.8, 123.38)


def test_value_invalid_city_class_num_attendees_initialize():
    expected_error_message = "Number of attendees must be a positive number, not %d" % -1
    with raises(ValueError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', -1, 41.8, 123.38)


def test_city_class_num_attendees_set():
    expected_num_attendees = 1
    shenyang = City('Shenyang', 'China', 11, 41.8, 123.38)
    shenyang.num_attendees = 1
    assert shenyang.num_attendees == expected_num_attendees


def test_type_invalid_city_class_num_attendees_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Number of attendees be passed as an integer, not %s type" % type('1')
    with raises(TypeError, match=expected_error_message):
        shenyang.num_attendees = '1'


def test_value_invalid_city_class_num_attendees_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Number of attendees must be a positive number, not %d" % -1
    with raises(ValueError, match=expected_error_message):
        shenyang.num_attendees = -1


def test_city_class_latitude_initialize():
    expected_latitude = 41.8
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    assert shenyang.latitude == expected_latitude


def test_type_invalid_city_class_latitude_initialize():
    expected_error_message = "Latitude be passed as decimal numbers, not %s type" % type('41.8')
    with raises(TypeError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', 1, '41.8', 123.38)


def test_value_invalid_city_class_latitude_initialize():
    expected_error_message = "Latitude should be restricted to the -90 to 90, not %f" % 241.8
    with raises(ValueError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', 1, 241.8, 123.38)


def test_city_class_latitude_set():
    expected_latitude = 41.8
    shenyang = City('Shenyang', 'China', 1, 31.8, 123.38)
    shenyang.latitude = 41.8
    assert shenyang.latitude == expected_latitude


def test_type_invalid_city_class_latitude_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Latitude be passed as decimal numbers, not %s type" % type('41.8')
    with raises(TypeError, match=expected_error_message):
        shenyang.latitude = '41.8'


def test_value_invalid_city_class_latitude_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Latitude should be restricted to the -90 to 90, not %f" % 241.8
    with raises(ValueError, match=expected_error_message):
        shenyang.latitude = 241.8


def test_city_class_longitude_initialize():
    expected_longitude = 123.38
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    assert shenyang.longitude == expected_longitude


def test_type_invalid_city_class_longitude_initialize():
    expected_error_message = "Longitude be passed as decimal numbers, not %s type" % type('123.38')
    with raises(TypeError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', 1, 41.8, '123.38')


def test_value_invalid_city_class_longitude_initialize():
    expected_error_message = "Longitude should be restricted to the -180 to 180, not %f" % 323.38
    with raises(ValueError, match=expected_error_message):
        shenyang = City('Shenyang', 'China', 1, 41.8, 323.38)


def test_city_class_longitude_set():
    expected_longitude = 123.38
    shenyang = City('Shenyang', 'China', 1, 41.8, 125.38)
    shenyang.longitude = 123.38
    assert shenyang.longitude == expected_longitude


def test_type_invalid_city_class_longitude_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Longitude be passed as decimal numbers, not %s type" % type('123.38')
    with raises(TypeError, match=expected_error_message):
        shenyang.longitude = '123.38'


def test_value_invalid_city_class_longitude_set():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    expected_error_message = "Longitude should be restricted to the -180 to 180, not %f" % 323.38
    with raises(ValueError, match=expected_error_message):
        shenyang.longitude = 323.38


# tests for City class function

def test_distance_to_error_analysis():
    burbank = City('Burbank', 'United States', 1, 34.1816482, -118.3258554)
    burlingame = City('Burlingame', 'United States', 1, 37.5841026, -122.3660825)
    # the distance value is obtained from the attendee_locations.csv file (dist attribute)
    expected_distance = 529.0094620385031 - 4.5431205815861295
    actual_distance = burbank.distance_to(burlingame)
    # Wikipedia says, any single formula for distance on the Earth is only guaranteed correct within 0.5%
    # So the distance we calculated should be within 0.5% of the result given by AGU Fall Meeting in csv file
    actual_error = (abs(expected_distance - actual_distance) / expected_distance) * 100
    assert actual_error <= 0.5


# Two cities, no matter which one is the starting point and which one is the ending point,
# the distance should be the same
def test_distance_to_for_each():
    salzburg = City('Salzburg', 'Austria', 3, 47.7981346, 13.0464806)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    assert salzburg.distance_to(hainan) == hainan.distance_to(salzburg)


# distances up to 1000 km
def test_co2_to_first_category():
    burbank = City('Burbank', 'United States', 1, 34.1816482, -118.3258554)
    burlingame = City('Burlingame', 'United States', 1, 37.5841026, -122.3660825)
    expected_co2 = 200 * 1 * burbank.distance_to(burlingame)
    assert burbank.co2_to(burlingame) == expected_co2


# distances larger than 1000 km, but up to 8000 km
def test_co2_to_second_category():
    chittagong = City('Chittagong', 'Bangladesh', 1, 22.3307998, 91.8412863)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    expected_co2 = 250 * 1 * chittagong.distance_to(hainan)
    assert chittagong.co2_to(hainan) == expected_co2


# longer distances
def test_co2_to_third_category():
    callaham = City('Callaghan', 'Australia', 8, -32.8892352, 151.6998983)
    burbank = City('Burbank', 'United States', 1, 34.1816482, -118.3258554)
    expected_co2 = 300 * 8 * callaham.distance_to(burbank)
    assert callaham.co2_to(burbank) == expected_co2


def test_co2_to_for_each():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    assert hawthorn.co2_to(hainan) / hawthorn.num_attendees == hainan.co2_to(hawthorn) / hainan.num_attendees


# tests for CityCollection class variables

def test_city_collection_class_cities_initialize():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    list_of_cities = [hawthorn, hainan]
    city_collection = CityCollection(list_of_cities)
    assert city_collection.cities == list_of_cities


def test_outer_type_invalid_city_collection_class_cities_initialize():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    tuple_of_cities = (hawthorn, hainan)
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection = CityCollection(tuple_of_cities)


def test_empty_type_invalid_city_collection_class_cities_initialize():
    list_of_cities = []
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection = CityCollection(list_of_cities)


def test_inner_type_invalid_city_collection_class_cities_initialize():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    list_of_cities = [hawthorn, 5]
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection = CityCollection(list_of_cities)


def test_city_collection_class_cities_set():
    callaham = City('Callaghan', 'Australia', 8, -32.8892352, 151.6998983)
    burbank = City('Burbank', 'United States', 1, 34.1816482, -118.3258554)
    city_collection = CityCollection([callaham, burbank])
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    list_of_cities = [hawthorn, hainan]
    city_collection.cities = [hawthorn, hainan]
    assert city_collection.cities == list_of_cities


def test_outer_type_invalid_city_collection_class_cities_set():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    city_collection = CityCollection([hawthorn, hainan])
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection.cities = (hawthorn, hainan)


def test_empty_type_invalid_city_collection_class_cities_set():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    city_collection = CityCollection([hawthorn, hainan])
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection.cities = []


def test_inner_type_invalid_city_collection_class_cities_set():
    hawthorn = City('Hawthorn', 'Austria', 2, -37.8355533, 145.055224565243)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    city_collection = CityCollection([hawthorn, hainan])
    expected_error_message = "The cities should take a list of City objects"
    with raises(TypeError, match=expected_error_message):
        city_collection.cities = [hawthorn, 5]


# tests for CityCollection class function
def test_countries():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    city_collection = CityCollection([shenyang, hainan])
    expected_unique_country_list = ['China']
    assert city_collection.countries() == expected_unique_country_list


def test_total_attendees():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    city_collection = CityCollection([shenyang, hainan])
    expected_total_attendees = 3
    assert city_collection.total_attendees() == expected_total_attendees


def test_total_distance_travel_to():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan])
    expected_total_distance = shenyang.distance_to(guiyang) * 1 + hainan.distance_to(guiyang) * 2
    assert city_collection.total_distance_travel_to(guiyang) == expected_total_distance


def test_travel_by_country():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan])
    expected_dict = {'China': city_collection.total_distance_travel_to(guiyang)}
    assert city_collection.travel_by_country(guiyang) == expected_dict


def test_total_co2():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan])
    expected_total_co2 = shenyang.co2_to(guiyang) + hainan.co2_to(guiyang)
    assert city_collection.total_co2(guiyang) == expected_total_co2


def test_co2_by_country():
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan])
    expected_dict = {'China': shenyang.co2_to(guiyang) + hainan.co2_to(guiyang)}
    assert city_collection.co2_by_country(guiyang) == expected_dict


# the collected cities exclude host city
def test_summary_exclude_host_city(capfd):
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan])
    city_collection.summary(guiyang)
    out, err = capfd.readouterr()
    expected_print = "Host city: Guiyang (China)\n" + "Total CO2: %d tonnes\n" % round(
        city_collection.total_co2(
            guiyang) / 1000) + "Total attendees travelling to Guiyang from 2 different cities: 3\n"
    assert out == expected_print


# the collected cities include host city, but contains only one
def test_summary_contain_single_host_city(capfd):
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan, guiyang])
    city_collection.summary(guiyang)
    out, err = capfd.readouterr()
    expected_print = "Host city: Guiyang (China)\n" + "Total CO2: %d tonnes\n" % round(
        city_collection.total_co2(
            guiyang) / 1000) + "Total attendees travelling to Guiyang from 2 different cities: 3\n"
    assert out == expected_print


# the collected cities include host city, and several of the cities in the collection are host cities
def test_summary_contain_multiple_host_city(capfd):
    shenyang = City('Shenyang', 'China', 1, 41.8, 123.38)
    hainan = City('Hainan', 'China', 2, 19.2000001, 109.5999999)
    guiyang_a = City('Guiyang', 'China', 6, 25.7561647, 112.72964)
    guiyang_b = City('Guiyang', 'China', 12, 25.7561647, 112.72964)
    guiyang = City('Guiyang', 'China', 18, 25.7561647, 112.72964)
    city_collection = CityCollection([shenyang, hainan, guiyang_a, guiyang_b])
    city_collection.summary(guiyang)
    out, err = capfd.readouterr()
    expected_print = "Host city: Guiyang (China)\n" + "Total CO2: %d tonnes\n" % round(
        city_collection.total_co2(
            guiyang) / 1000) + "Total attendees travelling to Guiyang from 2 different cities: 3\n"
    assert out == expected_print


# Some cities have the same name, but they are actually different cities.
# The more important attribute to determine if two cities are the same is latitude and longitude.
def test_summary_contain_host_city_different_location(capfd):
    san_diego_usa = City('San Diego', 'United States', 43, 32.7174209, -117.1627714)
    san_diego_brazil = City('San Diego', 'Brazil', 20, -30.4830, -55.758)
    shenyang = City('Shenyang', 'China', 4, 41.8, 123.38)
    city_collection = CityCollection([shenyang, san_diego_usa])
    city_collection.summary(san_diego_brazil)
    out, err = capfd.readouterr()
    expected_print = "Host city: San Diego (Brazil)\n" + "Total CO2: %d tonnes\n" % round(
        city_collection.total_co2(
            san_diego_brazil) / 1000) + "Total attendees travelling to San Diego from 2 different cities: 47\n"
    assert out == expected_print


# If the distance between cities is very close, co2 emissions are significantly affected by the number of attendees,
# and the more the number of attendees a city sends, the less it should be selected as a host city.
def test_sorted_by_emissions_num_attendees_lead():
    a = City('a', 'A', 1, 1.0, 1.0)
    b = City('b', 'B', 10, 1.1, 1.1)
    c = City('c', 'C', 100, 1.2, 1.2)
    d = City('d', 'D', 1000, 1.3, 1.3)
    collection_abc = CityCollection([a, b, c])
    collection_abd = CityCollection([a, b, d])
    collection_acd = CityCollection([a, c, d])
    collection_bcd = CityCollection([b, c, d])
    total_collection = CityCollection([a, b, c, d])
    expected_sort_list = [('d', collection_abc.total_co2(d)), ('c', collection_abd.total_co2(c)),
                          ('b', collection_acd.total_co2(b)), ('a', collection_bcd.total_co2(a))]
    assert total_collection.sorted_by_emissions() == expected_sort_list


# When all cities send the same number of attendees, co2 emissions are completely controlled by distance,
# so the smaller the distance from all other cities to a given city,
# the more likely that city will be chosen as host city.
# All four cities are from China, and if you look at a map of China,
# you will see that Chongqing is included in the middle by the other three cities, so if it is chosen as host city,
# The distance to the other cities is the smallest and the co2 emission is also the smallest.
# Most of the maps are scaled equally, so it is not difficult to determine the order of the other three cities.
def test_sorted_by_emissions_distance_lead():
    chengdu = City('Chengdu', 'China', 1, 30.6624205, 104.0633219)
    wuhan = City('Wuhan', 'China', 1, 30.5951051, 114.2999353)
    nanning = City('Nanning', 'China', 1, 22.8211654, 108.3159756)
    chongqing = City('Chongqing', 'China', 1, 29.35, 106.33)
    collection_abc = CityCollection([chengdu, wuhan, nanning])
    collection_abd = CityCollection([chengdu, wuhan, chongqing])
    collection_acd = CityCollection([chengdu, nanning, chongqing])
    collection_bcd = CityCollection([wuhan, nanning, chongqing])
    total_collection = CityCollection([chengdu, wuhan, nanning, chongqing])
    expected_sort_list = [('Chongqing', collection_abc.total_co2(chongqing)),
                          ('Chengdu', collection_bcd.total_co2(chengdu)),
                          ('Nanning', collection_abd.total_co2(nanning)), ('Wuhan', collection_acd.total_co2(wuhan))]
    assert total_collection.sorted_by_emissions() == expected_sort_list
