def greatestOfThree():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>=b and a>=c:
        return f"{a} :is Greater"
    elif b>=a and b>=c:
        return f"{b} :is Greater"
    else:
        return f"{c} :is Greater"


print(greatestOfThree())