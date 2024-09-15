# MAIN TESTING FOR 9.7
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lists import *

run_cases = [
    (
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
    ),
    (["Potion", "Iron Ore", None, None], ["Potion", "Iron Bar", None, None]),
]

submit_cases = run_cases + [
    ([None, None, None, None], [None, None, None, None]),
    (
        [None, "Iron Ore", None, "Leather Armor"],
        [None, "Iron Bar", None, "Leather Armor"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = smelt_ore(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
