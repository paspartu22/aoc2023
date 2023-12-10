class Pipe:
    def __init__(self, x, y, letter = "") -> None:
        self.x = x
        self.y = y 
        self.letter = letter
        self.directions = pipes_letters[letter]
    
    def return_adj_pipe(self, direction):
        x = self.x + directions[self.directions[direction]][0]
        y = self.y + directions[self.directions[direction]][1]
        return pipes[x, y] #
    
    def return_halfpipe(self, direction): #part 2 double coordinates
        x = 2*self.x + directions[self.directions[direction]][0]
        y = 2*self.y + directions[self.directions[direction]][1]
        return [x,y]        

    def __str__(self):
        return f"{self.x}, {self.y}, {self.directions}"

directions = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
pipes_letters = {"-":[0,2], "|":[1,3], "L":[0,1], "J":[1,2],"7":[2,3],"F":[0,3], "S":[3,2]}
pipes = {}

def parse_input(file):
    with open(file, "r") as file:
        height = 0
        width = 0
        for y,line in enumerate(file):
            height += 1
            width = len(line)
            for x, item in enumerate(line.strip()):
                if item != ".":
                    pipes[x,y] = Pipe(x,y, item)
                if item == "S":
                    start_pipe = pipes[x, y]
    return start_pipe, height, width


def double_map (loop):
    new_loop_tiles = []
    for pipe in loop:
        new_loop_tiles.append([pipe.x*2, pipe.y*2])
        if pipe.return_halfpipe(0) not in new_loop_tiles:
            new_loop_tiles.append(pipe.return_halfpipe(0))            
        if  pipe.return_halfpipe(1) not in new_loop_tiles:
            new_loop_tiles.append(pipe.return_halfpipe(1))     
    return new_loop_tiles       

def bfs(node, loop, height, width): #function for BFS

    visited = [node] # List for visited nodes.
    real_tiles = [node]
    queue = [node]     #Initialize a queue

    while queue:    
        if len(visited)%1000 == 0:
            print(len(visited))      # Creating loop to visit each node
        m = queue.pop(0) 

        for dir in directions.values():
            new = [m[0]+dir[0], m[1]+dir[1]]
            if (-1 <= new[0] <= 2*width+1 and -1 <= new[1] <= 2*height+1 and 
                new not in visited and new not in loop):
                visited.append(new)
                queue.append(new)
                if new[0]%2==0 and new[1]%2==0:
                    real_tiles.append(new)
    return real_tiles, visited

def main():
    start_pipe, height, width = parse_input("test5.txt")
    print("part 1")
    current_pipe = start_pipe
    last_dir = 0
    loop_tiles = []
    while current_pipe.letter != "S" or len(loop_tiles) == 0:
        loop_tiles.append(current_pipe)
        if current_pipe.directions[0] == (last_dir + 2) % 4: 
            last_dir = current_pipe.directions[1]
            current_pipe = current_pipe.return_adj_pipe(1)
        else:
            last_dir = current_pipe.directions[0]
            current_pipe = current_pipe.return_adj_pipe(0)

    print(len(loop_tiles)//2)
    
    print("part 2")
    new_loop = double_map (loop_tiles)
    outside, visited = bfs([0,0], new_loop, height, width)
    #Just draw BIG map
    result = 0
    for y in range(-1,2*height+1):
        line = ""
        for x in range(-1,2*width+1):
            if [x,y] in new_loop:
                if x%2==0 and y%2==0:
                    line += pipes[x//2, y//2].letter
                else:
                    line += "*"
            elif [x,y] in visited:
                line += ","
            elif x%2 == 0 and y%2 == 0:
                line += "+"
                result += 1
            else:
                line += "."
        print(line)

    print(result)
    print (len(outside))
    print (f"{width} {height}")
    print ((width+1)*(height+1) - len(outside) - len(loop_tiles))



if __name__ == "__main__":
    main()