import timeit

categories = {'x':0, 'm':1, 'a':2, 's':3}
pipelines = {}
global_result = []

class Pipeline:
    def __init__(self, line) -> None:
        self.name = line.split('{')[0]
        line = line.split("{")[1][:-1].split(',')
        self.rules = []
        for rule in line[:-1]:
            self.rules.append(Rule(rule))
        self.rules.append(Rule(line[-1], True))

    def process_item(self, item):
        for rule in self.rules:
            result = rule.solve(item)
            if result == 'A' or result == 'R':
                return result
            elif result is not None:
                return pipelines[result].process_item(item)
        
    def process_interval(self, interval):
        remain = interval
        for rule in self.rules:
            if remain:
                result = rule.solve_interval(remain)
                if result[0] == 'A':
                    global_result.append(result[1])
                elif  result[0] != 'R' and result[0] is not None:
                    pipelines[result[0]].process_interval(result[1]) 
                remain = result[2]
            else:
                break

class Rule:
    def __init__(self, line, auto = False) -> None:
        self.auto = auto
        if not auto:
            line = line.split(":")
            self.target = line[1]            
            self.category = categories[line[0][0]]
            self.sign = 1 if line[0][1] == '<' else -1
            self.i_sign = 0 if line[0][1] == '<' else 1
            self.value = int(line[0][2:])
        else:
            self.target = line
    
    def solve(self, item):
        return self.target if self.auto or item[self.category]*self.sign < self.value*self.sign  else None

    def solve_interval(self, interval):
        remain = []
        if self.auto:
            return self.target, interval, remain
        if interval[self.category][0] < self.value < interval[self.category][1]:
            split = [[interval[self.category][0], self.value], [self.value, interval[self.category][1]]]
            remain = interval.copy()
            interval[self.category] = split[self.i_sign]
            interval[self.category][1-self.i_sign] -= self.sign 
            remain[self.category] = split[1-self.i_sign]
        elif self.value < interval[self.category][self.i_sign]:
            remain = interval.copy()
            interval = []

        return self.target, interval, remain

    def __str__ (self):
        return f"{self.auto} {self.category} {self.sign} {self.value} : {self.target}"

def parse_input(file):
    with open(file, "r") as file:
        items = []
        pipelines_str, items_str = file.read().split("\n\n")
        for pipeline in pipelines_str.split('\n'):
            pipelines[pipeline.split("{")[0]] = Pipeline(pipeline)

        for item in items_str.split('\n'):
            items.append([int(x.split("=")[1]) for x in item[1:-1].split(',')])
        return items
    
def main():
    items = parse_input("data.txt")
    result = 0
    for item in items:
        item_result = pipelines['in'].process_item(item)
        #print(item_result)
        result += sum(item) if item_result == 'A' else 0
    print(f"part 1 {result}")

    interval = [[1,4000] for x in range(4)]
    pipelines['in'].process_interval(interval)

    result = 0
    for item in global_result:

        item_result = 1
        for i in range(4):
            item_result *= item[i][1]-item[i][0]+1
        result += item_result
        #print(item)
        #print(item_result)

    print(f"part 2 {result}")
    
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")
