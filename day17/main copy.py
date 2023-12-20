import timeit
from queue import PriorityQueue

directions = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
cells =  {}
class Cell:
    def __init__(self, x, y, loss) -> None:
        self.x = x
        self.y = y 
        self.loss = int(loss)
        self.neighbours = {}
    
    def attach_neibours(self):
        for dir in directions.items():
            for dist in range(1,4):
                if (self.x + dir[1][0]*dist, self.y + dir[1][1]*dist) in cells:
                    self.neighbours[dir[0]] = cells[self.x + dir[1][0], self.y + dir[1][1]]

    def __lt__(self, other):
        return self.loss < other.loss
    
def dijkstra(cells, start_vertex, size):
    dir = [0, 0] # 0 - direction, [1] counter
    D = {}
    for dir in range(16):
        D.update({(v[0], v[1], dir//4, dir%4):float('inf') for v in cells})
    D[start_vertex.x, start_vertex.y, 0, 0] = 0
    #for d in D.items():
    #    print(d)

    pq = PriorityQueue()
    pq.put((0, start_vertex, 0, -1))
    
    visited = []

    while not pq.empty():
        
        (dist, current_vertex, dir, dir_counter) = pq.get()
        visited.append((current_vertex, dir, dir_counter))
        
        for new_dir, cell in current_vertex.neighbours.items():
            new_dir_counter = dir_counter
            if new_dir == dir and dir_counter < 2:
                new_dir_counter = dir_counter + 1
            elif abs (new_dir - dir) != 2 and new_dir != dir:
                new_dir_counter = 0
            else:
                continue 

            distance = cell.loss
            if (cell,new_dir,new_dir_counter) not in visited:
                old_cost = D[cell.x, cell.y, dir, new_dir_counter]
                new_cost = dist + distance
                if new_cost < old_cost:
                    #if (cell.x, cell.y) == (2,1):
                        #pass
                    
                    values = [D[cell.x, cell.y, new_dir, i] for i in range(4)]
                    if not values or max(values) >= new_cost:
                        #print(max(values))
                        pq.put((new_cost, cell, new_dir, new_dir_counter))
                    D[cell.x, cell.y, new_dir, new_dir_counter] = new_cost
                    #print(f"{cell.x} {cell.y} | {new_cost} | {new_dir} {new_dir_counter}")
                    #if len(D)%10 == 0:
                    print(f'{new_cost} {len(visited)}', end= '\r')
                    if (cell.x == size-1 and cell.y == size-1):
                        return D
    return D

 
def main():
    size = parse_input("test.txt")
    for cell in cells.values():
        cell.attach_neibours()
    #draw_map(size)
    
    result = dijkstra(cells, cells[0,0], size)    
    draw_dijkstra(result, size)
    #print(result[size-1, size-1, 0])


def draw_dijkstra(D, size):
    output = {}
    print()
    line = "0000  "
    for x in range(size):
        line += str(x).zfill(3) + " "
    print (line)
    print ()
    for y in range(size):
        line = str(y).zfill(4) + '  '
        for x in range(size):
            line += str(cells[x,y].loss).zfill(3) + ' '
        print (line)
        line = str(y).zfill(4) + '  '
        for x in range(size):
            values = [D[x,y,dir//4,dir%4] for dir in range(16)]
            output[x,y] = values
            line += str(min(values)).zfill(3) + ' '
        print (line)  
        
        print ()
    
    #for line in output.items():
    #    print(f"{(cells[line[0]].loss)} {line[0]} \t {line[1]}")
    print("+++")
    print(min(output[size-1, size-1]))
            

def draw_map(size):
    for y in range(size):
        line = ""
        for x in range(size):
            line += str(cells[x,y].loss)
        print (line)

def parse_input(file):
    with open(file, "r") as file:
        size = 0
        for y,line in enumerate(file):
            size = len(line.strip())
            for x,char in enumerate(line.strip()):
                cells[x,y] = Cell (x,y,char)
    return size


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")