# ------------- This is the sample of one line of code -------------
# input_num = int(input("Enter Number: "))

list_of_even = [even for even in range(100) if even % 2 == 0]  # <<<<< one line of code, comprehension kung tawagin
print("List of Even Numbers: ", list_of_even)

# ------------- Lambda and sorted function sample -------------
"""
ang lambda is unknown function, pwede mo syang icall within the entire file depende sa logic and usability neto para sayo.
Yung sum_of_num dito hawak na nya or naka store na sa kanya yung lambda function which is
ang purpose ng lambda is to sum any number don sa 2
once na ginamit natin si sum_of_num need nyan ng parameter, yung parameter na yon ia-add nya sa 2
"""

sum_of_num = lambda num: num + 2
print("Sum of num>", sum_of_num(2))

fruits = [
    {
        "name": "Apple",
        "price": 10
    },
    {
        "name": "Grapes",
        "price": 50
    },
    {
        "name": "Mango",
        "price": 20
    },
]

# SORTED, i-arrange nya yung data ascending or descending
lst_of_fruits = sorted(fruits, key=lambda fruits_price: fruits_price["price"], reverse=True)
print("Fruits Sorted Descending: ", lst_of_fruits)

# ------------- map function sample -------------
"""
ginagamit tong map kapag may i-iterate ka sa list, or ireread ka na data sa loob ng list tapos may condition ka.
for ex., yan yung unang gawa mo, niloop yung data sa lst_of_num then ang condition is i-times sa 2 bawat data.
yung result is another list na sya
"""

# lst_of_employees = ["Lawrence", "Belawin", "Lorenz", "Lawin"]
# map_employees = map(lst_of_employees,)

lst_of_nums = [1, 2, 3, 4, 5]

double_the_lst_of_nums = list(map(lambda num: num * 2, lst_of_nums))
print("Double of the list of nums: ", double_the_lst_of_nums)

# Example: Convert a list of strings to uppercase
strings = ["hElLo", "woRld", "pytHon"]
upper_strings = list(map(str.capitalize, strings))
print(upper_strings)

# nums_lst = [num for num in range(10)]
results = list(map(lambda num: num * 2, filter(lambda even_num: even_num % 2 == 0, [num for num in range(10)])))
print("results>", results)

employees_lst = []
age_lst = []
for _ in range(3):
    input_employee = input("Enter employee name: ")
    employees_lst.append(input_employee)

    input_age = int(input("Enter Age: "))
    age_lst.append(input_age)

k_v_results = dict(map(lambda k, v: (k, v), employees_lst, age_lst))
print("k_v_results>", k_v_results)


