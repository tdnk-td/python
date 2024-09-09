# BOOT.DEV - "Learn Python" - Unit Tests - CHAPTER 5

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 5.1 - Unit Tests
def total_xp(level, xp_to_add):
    total = level * 100
    extra = total + xp_to_add
    return extra

# 5.2 - Two Lesson Types
question(5.02, "Two Lesson Types")
print("Q: You can submit ____ lessons with your debugging code.")
print("A: Unit Tests")
format()

# 5.3 - Debugging
def take_magic_damage(health, resist, amp, spell_power):
    maximum_damage = (spell_power * amp) - resist
    health -= maximum_damage
    return health

# 5.4 - 5.5 - Learning Effectively
question(5.04, "Learning Effectively", 5.05)
print("Q: You will be penalized for peeking at the solution after you have successfully completed an assignment.")
print("A: False\n")
print("Q: Temporarily adding print() statements is a good way to...")
print("A: ...quickly test and debug small pieces of code\n")
format()

# 5.7 - Debugging Practice
def unlock_achievement(before_xp, ach_xp, ach_name):
    sum = before_xp + ach_xp
    achievement = f"Achievement Unlocked: {ach_name}"
    return  sum, achievement

# 5.8 - Stack Trace
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
