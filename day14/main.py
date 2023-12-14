import timeit


def parse_input(file):
    with open(file, "r") as file:
        rounds = {}
        cubes_n = {}
        cubes_w = {}
        cubes_s = {}
        cubes_e = {}
        
        size = 0
        for y,line in enumerate(file):
            size = len(line.strip())
            if y == 0:
                for x in range(size):
                    rounds[x] = []
                    cubes_n[x] = []
                    cubes_w[x] = []
                    cubes_s[x] = []
                    cubes_e[x] = []
            for x,item in enumerate(line.strip()):
                if item == "O":
                    rounds[x].append(y)
                elif item == "#":
                    cubes_n[x].append(y)
                    cubes_e[y].append(size-x-1)
                    cubes_s[size-x-1].append(size-y-1)
                    cubes_w[size-y-1].append(x)
        cubes_array = {0:cubes_n, 1:cubes_w, 2:cubes_s, 3:cubes_e}
        return rounds, cubes_array, size

def draw(rounds, cubes, size, side):
    print (side)
    for y in range(size):
        line = ""
        for x in range(size):
            if y in rounds[x]:
                line+=" 0"
            elif y in cubes[x]:
                line+=" #"
            else:
                line+=" ."
        print(line)
                       
def sweep_col(rounds, cubes, height, x):
    y = 0
    while y < height:
        if y not in rounds and y not in cubes:
            z = y
            while z < height:
                if z in cubes:
                    y = z
                    break
                elif z in rounds:
                    rounds.remove(z)
                    rounds.append(y)
                    break
                else:
                    z += 1
        y += 1
    return rounds

def main():
    rounds, cubes_array, size = parse_input("data.txt")

    for cycle_num in range(1000):    
        result = 0
        for cycle in range(4):   
            #draw(rounds, cubes_array[cycle], size, cycle)
            new_rounds = {}
            for x in range(size):
                new_rounds[x] = []
            for x in range(size):
                rounds[x] = sweep_col(rounds[x], cubes_array[cycle][x], size, x)
                for y in range(size):
                    if y in rounds[x]:
                        new_rounds[size-y-1].append(x)
            
                #result += sum([size-round for round in rounds[x]])
            #print()
            #draw(rounds, cubes_array[cycle], size, cycle)
            rounds = new_rounds
            
        for x in range(size):
            result+=sum([size-y for y in rounds[x]])
        print(f"{cycle_num} {result}")


    print()
    #draw(rounds, cubes_array[0], size, 0)
    #print(result)
    
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")