import timeit
rep_map = {'.' : '#', '#' : '.'}

def parse_input(file):
    with open(file, "r") as file:
        mirrors = [x.split("\n") for x in file.read().split("\n\n")]
        return mirrors
        
def check_vertical(mirror):
    result = [x for x in range(1, len(mirror[0]))]
    for line in mirror:
        #print(f"line {line}")
        temp_result = result.copy()
        for placement in temp_result:
            #print(f"place {placement}")
            left = placement
            right = len(line)-placement
            compare_size = min(left, right)
            left_side = line[placement-compare_size : placement]
            right_side_m = line[placement+compare_size - 1 : placement - 1 : -1]
            if left_side != right_side_m:
                #print(f"remove {placement}")
                result.pop(result.index(placement))
            #print(f"size {compare_size}")
            #print(f"left side  {left_side}")
            #print(f"right side {right_side_m}")
            #print()

    return result if result else [0]

def log(message = ""):
    print(message)

def check_horisontal(mirror):
    result = []
    #log(mirror)
    for placement in range(1,len(mirror)):
        left = placement
        right = len(mirror) - placement
        compare_size = min(left, right)
        left_side = mirror[placement - compare_size : placement]
        right_side_m = mirror[placement + compare_size - 1 : placement - 1 : -1]
        #log(f"size {compare_size}")
        #log(f"left side  {left_side}")
        #log(f"right side {right_side_m}")
        #log()
        if left_side == right_side_m:
            result.append(placement)
    
    return result if result else [0]

def premutate_mirror(mirror, original_h, original_v):
    for row in range(len(mirror)):
        for col in range(len(mirror[0])):
            mirror[row] = mirror[row][:col] + rep_map[mirror[row][col]] + mirror[row][col+1:]
            #for p_row in range(len(mirror)):
            #
            #log(mirror[p_row])
            
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
                
            log(f" {row} {col} {result_v} {result_h}")
            #log()
            if result_v[0] == 0 and result_h[0] != 0 and len(result_h) == 1  :
                print(f"mirror {result_v[0]} {result_h[0]}")
                result_t = result_h[0]* 100 + result_v[0]  
                print(result_t)
                #result += result_t
                return result_t
            elif result_h[0] == 0 and result_v[0] != 0 and len(result_v) == 1:
                print(f"mirror {result_v[0]} {result_h[0]}")
                result_t = result_h[0]* 100 + result_v[0]
                print(result_t)
                #result += result_t
                return result_t
                    
            mirror[row] = mirror[row][:col] + rep_map[mirror[row][col]] + mirror[row][col+1:]
    input()
    return 0

def main():
    mirrors = parse_input("data.txt")
    result = 0
    for i, mirror in enumerate(mirrors):

        original_v = check_vertical(mirror)[0]
        original_h = check_horisontal(mirror)[0]
        print(f"\n{i} {original_v} {original_h}")
        result += premutate_mirror (mirror, original_h, original_v)


    print(result)
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")