import timeit

categories = {'x':0, 'm':1, 'a':2, 's':3}
pipelines = {}

class Pipeline:
    def __init__(self, line) -> None:
        self.name = line.split('{')[0]
        line = line.split("{")[1][:-1]
        line = line.split(',')
        self.rules = []
        for rule in line[:-1]:
            self.rules.append(Rule(rule))
        self.rules.append(Rule(line[-1], True))

    def __str__ (self):
        line = ""
        for rule in self.rules:
            line += str(rule) + '\n'
        return (line)

    def process_item(self, item):
        for rule in self.rules:
            result = rule.solve(item)
            if result == 'A' or result == 'R':
                return result
            elif result is not None:
                return pipelines[result].process_item(item)
        

class Rule:
    def __init__(self, line, auto = False) -> None:
        
        self.auto = auto
        if not auto:
            line = line.split(":")
            self.target = line[1]            
            self.category = categories[line[0][0]]
            self.sign = 1 if line[0][1] == '<' else -1
            self.value = int(line[0][2:])
        else:
            self.target = line
            self.category = None
            self.sign = None
            self.value = None
    
    def solve(self, item):
        return self.target if self.auto or item[self.category]*self.sign < self.value*self.sign  else None

    def __str__ (self):
        return f"{self.auto} {self.category} {self.sign} {self.value} : {self.target}"


def parse_input(file):
    with open(file, "r") as file:
        items = []
        pipelines_str, items_str = file.read().split("\n\n")
        for pipeline in pipelines_str.split('\n'):
            pipelines[pipeline.split("{")[0]] = Pipeline(pipeline)
        #for name, pipe in pipelines.items():
            #print(str(name) + "\n" + str(pipe))

        for item in items_str.split('\n'):
            item = item[1:-1].split(',')
            item = [int(x.split("=")[1]) for x in item]
            items.append(item)
            #print(item)
        return items
    
def main():
    items = parse_input("data.txt")
    result = 0
    for item in items:
        item_result = pipelines['in'].process_item(item)
        #print(item_result)
        result += sum(item) if item_result == 'A' else 0
    print(f"part 1 {result}")
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")