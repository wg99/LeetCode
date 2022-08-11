def isValid(s):
    stack = []
    closed_map = {'}': '{', ')': '(', ']': '['}
    for char in s:
        if char not in closed_map:
            stack.append(char)
        elif not stack or not stack.pop() == closed_map[char]:
            return False
    return not stack


print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('('))
