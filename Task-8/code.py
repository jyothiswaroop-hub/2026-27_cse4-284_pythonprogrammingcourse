
# Campus Transport Allocation System

print("===== CAMPUS TRANSPORT ALLOCATION =====")

routes = []
demands = []
capacities = []
buses_required = []
unserved_passengers = []

n = int(input("Enter number of routes: "))

total_buses = 0
total_unserved = 0

for i in range(n):
    print("\nRoute", i + 1)

    route = input("Enter route name: ")
    passengers = int(input("Enter passenger demand: "))
    capacity = int(input("Enter bus capacity: "))

    # Calculate buses required
    buses = (passengers + capacity - 1) // capacity

    # Calculate unserved passengers
    available_capacity = buses * capacity
    unserved = max(0, passengers - available_capacity)

    routes.append(route)
    demands.append(passengers)
    capacities.append(capacity)
    buses_required.append(buses)
    unserved_passengers.append(unserved)

    total_buses += buses
    total_unserved += unserved

# Display allocation report
print("\n===== TRANSPORT ALLOCATION REPORT =====")

print("Route\tDemand\tCapacity\tBuses\tUnserved")

for i in range(n):
    print(routes[i], "\t", demands[i], "\t",
          capacities[i], "\t\t",
          buses_required[i], "\t",
          unserved_passengers[i])

print("\n===== FINAL SUMMARY =====")
print("Total Routes:", n)
print("Total Buses Required:", total_buses)
print("Total Passengers:", sum(demands))
print("Total Unserved Passengers:", total_unserved)

if total_unserved == 0:
    print("Status: All passengers are served.")
else:
    print("Status: Some passengers are unserved.")

print("===== END OF REPORT =====")

