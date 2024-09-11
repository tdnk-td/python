# BOOT.DEV - "Learn Python" - Loops - CHAPTER 8

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 8.1 - Loops
question(8.01, "Loops")
def print_numbers():
    for i in range(0,100): # 0 - 99
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
format()

# 8.2 - 8.03 - Loops Practice
question(8.02, "Loops Practice", 8.03)
def print_numbers():
    for i in range(0, 200):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()

# 8.03
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()
format()

# 8.04 - Loop Review
question(8.04, "Binary Numbers", 8.06)
print("Q: Why would you want to use a loop?")
print("A: To do the same thing over and over without writing the same code\n")
print("Q: Why does the code on the left print 0-999 and not 0-1000?")
print("A: Because print(i) only happens while i is less than (not equal to) 1000\n")
print("Q: It is ____ to indent the body of a traditional for-loop in Python")
print("A: Required")
format()

# 8.07 - Range Continued
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()

# 8.08 - Sum Game
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

# 8.09 - Sum Game 2
def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

# 8.10 - While
def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
        if (enemy_distance <= 3):
            break
    return current_health