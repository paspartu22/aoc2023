import timeit


modules = {}
transmitions = []

class Module:
    def __init__(self, line, rx = False) -> None:

        line = line.split(' -> ')
        if line[0][0] == '%' or line[0][0] == '&':
            self.type = line[0][0]
            self.name = line[0][1:]
        else:
            self.type = None
            self.name = line[0]
        self.rx = rx
        if not rx:
            self.targets_names = line[1].strip().split(", ")
        else:
            self.targets_names = []

        self.module_done = False
        self.targets = []
        self.state = False
        self.inputs = {}
        
    def connect(self):
        for target in self.targets_names:
            if target not in modules:
                modules[target] = Module(f"{target} -> ", True)
            self.targets.append(modules[target])
        for module in modules.values():
            for target in module.targets_names:
                if target == self.name:
                    self.inputs[module.name] = 0
    
    def send(self, signal, sender):
        if self.rx:
            return 0            
        elif self.name == 'broadcaster':
            for target in self.targets:
                #transmitions.append([self.name[:3], signal, target.name])
                yield (target.name, signal, self.name)
        elif self.type == '%' and signal == 0:
            self.state = 1^self.state
            for target in self.targets:
                #transmitions.append([self.name[:3], self.state, target.name])
                yield (target.name, self.state, self.name)
        elif self.type == '&':
            self.inputs[sender] = signal
            if set(self.inputs.values()) == {1}:
                for target in self.targets:
                    #transmitions.append([self.name[:3], 0, target.name])
                    yield(target.name, 0, self.name)
            else:
                for target in self.targets:
                    #transmitions.append([self.name[:3], 1, target.name])
                    yield (target.name, 1, self.name)

            
    def __str__(self) -> str:
        return f"{self.type} {self.name} {self.targets_names} {self.inputs}"
    

    

    
def main():
    modules = parse_input("data.txt")
    names = modules.copy().keys()
    modules['broadcaster'].inputs= {'but' : 1}
    for name in names:
        modules[name].connect()
        print(f"{name} {modules[name]}")
    modules['rx'].connect()
    print()
    part_1()
              

def parse_input(file):
    with open(file, "r") as file:
        for line in file:
            name = line.split(' -> ')[0]
            if name[0] == '%' or name[0] == '&':
                modules[name[1:]] = Module(line)
            else:
                modules[name] = Module(line)
        return modules
    
def part_1():
    results = {'kr':[], 'kf':[], 'qk':[], 'zs':[]}
    for i in range(1_000_00):    
        #if i%1000 == 0:
            #print(i%1000*1000, end='\r')
        transmitions.append(["but", 0, "bro"])
        queue = [['broadcaster', 0, 'button']]
        while queue:
            now = queue.pop(0)     
            result = list(modules[now[0]].send(now[1], now[2]))
            if now[0] == 'gf' and now[1] == 1:
                #print()
                print(f"{i} {modules[now[0]].inputs}")
                #print()
                results[now[2]].append(i)
            queue.extend(result)
    for item in results.items():
        print(item)
    '''
    count_0 = 0
    count_1 = 0
    for transmition in transmitions:
        if transmition[1] == 0:
            count_0 += 1
        else:
            count_1 += 1
        #print(transmition)
    print(len(transmitions))
    print(count_0)
    print(count_1)
    print(count_0*count_1)
    '''
    
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")