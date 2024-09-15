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

