# BOOT.DEV - "Learn Python" - Comparison - CHAPTER 7

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 7.1 - Comparison Operators
def player_1_wins(player_1_score, player_2_score):
    result = player_1_score > player_2_score
    return result

# 7.2 - Comparison Operator Evaluations
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# 7.3 - Comparison Practice
def can_withstand_blow(hero_armor, enemy_damage):
    blow = hero_armor >= enemy_damage
    return blow

# 7.4 - If Statements
question(7.04, "If Statements")
def print_status(player_health):
    if (player_health == 0):
        print("dead")
    print("status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(3)


main()
