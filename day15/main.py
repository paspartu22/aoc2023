import timeit

def parse_input(file):
    with open(file, "r") as file:
        return file.readline().strip().split(",")
        
def main():
    items = parse_input("data.txt")
    boxes = {x:[] for x in range(256)}
    lenses = {}
    sum = 0
    for item in items:
        box = 0
        for char in item:
            if char == "=" or char == "-":
                break
            else:
                box = ((box + ord(char))*17)%256
        label = item[:item.index('-')] if '-' in item else item[:item.index('=')]          
                        
        if '=' in item:
            if label not in boxes[box]:
                boxes[box].append(label)
            lenses[(box, label)] = int(item[item.index('=')+1:])
        else:
            if label in boxes[box]:
                boxes[box].remove(label)
                lenses.pop((box, label))   

        print(f"{item} | {box}")
        sum += box

        #for box_p in boxes.items():
        #    if len(box_p[1]) > 0:
        #        print(box_p)
    
    print(sum)
    print("====")
    sum = 0
    for i,box in boxes.items():
        for j,lense in enumerate(box):
            sum += (i+1) * (j+1) * (lenses[(i,lense)])
    print(sum)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")