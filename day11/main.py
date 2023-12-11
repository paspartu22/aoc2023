def parse_input(file):
    with open(file, "r") as file:
        galaxies = []
        empty_rows = []
        empty_cols = None
        for y,line in enumerate(file):
            
            if empty_cols is None:
                empty_cols = [i for i in range(len(line))]
            
            if "#" not in line:
                empty_rows.append(y)
            for x,letter in enumerate(line):
                if letter == "#":
                    galaxies.append([x,y])
                    if x in empty_cols:
                        empty_cols.pop(empty_cols.index(x))
        return galaxies, empty_rows, empty_cols
            
def expand (galaxies, empty_cols, empty_rows, expand_multiplier):
    for i in range(len(galaxies)):
        j = len([1 for col in empty_cols if col < galaxies[i][0]]) 
        galaxies[i][0] += j*(expand_multiplier-1)
        
        j = len([1 for row in empty_rows if row < galaxies[i][1]])
        galaxies[i][1] += j*(expand_multiplier-1)
    return galaxies
        
def sum_all(galaxies):
    sum = 0
    for i,start in enumerate(galaxies):
        for end in galaxies[i:]:
            sum += abs(end[0]-start[0]) + abs(end[1]-start[1])
    return sum

def main():
    expand_multiplier = 2
    expand_multiplier = 1_000_000 
    galaxies, empty_rows, empty_cols  = parse_input("data.txt")
    galaxies = expand(galaxies, empty_cols, empty_rows, expand_multiplier)
    print(sum_all(galaxies))
    
if __name__ == "__main__":
    main()