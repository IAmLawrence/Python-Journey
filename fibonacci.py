user_inp = int(input("Enter number: "))
prev_num = 0
curr_num = 1
result = [prev_num]

for _ in range(user_inp - 1):
    next_num = prev_num + curr_num
    prev_num, curr_num = curr_num, next_num
    result.append(next_num)

print("Result: ", result)
