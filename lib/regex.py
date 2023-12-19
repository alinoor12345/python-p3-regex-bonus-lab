import re

my_pattern = r"^\s*It's such a lovely day today\.|^\s*Some weather we're having today, huh\?|^\s*Maybe today's just not my day\."

my_regex = re.compile(my_pattern)

# Example test strings
test_strings = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
    "This string doesn't match the pattern.",
]

# Test the compiled regular expression
def test_my_regex():
    for test_string in test_strings:
        if my_regex.fullmatch(test_string):
            print(f"Pattern matched in the string: {test_string}")
        else:
            print(f"Pattern not found in the string: {test_string}")

# Run the test function
if __name__ == "__main__":
    test_my_regex()