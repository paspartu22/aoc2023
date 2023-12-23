import timeit

cells = {}
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def parse_input(file):
    with open(file, "r") as file:
        start = []
        for y,line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char != "#":
                    cells[x, y] = 1
                if char == "S":
                    start = [x, y]
        return start
                    
def bfs(start, max_dist): #function for BFS
    visited = ([start])
    queue = ([[start, 0]])
    i = 0
    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        i+=1
        if i % 10 == 0:
            print (i%10*10, end = "\r") 
        
        for dir in directions:
            neighbour = (m[0][0]+dir[0], m[0][1]+dir[1]) 
            mod_neibour = (neighbour[0]%131, neighbour[1]%131)
            if mod_neibour in cells and neighbour not in visited and m[1] < max_dist:
                visited.append(neighbour)
                queue.append([neighbour, m[1]+1])      
    return visited             
        
def main():
    start = parse_input("data.txt")
    max_dist = 64
    visited = bfs([130, 0], max_dist)
    print()
    print(len(visited))
    result = []
    for item in visited:
        if (item[0]+item[1]+start[0]+start[1]) % 2 == max_dist % 2:
            result.append(item)

    for y in range(131):
        line = ""
        for x in range(131):
            if [x, y] == start:
                line += "S"
            elif (x, y) in result:
                line += "0"
            elif (x,y) in visited:
                line += "o"
            elif (x,y) in cells:
                line += "."
            else:
                line += "#"
        print (line)
    print()
    print(len(result))
  
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")
