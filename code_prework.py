# Question 1

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")
hello_name("USERNAME")

# Question 2

def first_odds():
    for digit in range(1,101,2):
        print(digit, end=" ")
    return ""
first_odds
first_odds()

# Question 3

def max_num_in_list(a_list):
    print()
    max_number = max(a_list)
    print(max_number)
list_1 = [1,2,3,4,5,6,7,8,9]
max_num_in_list(list_1)

# Question 4

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(1100))
print(is_leap_year(2024))

# Question 5
 
def is_consecutive(a_list):
    if len(a_list) < 2:
        return True
    for x in range(len(a_list) - 1):
        if a_list[x] + 1 != a_list[x+1]:
            return False
        
    return True
print(is_consecutive([1, 3, 2, 6, 5, 7 ,3]))
print(is_consecutive([1, 2 ,3, 4, 5, 6, 7, 8, 9]))
