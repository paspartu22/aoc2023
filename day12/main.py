replace_map = {'0':".", '1':"#"}

def parse_input(file):
    with open(file, "r") as file:
        input_array = []
        for line in file:
            springs, numbers = line.strip().split()
            input_array.append([springs, [int(num) for num in numbers.split(",")]])

        return input_array
    


def dfs(line, nums, char_counter, num_counter, running_spring_counter):
    #print(f"{int(char_counter/len(line)*100)}")
    num_of_ways = 0
    if line[char_counter] == "#":
        running_spring_counter += 1
        if num_counter == len(nums) or running_spring_counter > nums[num_counter]:
            return 0
    elif running_spring_counter != 0:
        if num_counter == len(nums) or running_spring_counter != nums[num_counter]:
            return 0
        else:
            running_spring_counter = 0
            num_counter += 1
    if char_counter == len(line)-1:
        if num_counter == len(nums):
            #print (f"{line} {nums}")
            #input()
            return 1
        else:
            return 0
        
    if line[char_counter+1] == "?":
        temp_line = line
        num_of_ways += dfs(line.replace('?', '#', 1), nums, char_counter+1, num_counter, running_spring_counter)
        num_of_ways += dfs(temp_line.replace('?', '.', 1), nums, char_counter+1, num_counter, running_spring_counter)
    else:
        num_of_ways += dfs(line, nums, char_counter+1, num_counter, running_spring_counter)
    return num_of_ways 

def main():
    input_array = parse_input("test.txt")
    sum_result = 0
    for input in input_array:
        line = input[0]
        nums = input[1].copy()
        for i in range(4):
            input[0] += '?'+line
            for num in nums:
                input[1].append(num)
        print(input)   
        result = 0
        input[0] += "."
        if input[0][0] == "?":
            temp_line = input[0]
            result += dfs(input[0].replace('?', '#', 1), input[1], 0, 0, 0)
            result += dfs(temp_line.replace('?', '.', 1), input[1], 0, 0, 0)
        else:
            result += dfs(input[0], input[1], 0, 0, 0)
        print(result)
        sum_result += result
    print("result")
    print(sum_result)

if __name__ == "__main__":
    main()

    ''' part 1
    def check_variant(line, nums):
    char_counter = 0
    num_counter = 0
    line += '.'
    for char in line:
        if char == "#":
            char_counter += 1

        elif char_counter != 0:
            if num_counter == len(nums) or char_counter != nums[num_counter]:
                return False
            else:
                char_counter = 0
                num_counter += 1
    return num_counter == len(nums)

    for line in input_array:
        print(line)
        line_result = 0
        for i in range(2**line[0].count('?')):
            temp_line = line[0]
            num = str(bin(i)[2:]).zfill(temp_line.count('?'))
            for digit in num:
                temp_line = temp_line.replace('?',replace_map[digit], 1)

            if check_variant(temp_line, line[1]):
                line_result += 1
                print(f"+ {temp_line} {line[1]}")
            else:
                pass
                #print(f"- {temp_line} {line[1]}")
        print(line_result)
        print()
        sum_result += line_result
    

    '''