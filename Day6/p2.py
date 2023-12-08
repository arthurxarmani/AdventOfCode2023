
import sys

file = open(sys.argv[1], "r")
lines = file.readlines()

times_allowed = []
best_distances = []
for line in lines:
    if line.startswith("Time:"):
        line.strip()
        times_allowed = [int(x) for x in line.split(":")[1].replace(" ", "").split()]
    
    if line.startswith("Distance:"):
        line.strip()
        best_distances = [int(x) for x in line.split(":")[1].replace(" ", "").split()]


def get_distance(starting_speed, max_time):
    print("getting distance for starting speed: " + str(starting_speed) + " and max time: " + str(max_time))
    seconds_left = max_time - starting_speed
    distance = starting_speed * seconds_left
    return distance

def get_number_of_ways(time, distance):
    """
    Returns the number of ways to get to the destination in the given time.
    """
    print("time: " + str(time))
    print("distance: " + str(distance))
    min_distance = distance
    starting_speed = 1
    number_of_ways = 0
    exhausted = False
    backtrack = False
    step = 10000 # The number of speeds to skip forward by.
    while not exhausted:
        distance_actual = get_distance(starting_speed, time) # Get the distance traveled in the given time.
        if distance_actual <= min_distance and not backtrack:
            # In this case we increment by 1 to find the first speed that will get us to the destination in the record time.
            starting_speed += 1
        elif distance_actual > min_distance and not backtrack: # If the distance traveled is greater than the minimum distance, then we have a new way to win.
            # Get the distance traveled with the new starting speed.
            distance_plus_ten = get_distance(starting_speed + step, time)
            if distance_plus_ten > min_distance:
                number_of_ways += step # Skip forward by step
                starting_speed += step
            else:
                backtrack_value = starting_speed + step # This is the point we don't want to go past.
                print("number of ways: " + str(number_of_ways))
                print("=============backtrack value: " + str(backtrack_value))
                backtrack = True
        elif backtrack and number_of_ways > 0 and starting_speed <= backtrack_value:
            print(int(backtrack_value))
            distance_actual = get_distance(starting_speed, time) # Get the distance traveled in the given time.
            if distance_actual > min_distance:
                number_of_ways += 1
                starting_speed += 1
            else:
                exhausted = True
        else:
            exhausted = True

    return number_of_ways

number_of_ways = []
for i in range(len(times_allowed)):
    time = times_allowed[i]
    distance = best_distances[i]
    number_of_ways.append(get_number_of_ways(time, distance))

print("You can beat this in " + str(number_of_ways) + " ways.")
