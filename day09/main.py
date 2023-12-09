def find_next_number(valve):
    old_array = valve
    new_array = []
    new_first_number = old_array[0]
    new_last_number = old_array[-1]
    line_num = 1
    
    while len(set(new_array)) != 1:   
        new_array = [] 
        for i in range(len(old_array)-1):
            new_array.append(old_array[i+1] - old_array[i])
        new_last_number += new_array[-1]
        new_first_number += new_array[0] if line_num%2 == 0 else -new_array[0]
        old_array = new_array
        line_num += 1
        
    return new_first_number, new_last_number
        
def parse_input(file):
    valves = []
    with open(file, "r") as file:
        for line in file:
            valve = line.strip().split()
            valves.append([int(num) for num in valve])
    return valves

def main():
    valves = parse_input("data.txt")
    results = []
    for valve in valves:
        results.append(find_next_number(valve))
    print(sum([result[0] for result in results]))
    print(sum([result[1] for result in results]))
if __name__ == "__main__":
    main()