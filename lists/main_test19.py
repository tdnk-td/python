# MAIN TESTING FOR 9.C4
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lists import *

run_cases = [
    (
        ["A", "B", "C", "D", "E"],
        ["Dellbi", "A", "B", "C", "D", "E"],
        ("Dellbi", 100.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Kaladin", "A", "X", "C", "D", "E"],
        ("Kaladin", 80.0),
    ),
]

submit_cases = run_cases + [
    (
        ["A", "B", "C", "D", "E"],
        ["ShadowWalker", "X", "X", "X", "X", "X"],
        ("ShadowWalker", 0.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Jamie", "A", "B", "X", "X", "E"],
        ("Jamie", 60.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Odium", "A", "B", "C", "D", "E"],
        ("Odium", 100.0),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nexpected_path: {input1}\ncharacter_path: {input2}")
    print(f"Expecting: {expected_output}")
    result = validate_path(input1, input2)
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
