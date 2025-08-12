from modules.fare_calculator import get_fare

# Step 1: Take input for pickup and drop
pickup_location = input("Enter the pickup location: ")
drop_location = input("Enter the drop location: ")

# Step 2: Ride platforms list
ride_platforms = ["Ola", "Uber", "Rapido"]

# Step 3: Loop through platforms and display checking message
for platform in ride_platforms:
    print(f"Checking fares for {platform} from {pickup_location} to {drop_location}...")

# Step 4: Take base fare and distance from user
base_fare_input = float(input("Enter the base fare: "))
distance_input = float(input("Enter the distance in km: "))

# Step 5: Get fare details
ride_info = get_fare(pickup_location, drop_location, distance_input, base_fare_input)

# Step 6: Print fare details
print("Fare details:", ride_info)
