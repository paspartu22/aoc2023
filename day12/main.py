import timeit

def parse_input(file, folding = 1):
    with open(file, "r") as file:
        input_array = []
        for line in file:
            springs, numbers = line.strip().split()
            input_array.append([((springs+'?')*folding)[:-1], [int(num) for num in ((numbers+',')*folding)[:-1].split(",")]])
        return input_array
    
DP = {}
def dp(line, nums, char, num, current):
    key = (char, num, current)
    if key in DP:
        return DP[key]
    if char == len(line):
        if num == len(nums) and current == 0:
            return 1
        elif num == len(nums)-1 and current == nums[-1]:
            return 1
        else:
            return 0
        
    result = 0
    for new_char in ['.', '#']:
        if line[char] == new_char or line[char] == '?':
            if new_char == '.' and current == 0:
                result += dp(line, nums, char+1, num, 0)
            elif new_char == '.' and num < len(nums) and current == nums[num]:
                result += dp(line, nums, char+1, num+1, 0)
            elif new_char == '#':
                result += dp(line, nums, char+1, num, current+1)
    DP[key] = result
    return result

def main():
    start_time = timeit.default_timer()
    input_array = parse_input("data.txt", 5)
    sum_result = 0
    for i,line in enumerate(input_array):
        DP.clear()
        result = dp(line[0], line[1], 0, 0, 0)
        #print(f'{i} {line}')  
        #print(result)
        #print(f"Time {timeit.default_timer()-start_time}")
        sum_result += result
        
    print("result")
    print(sum_result)
    stop_time = timeit.default_timer()
    print(f"Time {stop_time-start_time}")

if __name__ == "__main__":
    main()