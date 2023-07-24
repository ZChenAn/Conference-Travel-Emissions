from typing import Dict, List, Tuple
import math

import matplotlib.pyplot as plt


class City:

    def __init__(self, name, country, num_attendees, latitude, longitude):
        self.name = name
        self.country = country
        self.num_attendees = num_attendees
        self.latitude = latitude
        self.longitude = longitude

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_input):
        # the input city name should be a string
        if not type(name_input) == str:
            raise TypeError("City name should be passed in string type, not %s type" % type(name_input))
        # the string can not be empty string
        if len(name_input) == 0:
            raise ValueError("The city name can not be empty")
        self._name = name_input

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country_input):
        # the input country should be a string
        if not type(country_input) == str:
            raise TypeError("Country should be passed in string type, not %s type" % type(country_input))
        # the string can not be empty string
        if len(country_input) == 0:
            raise ValueError("The country name can not be empty")
        self._country = country_input

    @property
    def num_attendees(self):
        return self._num_attendees

    @num_attendees.setter
    def num_attendees(self, num_attendees_input):
        # the input number of attendees should be an integer
        if not type(num_attendees_input) == int:
            raise TypeError("Number of attendees be passed as an integer, not %s type" % type(num_attendees_input))
        # the number of attendees should be a positive number,
        if num_attendees_input < 0:
            raise ValueError("Number of attendees must be a positive number, not %d" % num_attendees_input)
        self._num_attendees = num_attendees_input

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude_input):
        # the input latitude should be real numbers
        if not (type(latitude_input) == float or type(latitude_input) == int):
            raise TypeError("Latitude be passed as decimal numbers, not %s type" % type(latitude_input))
        # the input latitude should be restricted to the -90 to 90
        if not (-90 <= latitude_input <= 90):
            raise ValueError("Latitude should be restricted to the -90 to 90, not %f" % latitude_input)
        self._latitude = latitude_input

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude_input):
        # the input longitude should be real numbers
        if not (type(longitude_input) == float or type(longitude_input) == int):
            raise TypeError("Longitude be passed as decimal numbers, not %s type" % type(longitude_input))
        # the input longitude should be restricted to the -180 to 180
        if not (-180 <= longitude_input <= 180):
            raise ValueError("Longitude should be restricted to the -180 to 180, not %f" % longitude_input)
        self._longitude = longitude_input

    # the distance in km from one city to other city
    def distance_to(self, other: 'City') -> float:
        distance = 2 * 6371 * math.asin(math.sqrt(
            (math.sin((math.radians(other.latitude) - math.radians(self.latitude)) / 2)) ** 2 + math.cos(
                math.radians(other.latitude)) * math.cos(
                math.radians(self.latitude)) * (
                math.sin((math.radians(other.longitude) - math.radians(self.longitude)) / 2)) ** 2))
        return distance

    # the CO2 in kg emitted by the all researchers from one city travelling to other city
    def co2_to(self, other: 'City') -> float:
        distance = self.distance_to(other)
        if distance <= 1000:
            co2 = 200 * distance * self.num_attendees
        elif 1000 < distance <= 8000:
            co2 = 250 * distance * self.num_attendees
        else:
            co2 = 300 * distance * self.num_attendees
        return co2


class CityCollection:

    def __init__(self, cities: List[City]):
        self.cities = cities

    @property
    def cities(self):
        return self._cities

    @cities.setter
    def cities(self, cities_input):
        # the input cities should be a list of City objects
        if type(cities_input) == list and len(cities_input) > 0:
            if all(type(city) == City for city in cities_input):
                self._cities = cities_input
            else:
                raise TypeError("The cities should take a list of City objects")
        else:
            raise TypeError("The cities should take a list of City objects")

    # return a list of unique countries that the cities in the collection belong to
    def countries(self) -> List[str]:
        countries_list = [city.country for city in self.cities]
        unique_countries_list = sorted(set(countries_list), key=countries_list.index)
        return unique_countries_list

    # return the number of all the attendees
    def total_attendees(self) -> int:
        num_total_attendees = sum([city.num_attendees for city in self.cities])
        return num_total_attendees

    # return the total distance travelled by all attendees
    def total_distance_travel_to(self, city: City) -> float:
        total_distance = sum([start_city.distance_to(city) * start_city.num_attendees for start_city in self.cities])
        return total_distance

    # return a dictionary mapping the attendees' country to the distance
    # travelled by all attendees from that country to the host city
    def travel_by_country(self, city: City) -> Dict[str, float]:
        dict_country_distance = {}
        for start_city in self.cities:
            if dict_country_distance.get(start_city.country) is not None:
                dict_country_distance[start_city.country] += start_city.distance_to(city) * start_city.num_attendees
            else:
                dict_country_distance[start_city.country] = start_city.distance_to(city) * start_city.num_attendees
        return dict_country_distance

    # returns the total CO2 emitted travelled by all attendees
    def total_co2(self, city: City) -> float:
        total_co2 = sum([start_city.co2_to(city) for start_city in self.cities])
        return total_co2

    # returns a dictionary mapping the attendees' country to the C02
    # emitted by all attendees from that country to the host city
    def co2_by_country(self, city: City) -> Dict[str, float]:
        dict_country_co2 = {}
        for start_city in self.cities:
            if dict_country_co2.get(start_city.country) is not None:
                dict_country_co2[start_city.country] += start_city.co2_to(city)
            else:
                dict_country_co2[start_city.country] = start_city.co2_to(city)
        return dict_country_co2

    # print out appropriate information
    def summary(self, city: City):
        print("Host city: %s (%s)" % (city.name, city.country))
        print("Total CO2: %d tonnes" % round(self.total_co2(city) / 1000))
        # The latitude and longitude of the same city are the same, and we use the latitude and longitude attributes
        # of the city to get the number of different cities from which attendees go to the host city.
        # Here we need to consider several situations, as you will see more obviously in my test cases
        # 1. Statistics of the same city in csv with multiple rows, sometimes number of attendees can also be different
        # e.g. city Morgantown in attendee_locations.csv
        # 2. The same city is called by different names, but they are the same city
        # e.g. Shaanxi and Shaanxi Province in attendee_locations.csv, my hometown shenyang also called shengjing
        # 3. Some cities have the same name, but they are actually different cities.
        # e.g. San Diego in the United States, San Diego in Brazil
        # 4. keyword is travelling to, if the collected cities include host city, they are not counted in the statistics
        # e.g. The host city is Zurich, Zurich information is also in attendee_locations.csv
        count = 0
        host_city_idx = []
        latitude_longitude_list = []
        city_collection_list = []
        temp_city_collection_list = []
        for data_city in self.cities:
            latitude_longitude_list.append([data_city.latitude, data_city.longitude])
        for i in latitude_longitude_list:
            if latitude_longitude_list.count(i) > 1:
                city_collection_list.append(i)
        overlap = city_collection_list.count([city.latitude, city.longitude])
        if overlap > 0:
            overlap = overlap - 1
        origin_len = len(city_collection_list)
        for item in city_collection_list:
            if not item in temp_city_collection_list:
                temp_city_collection_list.append(item)
        current_len = len(temp_city_collection_list)
        count = count + origin_len - current_len
        for i in range(len(self.cities)):
            if math.isclose(self.cities[i].latitude, city.latitude) and math.isclose(self.cities[i].longitude,
                                                                                     city.longitude):
                count = count + 1
                host_city_idx.append(i)
        host_city_attendees = sum([self.cities[idx].num_attendees for idx in host_city_idx])
        print("Total attendees travelling to %s from %d different cities: %d" % (
            city.name, len(self.cities) - count + overlap,
            self.total_attendees()
            - host_city_attendees))

    # return a sorted list of city names and CO2 emissions
    # the elements are sorted by the total CO2 emitted by all attendees if that city were to be chosen as the host city

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        emissions_list = [self.total_co2(host_city) for host_city in self.cities]
        emissions_sort_index = sorted(range(len(emissions_list)), key=emissions_list.__getitem__)
        emissions_sort_list = sorted(emissions_list)
        country_sort_list = [self.cities[idx].name for idx in emissions_sort_index]
        country_emissions_sort_list = list(zip(country_sort_list, emissions_sort_list))
        return country_emissions_sort_list

    # plotting
    def plot_top_emitters(self, city: City, n: int = 10, save: bool = False):
        emissions_dict = self.co2_by_country(city)
        emissions_sort_list = sorted(emissions_dict.items(), key=lambda x: x[1], reverse=True)
        countries = [emissions_sort_list[i][0] for i in range(n)]
        countries.append('Everything else')
        emissions = [emissions_sort_list[i][1] for i in range(n)]
        emissions.append(sum([emissions_sort_list[j][1] for j in range(n, len(emissions_sort_list))]))
        emissions_tonnes = [emission / 1000 for emission in emissions]
        my_colors = ['pink', 'grey', 'blue', 'magenta', 'brown', 'red', 'green', 'cyan', 'orange', 'purple', 'black']
        plt.figure(figsize=(10, 8))
        plt.bar(countries, emissions_tonnes, color=my_colors)
        plt.xticks(rotation=45)
        plt.ylabel("Total emissions (tonnes CO2)")
        plt.title("Total emissions from each country(top %d)" % n)
        if save:
            save_name = str.lower(city.name)
            save_name = save_name.replace(" ", "_")
            plt.savefig('./' + save_name + '.png')
        else:
            plt.show()
