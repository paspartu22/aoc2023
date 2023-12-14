import timeit
rep_map = {'.' : '#', '#' : '.'}

def parse_input(file):
    with open(file, "r") as file:
        mirrors = [x.split("\n") for x in file.read().split("\n\n")]
        return mirrors
        
def check_vertical(mirror):
    result = [x for x in range(1, len(mirror[0]))]
    for line in mirror:
        temp_result = result.copy()
        for placement in temp_result:
            compare_size = min(placement, len(line)-placement)
            left_side = line[placement-compare_size : placement]
            right_side_m = line[placement+compare_size - 1 : placement - 1 : -1]
            if left_side != right_side_m:
                result.pop(result.index(placement))
    return result if result else [0] #return list of all possible mirrors else [0]

def check_horisontal(mirror):
    result = []
    for placement in range(1,len(mirror)):
        compare_size = min(placement, len(mirror) - placement)
        left_side = mirror[placement - compare_size : placement]
        right_side_m = mirror[placement + compare_size - 1 : placement - 1 : -1]
        if left_side == right_side_m:
            result.append(placement)
    return result if result else [0] #return list of all possible mirrors else [0]

def premutate_mirror(mirror, original_h, original_v):
    for row in range(len(mirror)):
        for col in range(len(mirror[0])):
            mirror[row] = mirror[row][:col] + rep_map[mirror[row][col]] + mirror[row][col+1:]

            result_v = check_vertical(mirror)  
            result_h = check_horisontal(mirror)
            if original_h in result_h:
                result_h.remove(original_h)
                if not result_h:
                    result_h = [0] 
            if original_v in result_v:
                result_v.remove(original_v)
                if not result_v:
                    result_v = [0]
                
            if (result_v[0] == 0 and result_h[0] != 0 and len(result_h) == 1 or 
                result_h[0] == 0 and result_v[0] != 0 and len(result_v) == 1) :
                return result_h[0]*100 + result_v[0] #found mirror              
            mirror[row] = mirror[row][:col] + rep_map[mirror[row][col]] + mirror[row][col+1:]
            
    input("Error, mirror not found")
    return 0

def main():
    mirrors = parse_input("data.txt")
    part_1_result = 0
    part_2_result = 0
    for mirror in mirrors:
        original_v = check_vertical(mirror)[0]
        original_h = check_horisontal(mirror)[0]
        part_1_result += original_h*100 + original_v
        part_2_result += premutate_mirror (mirror, original_h, original_v)

    print(f"part 1 {part_1_result}")
    print(f"part 2 {part_2_result}")

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {str((timeit.default_timer()-start_time))[:7]} sec")