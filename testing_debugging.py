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
question(5.01, "Unit Tests")
def total_xp(level, xp_to_add):
    total = level * 100
    extra = total + xp_to_add
    return extra


format()
