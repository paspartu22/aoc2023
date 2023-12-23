import timeit

slopes = {'>' : 0, '^' : 1, '<' : 2, 'v': 3}
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

class Cell:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.is_wall = (char == "#")
        self.is_slope = (char in slopes)
        self.slope_dir = slopes[char] if self.is_slope else None
        self.neibours = []
    
    def connect_graph(self):
        for i,dir in enumerate(directions):
            xy = (self.x + dir[0], self.y + dir[1])
            if (xy in cells and 
                (not cells[xy].is_wall and 
                (not cells[xy].is_slope or 
                (cells[xy].slope_dir + i)%4 != 2))):
                self.neibours.append(cells[xy])
        
def dp (cell, path, end, len):
    if cell == end:
        return len
    else:
        len += 1
        path.append(cell)
        path_array = []
        for neibour in cell.neibours:
            if neibour not in path:

        path_array.append(dp(neibour, path, end, len))
        return (path_array)

cells = {}
def parse_input(file):
    with open(file, "r") as file:    
        width = 0
        height = 0
        for y,line in enumerate(file):
            width = len(line.strip())
            height += 1
            for x, char in enumerate(line.strip()):
                cells[x, y] = Cell(x, y, char)
        return width, height
    
def main():
    width, height = parse_input("test.txt")
    for cell in cells.values():
        cell.connect_graph()
    result = dp(cells[1,0], [], cells[width-2, height-1], 0)
    for res in result:
        print(res)
    
    '''for y in range(height):
        line = ""
        for x in range(width):
            line += cells[x, y].char
        print(line)
    '''
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")