# BOOT.DEV - "Learn Python" - Introduction

def question(num, title, extra=""):
    if extra != "":
        print(f"Chapter {num} - {extra} - {title}:")
    else: 
        print(f"Chapter {num} - {title}:")
        
def format():
    print("\n")

# 1.1 - Welcome to "Learn Python"
question(1.1, "Welcome to Learn Python")
print("Welcome to Fantasy Quest!")
format()


# 1.2 - Fix Your First Bug
question(1.2, "Fix Your First Bug")
sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

# Don't touch below this line
print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred is hit by a sword for {sword_damage} damage...")
print(f"Lollilfred's health is now: {health_after_attack}")
format()

# 1.3 - The Console
question(1.3, "The Console")
print("Use the arrow keys to move")
format()

# 1.4 - 1.5 - What is Python?
question(1.4, "What is Python?", 1.5)
print("Q: Python is NOT often used in...")
print("A: Front-end apps\n")
print("Q: Python is known for being...")
print("A: Simple to read and write")
format()

# 1.6 - What is "Code"?
question(1.6, "What is Code?")
print(250 + 75)
format()

# 1.7 - Multiple Instructions
question(1.7, "Multiple Instructions")
print("Jax: B-Kaw!")
print("Hero: ...")
print("Jax: Where are you off to this morning? Bkaw...")
print("Hero: Where did an owl learn to speak??")
format()

# 1.8 - Syntax Errors
question(1.8, "Syntax Errors")
print("Welcome to Fantasy Quest!")
format()

# 1.9 - 1.10 - Syntax Errors Quiz
question(1.9, "Syntax Errors Quiz", 1.10)
print("Q: What does syntax mean?")
print("A: The rules for valid code in a programming language")

print("Q: What happens if you try to run code with invalid syntax?")
print("A: You'll be provided a syntax error message and the code won't execute")
format()

# 1.C1 - Startup Bug
question(1.11, "Startup Bug")
print("Starting up game server...")
print("local game server is listening on port 8080")
format()

# 1.C2 - Game Statistics
question(1.12, "Game Statistics")
print((250 + 241 + 244 + 255) / 4)
format()

# 1.C3 - Shop Response
question(1.13, "Shop Response")
print("Ah! Great choices...")
print("Is there anything else I can help you with?")
format()



