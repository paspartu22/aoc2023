def find_next_number(valve):
    numbers = [valve]
    new_array = []
    while len(set(new_array)) != 1:   
        new_array = [] 
        for i in range(len(numbers[-1])-1):
            new_array.append(numbers[-1][i+1] - numbers[-1][i])
        numbers.append(new_array)
        
    new_last_number = 0
    new_first_number = 0
    for i,line in enumerate(numbers):
        new_last_number += line[-1]
        new_first_number += line[0] if i%2 == 0 else -line[0]
        
    return new_first_number, new_last_number
        
def parse_input(file):
    valves = []
    with open(file, "r") as file:
        for line in file:
            valve = line.strip().split()
            valve = [int(num) for num in valve]
            valves.append(valve)
    return (valves)

def main():
    valves = parse_input("data.txt")
    result_part_1 = 0
    result_part_2 = 0 
    for valve in valves:
        result_1, result_2 = find_next_number(valve)
        print(f"{result_1} {result_2}")
        result_part_1 += result_1
        result_part_2 += result_2
    print(result_part_1)
    print(result_part_2)
if __name__ == "__main__":
    main()