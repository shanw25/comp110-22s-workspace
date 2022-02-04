"""A magic 8 ball oracle of truth about the future."""

from random import randint

input("Ask a yes or no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Yes, definitely!")
elif response == 1:
    print("Looking hopeful.")
elif response == 2:
    print("Ask again later")
else:
    print("No way. Not a chance.")
# i: int = 3
# s: str = ""

# while i > 0:
#     s = s + "h"
#     h: int = 0
#     while h < i:
#         s = s + "e"
#         h = h + 1
#     i = i - 1

# print(s)