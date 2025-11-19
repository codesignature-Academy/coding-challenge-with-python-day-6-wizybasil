"""
🔹FOR LOOP PROJECT: Square Numbers Calculator

=============== ✅ Task Description ================

Ask the user for a number **N**, then use a **for loop** to generate the squares of all numbers from **1 to N**, and store them in a list.

Example:
If the user enters **5**, the output list should be:
➡️ `[1, 4, 9, 16, 25]`

================ 🧠 What You Learn =================

* using `range()`
* list accumulation inside a loop
* basic arithmetic
* data structures (lists)
"""
# Square Numbers Calculator

N = int(input("Enter a number: "))
squares = []

for i in range(1, N + 1):
    squares.append(i * i)

print("The squares are:", squares)
