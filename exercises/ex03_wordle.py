"""EX03 - Wordle game with 6 attempts in total."""

__author__ = "730488727"


def contains_char(secret_word: str, checking_char: str) -> bool:
    """Determain whether the second parameter which is a single character is contained in the first parameter."""
    assert len(checking_char) == 1  # makeing sure the second param's length is 1
    i: int = 0  # indexing var
    word_length: int = len(secret_word)  # length of the secret word in the fisrt param
    while i < word_length:  # checking whether the second param, checking_char, is contained in the first param, secret_word
        if secret_word[i] == checking_char:
            return True  # return True if contained
        i += 1
    return False  # return False if not contained


def emojified(guess: str, secret: str) -> str:
    """Print the emoji boxes which show the status of each character: matched(green), contained(yellow), not contained(white)."""
    assert len(guess) == len(secret)  # making sure the two params have same length
    WHITE_BOX: str = "\U00002B1C"  # three emoji boxes
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0  # indexing var
    boxes: str = ""  # boxes var
    secret_len: int = len(secret)  # length of the secret word
    while i < secret_len:
        if secret[i] == guess[i]:
            boxes += GREEN_BOX   # add green box if the current char in user's guess is correct
        else:
            if contains_char(secret, guess[i]):
                boxes += YELLOW_BOX  # if the current char is contained in the secret word, add yellow box
            else:
                boxes += WHITE_BOX  # if the current char is not contained in the secret word, add white box
        i += 1
    return boxes  # the final boxes are retured, length of the boxes is equal to the length of the secret word

    
def input_guess(length: int) -> str:
    """Obtaining users guess with similar length as the secret word."""
    guess: str = input(f"Enter a {length} character word: ")  # obtaining user's guess
    while length != len(guess):
        guess = input(f"That wasn't {length} chars! Try again: ")  # while the length is not equal to the secret word, asking the user for another input
    return guess  # guessed word with correct length is returned


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"  # secret word
    win: bool = False  # var tracking whether the user has win
    tried: int = 1  # var tracking the number of attempt(s)
    while not win and tried <= 6:
        print(f"=== Turn {tried}/6 ===")  # the number of try
        guess = input_guess(len(SECRET))  # obtaining user's guess
        print(emojified(guess, SECRET))  # print the emoji boxes according to user's guess
        if guess == SECRET:
            win = True  # win is the guess equals to the secret
        else:
            tried += 1  # keep looping if the guess is incorrect and the number of attempt is less or equal to 6
    if win:
        print(f"You won in {tried}/6 turns!")  # congrets msg if the user wins
    else:
        print("X/6 - Sorry, try again tomorrow!")  # sorry msg if the user loses


if __name__ == "__main__":
    main()  # declearing the main method