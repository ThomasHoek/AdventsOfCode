# L = length
# W = Width
# H = Height
# Want to order EXACTLY as much as they need
# Find the surface: 2*l*w + 2*w*h + 2*h*l
# Question: Total square feet

def formula(L: int, W: int, H: int) -> int:
    """Calculate the square feet and added paper

    Args:
        L (int): Length
        W (int): Width
        H (int): Height
    """
    return 2*L*W + 2*W*H + 2*H*L + min(L*W, W*H, H*L)


total = 0
puzzle_input = open("input.txt", "r").readlines()
for line in puzzle_input:
    l, w, h = map(int, line.split("x"))
    total += formula(l, w, h)
print(total)
