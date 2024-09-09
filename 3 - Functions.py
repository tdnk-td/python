# BOOT.DEV - "Learn Python" - Function

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 3.1 - Functions
question(3.01, "Functions")
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
format()

# 3.2 - Functions Review
question(3.02, "Functions Review", 3.04)
print("Q: Which happens first?")
print("A: The function is defined\n")
print("Q: Of the choices, which step happens last?")
print("A: A value is returned from the function\n")
print("Q: Why is the variable called 'radius' outside the function, but 'r' inside the function?")
print("A: Because only the value of the variable is passed to the function. It is then assigned to a new variable called 'r'")
format()

# 3.5 - Multiple Parameters
question(3.05, "Multiple Parameters")
def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total


# Don't touch below this line

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")
format()

# 3.6 - Where to Declare Functions
question(3.06, "Where to Declare Functions")
def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()
format()

# 3.7 - 3.9 Order of functions
question(3.07, "Order of functions", 3.09)
print("Q: Functions must be _____ before they can be _____")
print("A: defined, called\n")
print("Q: Functions must be defined in the same order they call one another")
print("A: False\n")
print("Q: Which is best practice to make sure you don't define functions out of order?")
print("A: Create an entrypoint function (usually called 'main') and call it at the end of the file")
format()

# 3.10 - Functions Practice - Degrees
question(3.10, "Functions Practice - Degrees")
def to_celsius(f):
    c = 5/9 * (f - 32)
    return c

## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
format()

# 3.11 - 3.13 - Function Quiz
question(3.11, "Function Quiz", 3.13)
print("Q: Which keyword is used to create functions in Python?")
print("A: def\n")
print("Q: Which is NOT an alternative term for values that are passed into a function?")
print("A: slots\n")
print("Q: A function must be defined _____ to be called many times with different arguments.")
print("A: once\n")
format()

# 3.14 - Hours to Seconds
question(3.12, "Hours to Seconds")
def hours_to_seconds(hours):
    hours *= 60 * 60
    return hours


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)
format()

# 3.15 - 3.16 - None Return
question(3.15, "None Return", 3.16)
print("Q: What happens if there is no 'return' line in a function")
print("A: It returns None\n")
print("Q: What's the difference between printing a value and returning it?")
print("A: Print: Shows a value in the console. Return: Makes a value available to the caller of the function")
format()

# 3.17 - Multiple return values
question(3.17, "Multiple return values")
def become_warrior(first_name, last_name, power):
    warrior = f"{first_name} {last_name} the warrior"
    power += 1
    return warrior, power
# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(input1, input2, input3):
    result1, result2 = become_warrior(input1, input2, input3)
    print(result1, "has a power level of:", result2)


main()
format()

# 3.18 - 3.19 Parameters vs Arguments
question(3.18, "Parameters vs Arguments", 3.19)
print("Q: ____ are the values that are passed into the function by the caller")
print("A: Arguments\n")
print("Q: ____ are the inputs specified by the function definition")
print("A: Parameters")
format()

# 3.20 - Default values for function arguments
question(3.20, "Default values for function arguments")
def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


# Don't touch below this line


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")


test(400, 5)
test(300, 3)
test(200, 1)
format()

# 3.21 - Printing vs Returning
question(3.21, "Printing vs Returning")
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
format()

# 3.98 - Curse
question(3.98, "[C1] Curse")
def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25

    return lesser_cursed, greater_cursed


# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()
format()

# 3.99 - Enchant and Attack
question(3.99, "Enchant and Attack")
def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health


# Don't modify below this line


def test(target_health, damage, weapon):
    print("The target has", target_health, "health.")
    print(weapon, "base damage:", damage, "Enchanting and attacking")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print("The target has been attacked with the", enchanted_weapon)
    print("The target has", new_health, "health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()


