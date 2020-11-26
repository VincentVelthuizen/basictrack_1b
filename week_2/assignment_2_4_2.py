distance = float(input("What is the distance you need to travel (in km)? "))

walking_speed = 5       # in km/h
walking_get_going = 1   # in minutes
walking_parking = 0     # in minutes
walking_total_time = walking_get_going + 60 * (distance / walking_speed) + walking_parking  # minutes

biking_speed = 20
biking_get_going = 5
biking_parking = 5
biking_total_time = biking_get_going + 60 * (distance / biking_speed) + biking_parking

driving_speed = 40      # in km/h, average within city limits?
driving_get_going = 5
driving_parking = 10
driving_total_time = driving_get_going + 60 * (distance / driving_speed) + driving_parking

print("Walking will take", walking_total_time, "minutes")
print("Biking will take", biking_total_time, "minutes")
print("Driving will take", driving_total_time, "minutes")
