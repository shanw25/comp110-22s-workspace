"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730488727"

input_word: str = input("Enter a 5-character word: ")

if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
    
input_char: str = input("Enter a single character: ")

if len(input_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for e in hello")
char_count: int = 0

if input_word[0] == input_char:
    print(input_char + "found at index 0")
    char_count += 1
if input_word[1] == input_char:
    print(input_char + "found at index 1")
    char_count += 1
if input_word[2] == input_char:
    print(input_char + "found at index 2")
    char_count += 1
if input_word[3] == input_char:
    print(input_char + "found at index 3")
    char_count += 1
if input_word[4] == input_char:
    print(input_char + "found at index 4")
    char_count += 1
if char_count > 0:
    print(str(char_count) + " instance of " + input_char + " found in " + input_word)
else:
    print("No instances of " + input_char + " found in " + input_word)