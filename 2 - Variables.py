# BOOT.DEV - "Learn Python" - Variables

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 2.1 - Variables
question(2.01, "Variables")
player_health = 1000

# don't touch below this line

print(player_health)
format()

# 2.2 - Variables Vary
question(2.02, "Variables Vary")
player_health = 1000

# reduce by 100 here
player_health = 900
print(player_health)

# and here
player_health = 800
print(player_health)

# and here
player_health = 700
print(player_health)

# and here
player_health = 600
print(player_health)
format()

# 2.3 - Let's do some math
question(2.03, "Let's do some math")
player_health = 1000
armor_multiplier = 2

# create armored_health here
armored_health = player_health * armor_multiplier
print(armored_health)

# 2.4 - Let's do some more math
question(2.04, "Let's do some more math")
player_health = 100
poison_damage = -10

# don't touch below this line

player_poison_health = player_health + poison_damage

print(player_poison_health)
format()

# 2.5 - Comments
question(2.05, "Comments")
# the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)
format()

# 2.6 - 2.7 - Variable Names
question(2.06, "Variable Names", 2.07)
print("Q: Which is valid camel case?")
print("A: heroHealth\n")
print("Q: Which is valid snake case?")
print("A: hero_health")
format()

# 2.8 - Basic Variable Types
question(2.08, "Best Variable Types")
player_health = 100

player_has_magic = True

# don't touch below this line
print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")
format()

# 2.9 - F-strings in Python
question(2.09, "Comments")
name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")
format()

# 2.10 - NoneType Variables
question(2.10, "NoneType Variables")
# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None)
format()

# 2.11 - NoneType
question(2.11, "NoneType")
print("Q: Why might you use a 'None' value")
print("A: As  the default value that will be replaced later")
format()

# 2.12 - 2.13 - Dynamic Typing
question(2.12, "Dynamic Typing", 2.13)
print("Q: Is changing the type of a variable generally a good idea?")
print("A: No\n")
print("Q: What kind of typing does Python employ?")
print("A: Dynamic")
format()

# 2.14 - Math With Strings
question(2.14, "Math With Strings")
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(f"You have {player1_health} health")
print(f"You have {player2_health} health")

# 2.15 - 2.16 - Multi-Variable Declaration
question(2.15, "Multi-Variable Declaration", 2.16)
# Q: How many variables can be declared on the same line?
# A: No limit

# Q: What is clean code?
# A: Code that is easy for developers to read and understand
format()

# 2.C1 - Quest Output
question(2.97, "[C1] Quest Output")
quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(quest_start)
print(quest_middle)
print(quest_end + space + quest_objective)
format()

# 2.C2 - Battleground Average
question(2.98, "[C2] Battleground Average")
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105
game_five_score = 96
game_six_score = 93
game_seven_score = 104

# Don't touch above this line

average_score = (game_one_score +
game_two_score +
game_three_score +
game_four_score +
game_five_score +
game_six_score  +
game_seven_score) / 7

# Don't touch below this line

print(round(average_score))
format()

# 2.C3 - Character Report
question(2.99, "[C3] Character Report")
level = 25
name = "Lopen"
character_class = "Windrunner"
account_active = True
pvp_rank = "Squire"
max_health = 79
max_mana = 274
armor = 12
magic_resistance = 15.4

print("Character Report")
print(
    f"Character {name} is a level {level} {character_class}. And are currently ranked as a {pvp_rank}."
)
print(f"They have {max_health} max health and {max_mana} max mana.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

# Don't edit below this line

print("Character Report Complete")
print(
    f"Data types {type(level)}, {type(name)}, {type(character_class)}, {type(account_active)}, {type(pvp_rank)}, {type(max_health)}, {type(max_mana)}, {type(armor)}, {type(magic_resistance)}"
)
