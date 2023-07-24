import csv
from pathlib import Path

from cities import City, CityCollection


def read_attendees_file(filepath: Path) -> CityCollection:
    with open(filepath, "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]
    cities = []
    data_rows = rows[1:]
    for data in data_rows:
        city = City(data[3], data[1], int(data[0]), float(data[4]), float(data[5]))
        cities.append(city)
    city_collection = CityCollection(cities)
    return city_collection

