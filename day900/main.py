import timeit

def parse_input(file):
    with open(file, "r") as file:
        for line in file:
            pass
        
def main():
    parse_input("test.txt")

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Time {timeit.default_timer()-start_time}")