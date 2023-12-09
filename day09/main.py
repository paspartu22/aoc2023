def find_next_number(valve):
    array = valve
    result = [[array[0]],[array[-1]]]
    
    while len(set(array)) != 1:   
        array = [array[i+1] - array[i] for i in range(len(array)-1)]
        result[0].append(array[0] if len(result[1])%2 == 0 else -array[0])
        result[1].append(array[-1])
    print(result)
    print(f"{sum(result[0])} {sum(result[1])}")
    return sum(result[0]), sum(result[1])
        
def parse_input(file):
    valves = []
    with open(file, "r") as file:
        for line in file:
            valve = line.strip().split()
            valves.append([int(num) for num in valve])
    return valves

def main():
    valves = parse_input("test.txt")
    results = []
    for valve in valves:
        results.append(find_next_number(valve))
    print("\nresult for part 1")
    print(sum([result[0] for result in results]))
    print("result for part 2")
    print(sum([result[1] for result in results]))
    
if __name__ == "__main__":
    main()