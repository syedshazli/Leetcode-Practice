#Notes
# A somewhat bruteforce solution, but could also attach all the necessary 'operations' in a set
# If something equals any of the operations  we pop the first 2 items on the stack and either add, subtract, multiply, divide
# Otherwise, just append the current token as an int
#return the only item left in the stack "stack[0]"
class Solution(object):
   
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
       

        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif tokens[i] == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif tokens[i] == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()
                if first * second < 0 and second % first != 0:
                        stack.append(second / first + 1)
                else:
                    stack.append(second / first)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
