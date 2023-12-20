import timeit
mirrors_type = {'-':0, '|':1, '/':2, "\\":3, '.':4}
directions = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
mirrors = {}

all_reflect_maps = {0:{0:[0],   1:[0,2], 2:[2],   3:[0,2]},
                    1:{0:[1,3], 1:[1],   2:[1,3], 3:[3]},
                    2:{0:[1],   1:[0],   2:[3],   3:[2]},
                    3:{0:[3],   1:[2],   2:[1],   3:[0]},
                    4:{0:[0],   1:[1],   2:[2],   3:[3]}}
class Mirror:
    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.char_type = type
        self.type = mirrors_type[type]
        self.reflect_map = all_reflect_maps[self.type]
    
    def reflect(self, dir):
        output = []
        for output_dir in self.reflect_map[dir]:
            target = (self.x + directions[output_dir][0], self.y + directions[output_dir][1])
            if target in mirrors:
                output.append([mirrors[self.x + directions[output_dir][0], 
                               self.y + directions[output_dir][1]] , 
                               output_dir])
        return output

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.type}"

def parse_input(file):
    with open(file, "r") as file:
        width = 0
        for y,line in enumerate(file):
            width = len(line)
            for x, char in enumerate(line.strip()):
                mirrors[x,y] = Mirror(x,y,char)
        return width
    
def bfs(start):
    queue = [[mirrors[start[0],start[1]],start[2]]]
    visited = [[mirrors[start[0],start[1]],start[2]]]
    
    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        #print (m[0], " ", m[1], end = " ") 

        for neighbour in m[0].reflect(m[-1]):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    set_visited = []
    for item in visited:
        if item[0] not in set_visited:
            set_visited.append(item[0])
    return len(set_visited)

def main():
    width = parse_input("test.txt")
    #for y in range(height):
    #    line = ""
    #    for x in range(width):
    #        line += mirrors[x,y].char_type
    #    print(line)
    max = 0
    
    for coordinate in range(width):
        start = [coordinate, 0, 3]
        visited = bfs(start)
        print(start, visited)
        if visited > max:
            max = visited
            print(f"max {max}")

    for coordinate in range(width):
        start = [0, coordinate, 0]
        visited = bfs(start)
        print(start, visited)

        if visited > max:
            max = visited
            print(f"max {max}")

    for coordinate in range(width):
        start = [coordinate, width-1, 1]
        visited = bfs(start)
        print(start, visited)

        if visited > max:
            max = visited
            print(f"max {max}")
    
    for coordinate in range(width):
        start = [width-1, coordinate, 2]
        visited = bfs(start)
        print(start, visited)
        if visited > max:
            max = visited
            print(f"max {max}")


    print(max)
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")