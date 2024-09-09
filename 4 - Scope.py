# BOOT.DEV - "Learn Python" - Scope

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 4.1 - Scope
question(4.01, "Scope")

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")
format()

# 4.2 - Global Scope
question(4.02, "Global Scope")
player_level = 4

# Don't touch below this line


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
format()

# 4.3 - 4.4 - Scope Quiz
question(4.03, "Scope Quiz", 4.04)
print("Q: Can functions access variables declared in the global scope?")
print("A: Yes\n")
print("Q: Can code outside the scope of a function access variables that are defined inside that function?")
print("A: No")

