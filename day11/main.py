galaxies = []
empty_rows = []
empty_cols = []
width = 0
height = 0
expand_multiplyer = 1000000 

def parse_input(file):
    with open(file, "r") as file:
        for y,line in enumerate(file):
            global width 
            width = len(line.strip())
            global height
            height += 1
            if "#" not in line:
                empty_rows.append(y)
            for x,letter in enumerate(line):
                if letter == "#":
                    galaxies.append([x,y])

def find_empty_cols():
    for x in range(width):
        is_empty = True
        for galaxy in galaxies:
            if x == galaxy[0]:
                is_empty = False
                break
        if is_empty:
            empty_cols.append(x)
            
def expand ():
    for i in range(len(galaxies)):
        j = 0
        for row in empty_rows:
            if row < galaxies[i][1]:
                j += 1
        galaxies[i][1] += j*(expand_multiplyer-1)
        j = 0
        for col in empty_cols:
            if col < galaxies[i][0]:
                j += 1
        galaxies[i][0] += j*(expand_multiplyer-1)
        
def find_closest():
    sum = 0
    for start in galaxies:
        for end in galaxies:
            sum += abs(end[0]-start[0]) + abs(end[1]-start[1])
    return sum

def main():
    parse_input("data.txt")
    find_empty_cols()
    expand()
    print(galaxies)
    print(empty_rows)
    print(empty_cols)
    
    '''for y in range(height+len(empty_rows)*expand_multiplyer):
        line = ""
        for x in range(width+len(empty_cols)*expand_multiplyer):
            if [x,y] in galaxies:
                line += "#"
            else:
                line += "."
        print(line)
    '''
    result = find_closest()
    print(result//2)
    

if __name__ == "__main__":
    main()