from functions import *
from settings import land, sea, air

cities = set()
for d in [land, sea, air]:
    cities.update(d.keys())

print("* CITIES ON MAP *")
for city in cities:
    print(city)

start = input("\nOrigin: ")
while start not in cities:
    start = input("Invalid. Provide new origin from list: ")

end = input("Destination: ")
while start not in cities:
    end = input("Invalid. Provide new destination from list: ")

network = {'land': land, 'sea': sea, 'air': air}

d, r = shortest_path(start, network)
print(f'Shortest path: {d[end]} via route: {r[end]}')
