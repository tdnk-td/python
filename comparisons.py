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

# 7.5 - If Practice
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if (number_of_soldiers == number_of_swords):
        return "correct amount"
    else:
        return "incorrect amount"
    
# 7.6 - If-Else
def player_status(health):
    if (health <= 0):
        return "dead"
    elif (health <= 5):
        return "injured"
    else:
        return "healthy"
    
# 7.7 - If-Else Practice
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name <= high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
    
# 7.8 - If-Else Practice
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if (player_name == high_scoring_player_name):
        return "high"
    elif (player_name == low_scoring_player_name):
        return "low"
    else:
        return "neither"
    
# 7.9 - Boolean Logic
def does_attack_hit(attack_roll, armor_class):
        if (attack_roll != 1 and attack_roll >= armor_class or attack_roll == 20):
            return True
        else:
            return False