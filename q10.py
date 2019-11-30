
class Parentheses:

    def isValid(self, str):
        stack = []
        dict1 = {')': '(', ']': '[', '}': '{'}
        for char in str:
            if char in dict1.values():
                stack.append(char)
            elif char in dict1.keys():
                if stack == [] or dict1[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


p = Parentheses()

while 1:
    str = input('Input string with "()[]{}" (input \'q\' to quit): ')
    if str == 'q':
        break
    print(p.isValid(str))

