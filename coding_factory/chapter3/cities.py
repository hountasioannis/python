cities = ["london","paris", "barcelona", "athens"]

cap_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))
print(cap_cities)