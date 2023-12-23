import timeit

class Coordinate:
    def __init__(self, x, y, z) -> None:
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def return_cubes(self, end):
        if self.x != end.x:
            for i in range(min(self.x, end.x) , max(self.x, end.x)+1):
                yield Coordinate(i, self.y, self.z)
        elif self.y != end.y:
            for i in range(min(self.y, end.y) , max(self.y, end.y)+1):
                yield Coordinate(self.x, i, self.z)
        elif self.z != end.z:
            for i in range(min(self.z, end.z) , max(self.z, end.z)+1):
                yield Coordinate(self.x, self.y, i)
        else:
            yield Coordinate(self.x, self.y, self.z)

class Brick:
    def __init__(self, id, line) -> None:
        self.id = id
        start, end = line.split('~')
        x,y,z = start.split(",")
        self.start = Coordinate(x,y,z)
        x,y,z = end.split(",")
        self.end = Coordinate(x,y,z)
        self.cubes = list(self.start.return_cubes(self.end))
        self.stable = False
        self.support = []
        self.supported = []

    def count_fall(self, fall_list = []):
        if fall_list != []:
            for item in self.supported:
                if item.id not in fall_list:
                    return fall_list
                       
        fall_list.append(self.id)
        for item in self.support:
            fall_list = item.count_fall(fall_list)

        return fall_list

    def cubes_list(self):
        return [[cube.x, cube.y, cube.z] for cube in self.cubes]

    def get_z_by_xy(self, x, y):
        result = []
        for cube in self.cubes:
            if cube.x == x and cube.y == y:
                result.append(cube.z)
        return max(result)

    def get_xy(self):
        return [[cube.x, cube.y] for cube in self.cubes]

    def move(self, stable_bricks):
        drops = [min([cube.z-1 for cube in self.cubes])]
        for cube in self.cubes_list():
            for brick in stable_bricks.values():
                if [cube[0], cube[1]] in brick.get_xy():
                    drops.append(cube[2] - brick.get_z_by_xy(cube[0], cube[1]) - 1)
        
        for cube in self.cubes:
            cube.z -= min(drops)    
        self.stable = True
            
    def count_supports(self, bricks):
        supports = []
        for cube in self.cubes:
            cube_up = [cube.x, cube.y, cube.z-1]
            for brick in bricks:
                if self != brick and cube_up in brick.cubes_list() and brick not in supports:
                    supports.append(brick)
        
        for support in supports:
            support.support.append(self)
        self.supported = supports
        return supports
        
    def __str__(self) -> str:
        line = ""
        for cube in self.cubes:
            line += f"{cube.x} {cube.y} {cube.z} \n"
        return line[:-1]

def parse_input(file):
    
    with open(file, "r") as file:
        bricks = {(i,int(line.split("~")[0].split(",")[2])) : Brick(i, line) for i,line in enumerate(file)}
        max_z = max([item[1] for item in bricks])
    return bricks , max_z   
        
def main():
    not_stable_bricks, max_z = parse_input("data.txt")

    stable_bricks = {}

    for z in range(max_z+1):
        print(z, end='\r')
        for id, brick in not_stable_bricks.items():
            if id[1] == z and not brick.stable:
                brick.move(stable_bricks)
                stable_bricks[id] = brick
    
    result = [x for x in stable_bricks.values()]
    for z, brick in stable_bricks.items():
        support = brick.count_supports(stable_bricks.values())
        if len(support) == 1 and support[0] in result:
            result.pop(result.index(support[0]))

    print(f'part 1 {len(result)}')
    p2_result = int(0)
    
    for i, brick in stable_bricks.items():
        fall = brick.count_fall([])
        p2_result += len(fall)-1
    print(f"Result {p2_result}")
        
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")
    
1102