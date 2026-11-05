def balanced_brackets(text):
    bracket_stack = []
    brackets = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    for character in text:
        if character in ("(", "[", "{"):
            bracket_stack.append(character)
        elif character in (")", "]", "}"):
            if len(bracket_stack) == 0:
                return False
            top_item = bracket_stack.pop()
            if top_item != brackets[character]:
                return False
    if len(bracket_stack) == 0:
        return True
    else:
        return False
    
print(balanced_brackets("(hello)")) 
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))