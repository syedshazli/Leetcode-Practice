stack = []
for i in range(len(s)):
    if s[i] == "[":
        stack.append("]")
    elif s[i] == "(":
        stack.append(")")
    elif s[i] == "{":
        stack.append("}")
    elif len(stack) == 0 or stack.pop() != s[i]:
        return False
return len(stack) == 0