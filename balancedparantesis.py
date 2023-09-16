def is_balanced(s):
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if len(stack) == 0 or bracket_pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

s = input("Enter a string of brackets:")
print("Given string is balanced:", is_balanced(s))
