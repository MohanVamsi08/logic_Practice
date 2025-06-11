def fizzBuzz():
    n=int(input())
    a=int(input())
    b=int(input())
    for i in range(1, n+1):
        if i % a==0 and i % b==0:
            print("FizzBuzz")
        elif i%a==0:
            print("Fuzz")
        elif i%b==0:
            print("Buzz")
        else:
            print(i)
fizzBuzz()