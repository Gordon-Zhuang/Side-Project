from geopy.geocoders import Nominatim
import random
def random_adress():
    returnarry = []
    for i in range(60):
        lat = round(random.uniform(24.965376, 25.115544), 6)
        long = round(random.uniform(121.401070, 121.612159), 6)
        geocoder = Nominatim(user_agent='random_address')
        location = geocoder.reverse((lat, long))
        try:
            road = location.raw['address']['road']
        except KeyError:
            try:
                road = location.raw['address']['hamlet']
            except KeyError:
                try:
                    road = location.raw['address']['neighbourhood']
                except KeyError:
                    try:
                        road = location.raw['address']['residential']
                    except KeyError:
                        try:
                            road = location.raw['address']['industrial']
                        except KeyError:
                            road = 'None'
        try:
            city = location.raw['address']['city']
        except KeyError:
            city = location.raw['address']['county']
        try:
            suburb = location.raw['address']['suburb']
        except KeyError:
            try:
                suburb = location.raw['address']['suburb']
            except KeyError:
                suburb = location.raw['address']['city_district']
        returnarry.append([city + suburb + road, float(long), float(lat)])

    return returnarry
