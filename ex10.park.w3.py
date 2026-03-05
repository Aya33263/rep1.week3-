# ParkingMeter.py
# @ author: A. N. Other
# @ date: September 2016

print("Kia Ora, this is a parking meter")
park_time =4
print("park_time time is ", park_time, " hours.")

rate = 4
cost = 0

if park_time > 3:
    # Charge the first 3 hours at the full rate
    cost = rate * 3
    # Drop the rate by $2 for subsequent hours
    rate -= 2
    # Get the remainder of the parking time
    park_time -= 3
    # Add the discounted rate for the remaining time to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    # If 3 hours or less, use the standard rate for the whole time
    cost = rate * park_time
    print("The cost of the parking is $", cost)