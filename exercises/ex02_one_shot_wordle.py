"""EX02 - One Shot Wordle - A cute step toward Wordle."""

__author__ = "730488727"

# var: secret word, length of secret word, 3 different boxes
SECRET: str = "python"
SECRET_LEN: int = len(SECRET)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

user_guess: str = (str(input(f"What is your { SECRET_LEN }-letter guess? ")))  # obtaining user's guess

# Checking the length of user's input
while len(user_guess) != len(SECRET):
    user_guess = input(f"That was not { SECRET_LEN } letters! Try again: ")

i: int = 0  # green box indexing var
boxes: str = ""  # boxes var
while i < SECRET_LEN:
    if SECRET[i] == user_guess[i]:
        boxes += GREEN_BOX   # add green box if the current char in user's guess is correct
    else:
        i_check: int = 0  # yellow box indexing var
        while (i_check < SECRET_LEN) & (len(boxes) <= i):
            if user_guess[i] == SECRET[i_check]:
                boxes += YELLOW_BOX   # add yellow box if user's guess if the char is in the SECRET
            i_check += 1
        if len(boxes) <= i:
            boxes += WHITE_BOX    # add white box if the char is neither correct nor in the SECRET
    i += 1
print(boxes)
if user_guess == SECRET:
    print("Woo! You got it!")  # congrats message
else:
    print("Not quite. Play again soon!")  # encourage the user to retry