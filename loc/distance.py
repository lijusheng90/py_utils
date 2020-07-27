import math


def geo_distance(lng_1, lat_1, lng_2, lat_2):
    lng_1, lat_1, lng_2, lat_2 = map(math.radians, [lng_1, lat_1, lng_2, lat_2])
    d_lon = lng_2 - lng_1
    d_lat = lat_2 - lat_1
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    dis = 2 * math.asin(math.sqrt(a)) * 6371 * 1000
    return round(dis / 1000, 2)


if __name__ == "__main__":
    lng1, lat1, lng2, lat2 = 10, 10, 10, -10
    print(geo_distance(lng1, lat1, lng2, lat2))