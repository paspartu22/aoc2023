digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8",
    "nine" : "9"
}

def find_digits(line):
    new_line = ""
    for letter in range(len(line)):
        if line[letter].isdigit():
            new_line+=line[letter]
        else:    
            for digit in digits:
                if  line[letter : letter + len(digit)] == digit:
                    new_line+=digits[digit]
                    break
    return (new_line)

def solve(filename):
    with open(filename, 'r') as file:
        result = 0
        for line in file:
            line = find_digits(line.strip())
            result += int(line[0])*10 + int(line[-1])
        print(f"answer in {filename} is {result}")

if __name__ == "__main__":
    #solve("test.txt")
    solve("test2.txt")
    solve("input.txt")