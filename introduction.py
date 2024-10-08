# BOOT.DEV - "Learn Python" - Introduction - CHAPTER 1

def question(num, title="", extra=""):
    # Format num to always show two decimal places
    formatted_num = f"{num:.2f}"
    
    if extra != "":
        print(f"Chapter {formatted_num} - {extra} - {title}:")
    else: 
        print(f"Chapter {formatted_num} - {title}:")
        
def format():
    print("\n")

# 1.1 - Welcome to "Learn Python"
question(1.01, "Welcome to Learn Python")
print("Welcome to Fantasy Quest!")
format()


# 1.2 - Fix Your First Bug
question(1.02, "Fix Your First Bug")
sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

# Don't touch below this line
print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred is hit by a sword for {sword_damage} damage...")
print(f"Lollilfred's health is now: {health_after_attack}")
format()

# 1.3 - The Console
question(1.03, "The Console")
print("Use the arrow keys to move")
format()

# 1.4 - 1.5 - What is Python?
question(1.04, "What is Python?", 1.5)
print("Q: Python is NOT often used in...")
print("A: Front-end apps\n")
print("Q: Python is known for being...")
print("A: Simple to read and write")
format()

# 1.6 - What is "Code"?
question(1.06, "What is Code?")
print(250 + 75)
format()

# 1.7 - Multiple Instructions
question(1.07, "Multiple Instructions")
print("Jax: B-Kaw!")
print("Hero: ...")
print("Jax: Where are you off to this morning? Bkaw...")
print("Hero: Where did an owl learn to speak??")
format()

# 1.8 - Syntax Errors
question(1.08, "Syntax Errors")
print("Welcome to Fantasy Quest!")
format()

# 1.9 - 1.10 - Syntax Errors Quiz
question(1.09, "Syntax Errors Quiz", 1.10)
print("Q: What does syntax mean?")
print("A: The rules for valid code in a programming language")

print("Q: What happens if you try to run code with invalid syntax?")
print("A: You'll be provided a syntax error message and the code won't execute")
format()

# 1.97 - Startup Bug
question(1.97, "[C1] Startup Bug")
print("Starting up game server...")
print("local game server is listening on port 8080")
format()

# 1.98 - Game Statistics
question(1.98, "[C2] Game Statistics")
print((250 + 241 + 244 + 255) / 4)
format()

# 1.99 - Shop Response
question(1.99, "[C3] Shop Response")
print("Ah! Great choices...")
print("Is there anything else I can help you with?")
format()



