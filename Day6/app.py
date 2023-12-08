
import sys

file = open(sys.argv[1], "r")
lines = file.readlines()

times_allowed = []
best_distances = []
for line in lines:
    if line.startswith("Time:"):
        line.strip()
        print(line.split(":")[1].split())
        times_allowed = [int(x) for x in line.split(":")[1].split()]
    
    if line.startswith("Distance:"):
        line.strip()
        best_distances = [int(x) for x in line.split(":")[1].split()]


def get_distance(starting_speed, max_time):
    print("getting distance for starting speed: " + str(starting_speed) + " and max time: " + str(max_time))
    seconds_left = max_time - starting_speed
    distance = starting_speed * seconds_left
    return distance

def get_number_of_ways(time, distance):
    print("time: " + str(time))
    print("distance: " + str(distance))
    max_time = time
    min_distance = distance
    starting_speed = 0
    number_of_ways = 0
    
    for i in range(max_time):
        starting_speed = i
        distance_actual = get_distance(starting_speed, time)
        if distance_actual > min_distance:
            number_of_ways += 1

    return number_of_ways

number_of_ways = []
for i in range(len(times_allowed)):
    time = times_allowed[i]
    distance = best_distances[i]
    number_of_ways.append(get_number_of_ways(time, distance))

multiple = None
for way in number_of_ways:
    if multiple == None:
        multiple = way
    else:
        multiple *= way
print(multiple)