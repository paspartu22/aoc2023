import timeit
import numpy as np

directions_num = ['R', 'D', 'L', 'U']
directions = {'R':[1,0], 'U':[0,-1], 'L':[-1,0], 'D':[0,1]}

def parse_input(file):
    with open(file, "r") as file:
        lines = []
        for line in file:
            print(line.strip())
            dir, len, color = line.strip().split()
            p2_len = color[2:-2]
            
            p2_dir = directions_num[int(color[-2])]
            print(f'{p2_dir} {p2_len}')
            print()
            lines.append([directions[dir], int(len), directions[p2_dir], int(p2_len, base = 16)])
        return lines

cells_p1 = []
cells_p2 = []


def shoelace_formula_3(cells, absoluteValue = True):
    x, y = zip(*cells)
    result = np.int64(0)
    result = 0.5 * np.array(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    if absoluteValue:
        return abs(result)
    else:
        return result

def main():
    lines = parse_input("data.txt")
    current_position_p1 = [0, 0]
    current_position_p2 = [np.int64(0), np.int64(0)]
    len_p1 = 0
    len_p2 = 0

    for line in lines:
        print (line)
        len_p1 += line[1]
        current_position_p1[0] += line[0][0]*line[1] 
        current_position_p1[1] += line[0][1]*line[1]
        cells_p1.append(current_position_p1.copy())    

        len_p2 += line[3]
        current_position_p2[0] += (line[2][0])*(line[3]) 
        current_position_p2[1] += (line[2][1])*(line[3])
        cells_p2.append(current_position_p2.copy())    

    for i,item in enumerate(cells_p1):
        print(str(i)+str(item))

    print()
    for i,item in enumerate(cells_p2):
        print(str(i)+str(item))

    print("===")
    print(len_p1)
    print(shoelace_formula_3(cells_p1)+len_p1/2+1)
    print(shoelace_formula_3(cells_p2)+len_p2/2+1)
    
    '''
    for y in range(min_y, max_y):
        line = ""
        for x in range(min_x, max_x):
            if (x, y) in cells:
                line += "#"
            elif (x, y) in visited:
                line += "*"
            else:
                line += "."
        print(line)
    print(len(visited)+len(cells))

    '''
    #952408144115
    #1069685419
    #1069685419
    #1072888050
    
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")

'''
    min_x, max_x, min_y, max_y = get_min_max(lines)
    visited = bfs(cells, (1,1), min_x, max_x, min_y, max_y)

def get_min_max(lines):
    current_position = [0,0]
    for line in lines:
        for i in range(line[1]):
            current_position[0] += line[0][0]
            current_position[1] += line[0][1]
            cells[current_position[0],current_position[1]] = line[2]
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for item in cells.items():
        if item[0][0] > max_x:
            max_x = item[0][0]
        if item[0][0] < min_x:
            min_x = item[0][0]
        if item[0][1] > max_y:
            max_y = item[0][1]
        if item[0][1] < min_y:
            min_y = item[0][1]
        #print (item)
    print (f"{min_x} {max_x} {min_y} {max_y}")
    return min_x, max_x+1, min_y, max_y+1

def bfs(cells, node, min_x, max_x, min_y, max_y): #function for BFS
    visited = [node]
    queue = [node]

    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        print (len(visited)//1000*1000, end = "\r") 
        if m[0] == min_x or m[0] == max_x or m[1] == min_y or m[1] == max_y:
            print("out of min")
            break

        for dir in directions.values():
            if ((m[0] + dir[0], m[1] + dir[1]) not in visited and 
                (m[0] + dir[0], m[1] + dir[1]) not in cells):
                visited.append((m[0] + dir[0], m[1] + dir[1]))
                queue.append((m[0] + dir[0], m[1] + dir[1]))

    return visited

    '''