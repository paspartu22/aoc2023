import numpy as np

directions = {'L' : 0,
              'R' : 1}

def parse_input(file):
    with open(file, "r") as file:
        nodes = {}
        task = file.readline().strip()
        file.readline()
        start_names = []
        for line in file:
            nodes[line[:3]] = [line[7:10],line[-5:-2]]
            if line[2] == 'A':
                start_names.append(line[:3])
        return task, nodes, start_names
    
def main():
    task, nodes, start_names = parse_input("data.txt")
    results = []
    for start in start_names:
        current_node_name = start
        end = False
        i = 0        
        result = []
        while True:
            current_node_name = nodes[current_node_name][directions[task[i%len(task)]]]
            i += 1
            if current_node_name[-1] == 'Z':
                if not end:
                    results.append(np.int64(i))
                    break

    print(results)
    print(np.lcm.reduce(results))
    
if __name__ == "__main__":
    main()
    