# Fuel Gauge Calculator ⛽

Hi! I just started learning Python a few days ago, and this is my third GitHub repository. 

This is a simple script that acts like a fuel gauge. You type in a fraction (like `3/4` or `1/2`), and the program calculates the percentage of fuel left. 

### How it works:
- If the fuel is 1% or less, it outputs **E** (Empty).
- If it's 99% or more, it outputs **F** (Full).
- If it's exactly 50%, it outputs **H** (Half).
- For anything else, it just gives you the rounded percentage.

### What I learned making this:
- **`try...except` blocks:** I learned how to stop the program from crashing if a user types a word instead of a number, or if they try to divide by zero.
- **String formatting:** I figured out how to use `:.0f` in f-strings so the percentages print as clean whole numbers instead of ugly decimals (like `0.5%`).
- **While loops:** How to use `while True` to keep asking the user for input until they actually type a valid fraction.

### How to run it
If you want to try it out, just import and run this in your terminal:
`main.py`

*(Note: I'm still a newbie, so the code is pretty basic, but I'm having fun learning and tracking my progress here!)*
