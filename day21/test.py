All_odd = 7567
all_even = 7509

A_1 = 3787
A_2 = 3749
B_1 = 3674
B_2 = 3737

x = 202300

sum = 2*x+1

while x > 0:
    x -= 1
    sum += 2*2*x+2
print(sum)
size = 202300

x = size + 1
for i in range(1, size+1):
    x += 2*i
print(x)

all = 81850984601
A_1_count = 40925694601
B_count = A_1_count - 202300
A_2_count = all-A_1_count
print(A_2_count)
print(A_1*A_1_count + A_2*A_2_count + B_1*B_count + B_2*B_count - 1)