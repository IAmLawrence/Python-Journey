def print_triangle(num_row):
    for i in range(1, num_row+1):
        if i == 1 or i == 2 or i == num_row:
            print("*" * i)
        else:
            print("*" + (" " * (i - 2)) + "*")


print_triangle(10)

