replace_map = {'0':'.', '1':'#'}

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

def parse_input(file, folding = 1):
    with open(file, "r") as file:
        input_array = []
        for line in file:
            springs, numbers = line.strip().split()
            input_array.append([((springs+'?')*folding)[:-1], [int(num) for num in ((numbers+',')*folding)[:-1].split(",")]])
        return input_array
def main():
    input_array = parse_input('data.txt')
    sum_result = []
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
        sum_result.append(line_result)
    with open('output.txt', '+a') as file:
        file.write(str(sum_result)[1:-1])
        file.write('\n')
    print(sum(sum_result))
        
if __name__ == "__main__":
    main()