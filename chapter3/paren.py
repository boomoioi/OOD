inp = input("Enter expresion : ")
def paren(inp):
    open_close = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    stack = []
    for ch in inp:
        if ch in open_close.keys():
            stack.append(ch)
        elif ch in open_close.values():
            if not stack:
                return (f"{inp} close paren excess")
            checker = open_close[stack.pop()]
            if checker != ch:
                return(f"{inp} Unmatch open-close")
    if stack:
        return(f"{inp} open paren excess   {len(stack)} : {''.join(stack)}")
    return(f"{inp} MATCH")

print(paren(inp))