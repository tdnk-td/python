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
format()

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
        
# 7.10 - Boolean Quiz
question(7.10, "Boolean Quiz")

is_tall = True
is_fat = True
is_skinny = False
is_short = False
result = (is_tall and is_fat) or (is_skinny and is_short)
# (is_tall and is_fat) = True
# (is_skinny and is_short) = False
# Since or has one true, therefore True [1 or 0] = 1
print("Q: Boolean Quiz")
print(f"A: {result} ")

# 7.11 - Should Serve Drinks
def should_serve_customer(customer_age, on_break, time):
    if (customer_age >= 21 and on_break == False and time >= 5 and time <= 10): # if 5 <= time <= 10:
        return True
    else:
        return False
    
# 7.97 - [C1] Mount Rental
def check_mount_rental(time_used, time_purchased):
    if (time_used >= time_purchased):
        return "overtime charged"
    else:
        return "no charges yet"
    
# 7.98 - [C2] Combat Advantage
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if (player_power > enemy_defense):
        advantage = True
    elif (player_power < enemy_defense):
        disadvantage = True
    else: # elif (player_power == enemy_defense):
        evenly_matched = True

    return advantage, disadvantage, evenly_matched

# 7.99 - [C3] Race
def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    total_dist = distance_one_way * 2
    energy_needed = energy_available * meters_per_energy
    if (energy_needed >= total_dist):
        return True
    else:
        return False