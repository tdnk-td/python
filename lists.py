# BOOT.DEV - "Learn Python" - Lists - CHAPTER 9

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 9.1 - Loops
question(9.01, "Lists")
def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet","Shortsword"]


# Don't edit below this line


def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()


main()
format()

# 9.2 - 9.4 - Lists Continued
question(9.02, "Lists Continued")
print("Q: When would you declare a list on multiple lines?")
print("A: When there are many items and it's hard to read them all on one line\n")
print("Q: Which types can be stored in a list?")
print("A: All of them\n")
print("Q: Which index refers to the second item in a list?")
print("A: 1\n")

# 9.5 # Index into Lists
def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

# 9.6 - List length
def get_last_index(inventory):
    return len(inventory) - 1

# 9.7 - List Updates
def smelt_ore(inventory):
    if (inventory[0] == "Iron Ore" or inventory[1] == "Iron Ore"): # If Iron Ore is in within the first 2 slots, convert
        inventory[1] = "Iron Bar"

    return inventory

# 9.8 - Appending in Python
def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# 9.9 - Pop Values
question(9.09, "Pop Values")
def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
format()

# 9.10 - Counting the items in a list
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if (items[i] == "Potion"):
            potion_count += 1
        elif (items[i] == "Bread"):
            bread_count += 1
        elif (items[i] == "Shortsword"):
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

# 9.11 - 9.12 - No-index Syntax
question(9.11, "No-Index Syntax", 9.12)
print("Q: When should we use the no-index syntax?")
print("A: When we don't need to know the index, just the value\n")
print("Q: Which method of writing for-loops is considered more 'clean' assuming you don't need the index?")
print("A: for item in items")
format()

# 9.13 - Find an item in a list
def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if (item == "Leather Scraps"):
            found = True

    # don't touch below this line

    return found

# 9.14 - Find the Increase
question(9.14, "Find the Increase")
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if (old_character_levels[i] < new_character_levels[i]):
            # print(i) This is what boot.dev wanted, I just added additional formating underneath
            print(f"Level increased at index {i} from {old_character_levels[i]} to {new_character_levels[i]}")


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()
format()

# 9.15 - Find Max
def find_max(nums):
    max_so_far = float("-inf")
    
    for i in range(0, len(nums)):
        if (nums[i] > max_so_far): # If the number is greater than the max so far, set it to max_so_far
            max_so_far = nums[i]

    return max_so_far

# 9.16 - Modulo operator in Python
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if (i % 2 != 0): # If the remainder of i divided by 2 is not equal to 0
            odd_numbers.append(i)
            
    # don't touch below this line

    return odd_numbers

# 9.17 - Slicing list
def get_champion_slices(champions):
    value1 = champions[2:] # From index 3 to the end
    value2 = champions[:-2] # From the beginning to index -3
    value3 = champions[::2] # From the beginning to the end, in steps of 2
    return value1, value2, value3

# 9.18 - List Operations - Concatenate
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favorites = favorite_weapons + favorite_armor + favorite_items
    return favorites

# 9.19 - List Operations - Contains
def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    if (weapon in top_weapons):
        return True
    else:
        return False
    
# 9.20 - List Deletion
def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:] # Last 2 items
    return strongholds

# 9.21 - Tuples
question(9.21, "Tuples")
def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False)
    ]

    return heroes


# Don't touch below this line


def test():
    heroes = get_heroes()
    for hero in heroes:
        print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")


def main():
    test()


main()
format()

# 9.22 - First Element
def get_first_item(items):
    if not items: # If the list is empty
        return "ERROR"
    else:
        return items[0]
    
# 9.23 - Reverse List
def reverse_array(items):
    return items[::-1] # Reverses the list

# 9.24 - Filter Messages
def filter_messages(messages):
    # Create the two empty lists to return at the end
    filtered_messages = []
    words_removed_counts = []

    # Iterate over each message in the input list
    for message in messages:
        words = message.split()  # Split the message into words
        not_bad_word = []  # Create a new list for non-bad words
        bad_word_count = 0  # Counter for removed words

        for word in words:
            if word == "dang":  
                bad_word_count += 1
            else:
                not_bad_word.append(word)  # If not 'dang', add to non-bad words list

        clean_message = " ".join(not_bad_word)
        filtered_messages.append(clean_message)  # Append the clean message to the filtered list
        words_removed_counts.append(bad_word_count)  # Append the count of removed words

    return filtered_messages, words_removed_counts

# 9.25 - Evens and Odds
def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line

    for number in numbers:
        if number % 2 == 0: # If the number is even
            num_evens += 1
        else:
            num_odds += 1
            
    return num_odds, num_evens
