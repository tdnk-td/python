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

# 8.95 - [C1] Match Countdown
def countdown_to_start():
    for i in range(10,1, -1):
        print(f"{i}...")
    print("1...Fight!")
#        if(i == 1):
#            print(f"{i}...Fight!")
# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()

# 8.96 - [C2] Critical Hit

'''def calculate_flurry_crit(num_attacks, base_damage): 
    critical_hit = base_damage * 2
    total_damage = 0
    for i in range (0, num_attacks+1):
        total_damage += critical_hit
        if(i == num_attacks+1):
            total_damage += base_damage * 4
            break
    return total_damage'''
    
# above was my first take then revised to bottom

def calculate_flurry_crit(num_attacks, base_damage):
    critical_hit = base_damage * 2 # critical hits do double the base_damage!
    total_damage = 0 
    
    for i in range(num_attacks):  # Loop for the number of attacks
        
        if (i == num_attacks - 1):  # If it's the last attack
            total_damage += base_damage * 4  # Deal extra damage on the last attack
        else:
            total_damage += critical_hit  # Normal critical hit for each attack
    
    return total_damage

# 8.97 - [C3] Experience Points
def calculate_experience_points(level):
    xp_next = 0
    total_xp = 0
    for i in range(level):
        xp_next += 5
        total_xp += xp_next - 5 # for some reason I had a hard time wrapping my head around this
        
    return total_xp

# 8.98 - [C4] Random Events
def is_prime(number):
    if (number <= 1): # Prime numbers are greater than 1
        return False 
    
    for i in range(2, number // 2 + 1):
        if (number % i == 0): # If divisible by any number other than 1 or itself, it's not prime
            return False 
        
    return True 

# 8.99 - [C5] Meditate
def meditate(mana, max_mana, energy, energy_potions):
    if (energy == 0 and energy_potions > 0): # In case energy starts off as 0 and energy potions are available
        energy += 50
        energy_potions -= 1
    
    # Active Meditate
    while (mana < max_mana) and (energy > 0 or energy_potions > 0): # Mana has to be lower than max, and energy is required
        if (energy == 0 and energy_potions > 0): # When energy depletes, gain 50 energy, lose 1 energy potion
            energy += 50
            energy_potions -= 1
        
        if (energy > 0): # Gain mana if energy is available, and reduce energy by 1 per iteration
            mana += 3
            energy -= 1
            
        if (mana > max_mana): # If mana is going to go over, set to max_mana
            mana = max_mana
        
    return mana, energy, energy_potions
