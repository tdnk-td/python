# BOOT.DEV - "Learn Python" - Computing - CHAPTER 6

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 6.1 - Python Numbers
def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

# 6.2 - Numbers Review
question(6.02, "Number Review")
print("Q: ____ and ____ are numerical types in Python")
print("A: Integers, Floats\n")

# 6.3 - Floor Division
question(6.03, "Floor Division")
print("Q: What would be the result of 11 // 2 ?")
print("A: 5\n")

# 6.4 - Exponents
question(6.04, "Exponents")
print("Q: What is 2 ** 3?")
print("A: 8")
format()

# 6.5 - Changing in Place
def update_player_score(current_score, increment):
    current_score += increment
    return current_score

# 6.6 - Plus Equals
def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

# 6.7 - Scientific Notation
def max_players_on_server():
    small = 1.024e18 # 1,024,000,000,000,000,000
    medium = 1.024e19 # 10,240,000,000,000,000,000
    large = 1.024e20 # 102,400,000,000,000,000,000
    return small, medium, large

# 6.8 - Logical Operators
question(6.08, "Logical Operators")
print("Q: What does this code statement evaluate to?\n((True and True) or (True and False))")
print("A: True\n")

# 6.9 - 6.11 - Binary Numbers
question(6.09, "Binary Numbers", 6.11)
print("Q: What does the binary number 1100 represent in decimal?")
print("A: 12\n")
print("Q: What does the binary number 1101 represent in decimal?")
print("A: 13\n")
print("Q: What's the largest number you can store in 5 digits of binary?")
print("A: 31")
format()

# 6.12 - Bitwise "&" Operator
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    perms = user_permissions & can_create_guild
    return perms

def get_review_bits(user_permissions):
    perms = user_permissions & can_review_guild
    return perms


def get_delete_bits(user_permissions):
    perms = user_permissions & can_delete_guild
    return perms


def get_edit_bits(user_permissions):
    perms = user_permissions & can_edit_guild
    return perms

# 6.13 - Bitwise "|" Operator
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    perms = glorfindel | galadriel | elendil | elrond
    return perms

# 6.14 - Not
question(6.14, "Not")
print("Q: The operators 'and', 'or', and 'not' are ___ operators?")
print("A: Logical\n")

# 6.98 - Damage Meter
question(6.98, "[C1] Damage Meter")
def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
format()

# 6.99 - Converting Binary
def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers = int(num_servers, 2)
    num_players = int(num_players, 2)
    num_admins = int(num_admins, 2)    
    return num_servers, num_players, num_admins