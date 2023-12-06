with open("data.txt", "r") as file:
    times = file.readline().split(":")[1]
    distances = file.readline().split(":")[1]
    while " " in times:
        times = times.replace(" ", "")
    while " " in distances:
        distances = distances.replace(" ", "")

    print(times)
    print(distances)
    race = [int(times), int(distances)]
    result = 0
    for time in range(race[0]):
        if time*(race[0]-time) > race[1]:
            result += 1
        if time % 100000 == 0:
            print(f"{time//1000000}")
    print (result)
#    part_1_races = []
#   for i in range(1,len(times)):
#        part_1_races.append([int(times[i]), int(distances[i])])
#    print(part_1_races)



#    for race in part_1_races:
#        number_ow_wins = 0
#        for time in range(race[0]+1):
#            if race[1] < time*(race[0]-time):
#               number_ow_wins += 1
#        result*= number_ow_wins
#        number_ow_wins = 0
#    print(result)
