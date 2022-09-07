

"If you want to learn about the collatz problem, you can find it here https://en.wikipedia.org/wiki/Collatz_conjecture "


while True:
    try:
        x=int(input("x (positive and integer): "))
        if x<=0:
            raise ValueError
        else:
            break
    except ValueError:
        print("please enter a positive and integer")

def collatzProblem(x):
    y=0
    while True:
        if x==1:
            print(f"1 found after {y} transactions")
            break
        if x%2==0:
            x=x/2
            print(x)
            y+=1
        else:
            x=3*x+1
            print(x)
            y+=1

collatzProblem(x)
