import numpy as np
directions = {'L' : 0, 'R' : 1}

def parse_input(file):
    with open(file, "r") as file:
        task = file.readline().strip()
        file.readline() #skip empty
        start_names = []
        nodes = {}
        for line in file:
            nodes[line[:3]] = [line[7:10], line[-5:-2]]
            if line[2] == 'A':
                start_names.append(line[:3])
        return task, nodes, start_names
    
def main():
    task, nodes, start_names = parse_input("data.txt")
    results = []
    for start in start_names:
        current_node_name = start
        i = 0        
        while True:
            current_node_name = nodes[current_node_name][directions[task[i%len(task)]]]
            i += 1
            if current_node_name[-1] == 'Z':
                results.append(np.int64(i))
                break

    print(results)
    print(np.lcm.reduce(results))
    
if __name__ == "__main__":
    main()
    