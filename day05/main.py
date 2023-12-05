class Map:
    def __init__(self, data) -> None:
        data = data.split()
        self.output = int(data[0])
        self.start = int(data[1])
        self.range = int(data[2])
        
        self.sweep = self.output - self.start
        self.end = self.start + self.range - 1

    def calc(self, input):
        if self.start <= input < self.start + self.range:
            return self.end + input - self.start
        else:
            return None

    def __str__(self) -> str:
        return f"{self.start} | {self.end} | {self.range}"

def parse_data(file_name):
    with open(file_name, "r") as file:
        maps = {}
        seeds_part_2 = []

        seeds_line = file.readline().split(":")[1].split()
        seeds_line = [int(x) for x in seeds_line]
        seeds_part_1 = seeds_line
        for i in range(int(len(seeds_line)/2)):
            seeds_part_2.append([seeds_line[2*i],seeds_line[2*i] + seeds_line[2*i+1]-1])
        
        map_num = 0
        map_array = []
        file.readline()
        for line in file:
            if line == "\n":
                maps[map_num] = map_array
                map_array = []
                map_num += 1
            elif line.split()[-1] != "map:":
                map_array.append(Map(line))
        maps[map_num] = map_array

        for i,map_array in maps.items():
            print(f"==={i}===")
            for map in map_array:
                print(map)
        print("===parsing done===")

        return seeds_part_1, seeds_part_2, maps

def solve_part_1(seeds, maps):

        # part 1
        paths = []
        results = []
        for seed in seeds:
            path = []
            print(f"Seed === {seed} ===")
            for map_num, map_array in maps.items():
                #print(f"maps === {map_num} ===")
                for map in map_array:
                    if map.calc(seed) is not None:
                        old_seed = seed
                        path.append(seed)
                        seed = map.calc(seed)
                        #print(f"maps N {map_num} from {old_seed} to {seed}")
                        break
                    #else:
                        #print("map not valid")
                    if map == map_array[-1]:
                        path.append(seed)
            
            path.append(seed)
            paths.append(path)
            results.append(seed)
            #print(seed)

        print(results)
        print("=== part one result ===")
        print(min(results))


def solve_part_2(current_layer_seed_array, maps):
    for layer_number in range(len(maps)):
        print(f"layer {layer_number}")
        new_layer_seeds_array = []
        while len(current_layer_seed_array) != 0:
            seed= current_layer_seed_array.pop()
            seed_was_processed = False
            for map in maps[layer_number]:
                if map.start <= seed[0] <=map.end or map.start <= seed[1] <= map.end:
                    seed_was_processed = True
                    new_layer_seeds_array.append([max(seed[0],map.start)+map.sweep, min(seed[1],map.end)+map.sweep])
                    if seed[0] < map.start:
                        current_layer_seed_array.append([seed[0],map.start-1])
                    if map.end < seed[1]:
                        current_layer_seed_array.append([map.end+1, seed[1]])  
            if not seed_was_processed:
                new_layer_seeds_array.append(seed)
        current_layer_seed_array = new_layer_seeds_array
        new_layer_seeds_array = []
    #min of all ranges 
    print("=== part two result ===")
    print (min([x[0] for x in current_layer_seed_array]))

def main():
    seeds_part_1, seeds_part_2, maps = parse_data("data.txt")
    solve_part_1(seeds_part_1, maps)
    solve_part_2(seeds_part_2, maps)

if __name__ == "__main__":
    main()