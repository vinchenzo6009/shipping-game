from functions import *
from settings import land as adj

print("* DESTINATIONS *")
for city in adj:
    print(city)

start = input("\nOrigin: ")
while start not in adj:
    start = input("Invalid. Provide new origin from list: ")

end = input("Destination: ")
while start not in adj:
    end = input("Invalid. Provide new destination from list: ")

d, r = shortest_path(start, adj)
print(f'Shortest path: {d[end]} via route: {r[end]}')
